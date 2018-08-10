from .parse_cdx import Cdx

def fix_kaitai_enum(Enum_cls):
    @classmethod
    def _missing_(cls, value):
        from types import SimpleNamespace
        val = SimpleNamespace()
        setattr(val, 'value', value)
        return val
    Enum_cls.Proptype._missing_ = _missing_

def default_format_mapper(form, data):
    "Callback for read_objs_from_doc to only return chemical files"
    if data.startswith(b'VjCD0100'):
        return ('cdx', data)
    elif (
            data[:4] == bytes([0xFF, 0xFE, 0xFF, 0xFF]) and
            data[6:16].decode('utf-16le') == '<?xml'
    ):
        endmarker = '</cml>'.encode('utf-16le')
        end = data.find(endmarker) + len(endmarker)
        if end == -1:
            return (None, None)
        mrv = data[6:end].decode('utf-16le').encode('utf-8')
        return ('mrv', mrv)
    else:
        # print('unknown format: ', form)
        pass
    return (None, None)


def read_mols_from_docx(filename, format_mapper=default_format_mapper):
    from .docx_handling import read_objs_from_doc
    from tempfile import NamedTemporaryFile
    import openbabel
    obconv = openbabel.OBConversion()
    for form, data in read_objs_from_doc(filename, mapper=format_mapper, paths=[['CONTENTS'], ['\x03PRINT'], ['MNOVA-CONTENTS']]):
        with NamedTemporaryFile() as tf:
            tf.write(data)
            tf.seek(0)
            try:
                if (form == 'cdx'):
                    mol = mol_from_cdx(tf.name)
                    obconv.SetInAndOutFormats(form, 'mol')
                    mdl = obconv.WriteString(mol)
                    if mdl: yield mdl
                else:
                    obconv.SetInAndOutFormats(form, 'mol')
                    mol = openbabel.OBMol()
                    obconv.ReadFile(mol, tf.name)
                    mdl = obconv.WriteString(mol)
                    if mdl: yield mdl
            except Exception as e:
                import sys
                print(f'Error in {filename}: {e}', file=sys.stderr)
                # raise

def create_mol(elems, bonds):
    import openbabel as ob
    mol = ob.OBMol()
    mol.BeginModify()
    atoms = []
    for e in elems:
        a = mol.NewAtom()
        atoms.append(a)
        a.SetAtomicNum(e['element'])
        a.SetSpinMultiplicity(e['spin'])
        a.SetFormalCharge(e['charge'])
        x, y, z = e.get('x', 0), e.get('y', 0), e.get('z', 0)
        # print('xyz', x, y, z)
        scaling = 1 / 65536.0 / 10
        a.SetVector(x * scaling, y * scaling, z * scaling)
    for b in bonds:
        order = 1
        ar = 0
        if b['order_flag'] == 0x0080:
            order = 5  # aromatic
        elif b['order_flag'] == 4:
            order = 3
        elif b['order_flag'] < 0:
            order = 1
        elif b['order_flag'] < 4:
            order = b['order_flag']
        else:
            order = 1
        if order > 0:
            mol.AddBond(b['begin'], b['end'], order)
        bond = mol.GetBond(mol.NumBonds() - 1)
        updown = b.get('updown')
        if updown == 'wedge': bond.SetWedge()
        if updown == 'hash': bond.SetHash()
    mol.Center()
    mol.EndModify()
    mol.DeleteData(ob.StereoData)
    ob.StereoFrom2D(mol)
    mol.SetChiralityPerceived()  # mark the molecule chirality as manually assinged to stop ob auto-guessing
    #         cfgs = []
    #         for a, e in zip(atoms, elems):
    #             if e.get('refs'):
    #                 refs = [r - 1 for r in e['refs']]  # 0-based
    #                 # view 3 atoms from the previous atom
    #                 from_id = refs[0] #min(refs)
    #                 refs = [*(set(refs)-set([from_id]))]
    #                 print(f'atom {a.GetId()}, from {from_id}')
    #                 pprint(refs)
    #                 cfgs.append(gen_stereo_config_for_atom(a.GetId(), refs, from_id))
    #         apply_stereo_configs(mol, cfgs)
    return mol


