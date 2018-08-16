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


def rd_map_from_ob(mol):
    from rdkit.Chem import RWMol, Atom, BondType
    rm = RWMol()
    for i in range(mol.NumAtoms()):
        a = mol.GetAtomById(i)
        ra = Atom(a.GetAtomicNum())
        rm.AddAtom(ra)
    for i in range(mol.NumBonds()):
        b = mol.GetBondById(i)
        b.GetBeginAtom().GetId()
        order = BondType.SINGLE
        if b.GetBO() == 2:
            order = BondType.DOUBLE
        if b.GetBO() == 3:
            order = BondType.TRIPLE
        rm.AddBond(b.GetBeginAtom().GetId(), b.GetEndAtom().GetId(),order)#b.GetBondOrder())
    return rm


def read_mols_from_docx(filename, format_mapper=default_format_mapper,*, rIds=None):
    from .docx_handling import read_objs_from_doc
    from tempfile import NamedTemporaryFile
    import openbabel
    obconv = openbabel.OBConversion()
    for form, data in read_objs_from_doc(filename, mapper=format_mapper, paths=[['CONTENTS'], ['\x03PRINT'], ['MNOVA-CONTENTS']], rIds=rIds):
        if data is None:
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
                #print(f'Error in {filename}: {e}', file=sys.stderr)
                raise


# def gen_tetrahedral_stereo_config_for_atom(atom_id, refs, from_id):
#     """ Chirality data uses atom IDs rather than IDX
#     If we have neighbor info, then tetrahedral stereo might be described with only 1 bit: parity. This is a more general impl
#     """
#     IMPLICIT_REF = 4294967294
#     def array_pad(arr, val, min_len):
#         return [*arr, *[val for _ in range(max([0, min_len-len(arr)]))]]
#     obs = openbabel.OBStereo
#     cfg = ob.OBTetrahedralConfig()
#     cfg.view = obs.ViewFrom
#     cfg.winding = obs.AntiClockwise
#     cfg.center = atom_id
#     cfg.refs = array_pad(refs, IMPLICIT_REF, 3)
#     cfg.from_or_towards = from_id
#     cfg.specified = True
#     return cfg

# def gen_tetrahedral_stereo_config_from_parity(mol, center_id, parity):
#     atom = mol.GetAtomById(center_id)
#     neighbors = [n.GetId() for n in openbabel.OBAtomAtomIter(atom)]
#     from_id = min(neighbors)
#     refs = neighbors if parity else reversed(neighbors)
#     cfg = gen_tetrahedral_stereo_config_for_atom(cente_id, refs, from_id)
#     return cfg

# def apply_tetrahedral_stereo_configs(mol, cfgs):
#     mol.DeleteData(openbabel.StereoData)
#     mol.SetChiralityPerceived()  # mark the molecule chirality as manually assinged to stop ob auto-guessing
#     ts = ob.OBTetrahedralStereo(mol)
#     for cfg in cfgs:
#         ts = ob.OBTetrahedralStereo(mol)
#         ts.SetConfig(cfg)
#         mol.CloneData(ts)
# #     mol.CloneData(ts)

def apply_cistrans(mol, bond_id, refs):
    import openbabel as ob
    bond = mol.GetBond(bond_id)
    if not refs: return
    if bond.GetBO() != 2:
        print('Non-double bond has cistrans stereo')
        return
    neighbors1 = [n.GetId() for n in ob.OBAtomAtomIter(bond.GetBeginAtom())]
    neighbors2 = [n.GetId() for n in ob.OBAtomAtomIter(bond.GetEndAtom())]
    
    #print(f'applying cistrans {refs} to bond {bond_id}, neighbors: {neighbors1} {neighbors2}')
    IMPLICIT_REF = 4294967294
    ct_stereo = ob.OBCisTransStereo(mol)
    config = ct_stereo.GetConfig()
    config.begin = bond.GetBeginAtom().GetId()
    config.end = bond.GetEndAtom().GetId()
    config.refs = [(r if r is not None else IMPLICIT_REF) for r in refs]
    config.specified = True
    ct_stereo.SetConfig(config)
    mol.CloneData(ct_stereo)