def mol_from_cdx(filename):
    from .parse_cdx import Cdx
    fix_kaitai_enum(Cdx)
    f = Cdx.from_file(filename)
    root = f.document.content[0]

    def find_chem_objects(root, ret=None):
        from collections import OrderedDict
        if (ret is None):
            ret = OrderedDict()
        if (hasattr(root, 'obj')):
            el = root.obj
            obj_id = str(el.obj_id)
            ret[obj_id] = ret.get(obj_id, {})
            r = ret[obj_id]
            for prop in el.content:
                if hasattr(prop, 'obj'):
                    find_chem_objects(prop, ret)
                if hasattr(prop, 'prop'):
                    tag = prop.tag
                    p = prop.prop
                    if tag == Cdx.Proptype.node_element:
                        r['type'] = 'element'
                        r['element'] = p.content
                    if tag == Cdx.Proptype.x2d_position:
                        r['y'], r['x'] = p.content.yx
                    if tag == Cdx.Proptype.x3d_position:
                        r['y'], r['x'], r['z'] = p.content.zyx
                    if tag == Cdx.Proptype.atom_charge:
                        r['charge'] = p.content
                    if tag == Cdx.Proptype.atom_radical:
                        r['spin'] = p.content
                    if tag == Cdx.Proptype.bond_display:
                        stereo = p.content
                        if (stereo == 3 or stereo == 4): r['updown'] = 'wedge'
                        if (stereo == 6 or stereo == 7): r['updown'] = 'hash'
                    if tag == Cdx.Proptype.atom_bond_ordering:  # or tag == Cdx.Proptype.bond_bond_ordering:
                        r['refs'] = [str(obj.obj_id) for obj in p.content.objs if obj.obj_id != 0]
                    if tag == Cdx.Proptype.bond_begin:
                        r['type'] = 'bond'
                        r['begin'] = str(p.content.obj_id)
                    if tag == Cdx.Proptype.bond_end:
                        r['type'] = 'bond'
                        r['end'] = str(p.content.obj_id)
                    if tag == Cdx.Proptype.bond_order:
                        r['order_flag'] = p.content  # not actually bond order, see create_mol
        return ret

    def insert_defaults(objlist):
        from collections import OrderedDict
        assert (isinstance(objlist,
                           OrderedDict)), "Regular dict does not preserve order and CDX depends on object order to provide stereochemistry."
        ret = objlist.copy()
        for k, v in objlist.items():
            if v.get('type') == 'bond':
                # mark bound objects as elements
                ret[v['end']]['type'] = 'element'
                ret[v['begin']]['type'] = 'element'

        def augment_with_defaults(v):
            if v['type'] == 'element': return {'spin': 0, 'charge': 0, 'element': 6, **v}
            if v['type'] == 'bond': return {'order_flag': 1, **v}
            return v

        ret = OrderedDict(
            [(k, augment_with_defaults(v)) for k, v in ret.items() if v.get('type')])  # filter out unknown stuff
        return ret

    def renumber_elements(root):
        elems = []
        elem_map = {}
        from collections import OrderedDict
        assert (isinstance(root,
                           OrderedDict)), "Regular dict does not preserve order and CDX depends on object order to provide stereochemistry."
        for k, v in root.items():
            if v['type'] == 'element':
                elems.append(v)
                elem_map[k] = len(elems)  # 1-based
        bonds = []
        for k, v in root.items():
            #             if v.get('refs') and v['type'] == 'element':
            #                 elem_id = elem_map[k] - 1
            #                 refs = enumerate_bound_atoms(k, [root[el] for el in v['refs']])
            #                 elems[elem_id] = {**elems[elem_id], 'refs': [elem_map[r] for r in refs]}
            if v['type'] == 'bond':
                bonds.append({**v, 'begin': elem_map[v['begin']], 'end': elem_map[v['end']]})
        return elems, bonds

    objects = find_chem_objects(root)
    from pprint import pprint
    objects = insert_defaults(objects)
    #     pprint(objects)
    elems, bonds = renumber_elements(objects)
    #     pprint(bonds)
    #     pprint(elems)
    mol = create_mol(elems, bonds)
    return mol