def create_mol(elems, bonds):
    import openbabel as ob
    mol = ob.OBMol()
    mol.SetDimension(2)
    mol.BeginModify()
    atoms = []
    aliases = []
    bond_refs = {}
    for e in elems:
        a = mol.NewAtom()
        atoms.append(a)
        a.SetAtomicNum(e['element'])
        x, y, z = e.get('x', 0), e.get('y', 0), e.get('z', 0)
        # print('xyz', x, y, z)
        scaling = 1 / 65536.0 / 10
        a.SetVector(x * scaling, y * scaling, z * scaling)
        if e['type'] == 'alias':
            text = e.get('text')
            if text:
                ad = ob.AliasData()
                ad.SetAlias(text)
                ad.SetOrigin(ob.fileformatInput)
                aliases.append((a, ad))
            continue
        a.SetSpinMultiplicity(e['spin'])
        a.SetFormalCharge(e['charge'])
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
            # Create bond and set bond stereo
            stereo = b.get('bond_stereo')
            if (stereo in [4,7,10,12]):
                b_begin, b_end = b['end'], b['begin']
            else:
                b_begin, b_end = b['begin'], b['end']
            mol.AddBond(b_begin, b_end, order)
            # mol.AddBond(b['begin'], b['end'], order)
            # set double bond stereo
            bond_id = mol.NumBonds() - 1
            bond_refs[bond_id] = b.get('bond_refs')
            bond = mol.GetBond(bond_id)
            if (stereo == 3 or stereo == 4): bond.SetWedge()
            if (stereo == 6 or stereo == 7): bond.SetHash()

    mol.Center()
    #mol.DeleteData(ob.StereoData)
    ob.StereoFrom2D(mol)  # TODO: check E-Z correspondence & roundtrip
    mol.EndModify()
    mol.SetChiralityPerceived()  # mark the molecule chirality as manually assinged to stop ob auto-guessing

    for bond_id in range(mol.NumBonds()):
        refs = bond_refs.get(bond_id)
        # print(refs)
        if not refs: continue   
        apply_cistrans(mol, bond_id, [(r - 1 if r is not None else None) for r in refs])
    
    # Expand aliases
    for a, ad in aliases:
        if (not ad.IsExpanded()):
            ad.Expand(mol, a.GetIdx()) # Make chemically meaningful, if possible.
    #         cfgs = []
    #         for a, e in zip(atoms, elems):
    #             if e.get('refs'):
    #                 refs = [r - 1 for r in e['refs']]  # 0-based
    #                 # view 3 atoms from the previous atom
    #                 from_id = refs[0] #min(refs)
    #                 refs = [*(set(refs)-set([from_id]))]
    #                 print(f'atom {a.GetId()}, from {from_id}')
    #                 pprint(refs)
    #                 cfgs.append(gen_tetrahedral_stereo_config_for_atom(a.GetId(), refs, from_id))
    #         apply_tetrahedral_stereo_configs(mol, cfgs)

    return mol


def mol_from_cdx_bytes(data):
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile() as tf:
        tf.write(data)
        tf.seek(0)
        return mol_from_cdx(tf.name)


def mol_from_cdx(filename):
    from .parse_cdx import Cdx
    fix_kaitai_enum(Cdx)
    f = Cdx.from_file(filename)

    def find_chem_objects(root, ret=None):
        from collections import OrderedDict
        if (ret is None):
            ret = OrderedDict()
        if (hasattr(root, 'obj')):
            el = root.obj
            obj_id = str(el.obj_id)
            ret[obj_id] = ret.get(obj_id, {})
            r = ret[obj_id]
            skip_objects = set()
            def find_in_node(node, tag):
                for ent in node.content:
                    if ent.tag != tag: continue
                    return ent
            
            for prop in el.content:
                if hasattr(prop, 'obj') and prop.obj.obj_id not in skip_objects:
                    find_chem_objects(prop, ret)
                if hasattr(prop, 'prop'):
                    tag = prop.tag
                    p = prop.prop
                    if tag == Cdx.Proptype.node_type:
                        nt = p.content
                        if (nt == 4 or nt == 5): # Nickname or fragment
                            r['type'] = 'alias'
                            # print('alias', hex(el.obj_id))
                            obj_text = find_in_node(el, Cdx.Proptype.obj_text)
                            obj_fragment = find_in_node(el, Cdx.Proptype.obj_fragment)
                            if obj_text:
                                to = obj_text.obj
                                skip_objects.add(to.obj_id)
                                text_prop = find_in_node(to, Cdx.Proptype.text)
                                if text_prop: r['text'] = text_prop.prop.content.text
                            if obj_fragment: skip_objects.add(obj_fragment.obj.obj_id)
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
                        r['bond_stereo'] = p.content
                    if tag == Cdx.Proptype.bond_bond_ordering:
                        r['bond_refs'] = [(str(obj.obj_id) if obj.obj_id != 0 else None ) for obj in p.content.objs]
                    if tag == Cdx.Proptype.atom_bond_ordering:
                        r['refs'] = [(str(obj.obj_id) if obj.obj_id != 0 else None ) for obj in p.content.objs]
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
                ret[v['end']]['type'] = ret[v['end']].get('type', 'element')
                ret[v['begin']]['type'] = ret[v['begin']].get('type', 'element')
                pass

        def augment_with_defaults(v):
            if v['type'] == 'alias': return {**v, 'element': 0}
            if v['type'] == 'element': return {'spin': 0, 'charge': 0, 'element': 6, **v}
            if v['type'] == 'bond': return {'order_flag': 1, **v}
            return v

        ret = OrderedDict(
            [(k, augment_with_defaults(v)) for k, v in ret.items() if v.get('type')])  # filter out unknown stuff
        return ret

    def renumber_elements(root):
        def enumerate_bound_atoms(root_atoms, bonds):
            ret = []
            for b in bonds:
                if b is None:
                    ret.append(None)
                    continue
                other = list(set([b['begin'], b['end']]) - set(root_atoms))
                if (len(other)):
                    ret.append(other[0])
            return ret
        elems = []
        elem_map = {}
        from collections import OrderedDict
        assert (isinstance(root,
                           OrderedDict)), "Regular dict does not preserve order and CDX depends on object order to provide stereochemistry."
        for k, v in root.items():
            if (v['type'] == 'element'):
                elems.append({**v, 'obj_id': k})
                elem_map[k] = len(elems)  # 1-based
            if (v['type'] == 'alias'): # or (v.get('text') is not None and not v.get('element')):
                elems.append({**v, 'type': 'alias', 'obj_id': k})
                elem_map[k] = len(elems)  # 1-based
        bonds = []
        for k, v in root.items():
            if v['type'] == 'element':
                if v.get('refs'):
                    elem_id = elem_map[k] - 1
                    refs = enumerate_bound_atoms([k], [root.get(r) for r in v['refs']])
                    new_refs = [(elem_map[r] if r else None) for r in refs]
                    elems[elem_id] = {**elems[elem_id], 'refs': new_refs}
            if v['type'] == 'bond':
                newbond = {**v, 'begin': elem_map[v['begin']], 'end': elem_map[v['end']]}
                if v.get('bond_refs'):
                    refs = enumerate_bound_atoms([v['begin'], v['end']], [root.get(r) for r in v['bond_refs']])
                    new_refs = [(elem_map[r] if r else None) for r in refs]
                    newbond = {**newbond, 'bond_refs': new_refs}
                bonds.append(newbond)
        return elems, bonds

    from collections import OrderedDict
    objects = OrderedDict()
    for root in f.document.content:
        find_chem_objects(root, objects)
    from pprint import pprint
    objects = insert_defaults(objects)
    #     pprint(objects)
    elems, bonds = renumber_elements(objects)
    #     pprint(bonds)
    #     pprint(elems)
    mol = create_mol(elems, bonds)
    return mol


