# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import struct


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Cdx(KaitaiStruct):

    class Proptype(Enum):
        end_object = 0
        creation_user_name = 1
        creation_date = 2
        creation_program = 3
        modification_user_name = 4
        modification_date = 5
        modification_program = 6
        unused1 = 7
        name = 8
        comment = 9
        z_order = 10
        registry_number = 11
        registry_authority = 12
        unused2 = 13
        represents_property = 14
        ignore_warnings = 15
        chemical_warning = 16
        visible = 17
        font_table = 256
        x2d_position = 512
        x3d_position = 513
        x2d_extent = 514
        x3d_extent = 515
        bounding_box = 516
        rotation_angle = 517
        bounds_in_parent = 518
        x3d_head = 519
        x3d_tail = 520
        top_left = 521
        top_right = 522
        bottom_right = 523
        bottom_left = 524
        color_table = 768
        foreground_color = 769
        background_color = 770
        node_type = 1024
        node_label_display = 1025
        node_element = 1026
        atom_element_list = 1027
        atom_formula = 1028
        atom_isotope = 1056
        atom_charge = 1057
        atom_radical = 1058
        atom_restrict_free_sites = 1059
        atom_restrict_implicit_hydrogens = 1060
        atom_restrict_ring_bond_count = 1061
        atom_restrict_unsaturated_bonds = 1062
        atom_restrict_rxn_change = 1063
        atom_restrict_rxn_stereo = 1064
        atom_abnormal_valence = 1065
        unused3 = 1066
        atom_num_hydrogens = 1067
        unused4 = 1068
        unused5 = 1069
        atom_h_dot = 1070
        atom_h_dash = 1071
        atom_geometry = 1072
        atom_bond_ordering = 1073
        node_attachments = 1074
        atom_generic_nickname = 1075
        atom_alt_group_id = 1076
        atom_restrict_substituents_up_to = 1077
        atom_restrict_substituents_exactly = 1078
        atom_cip_stereochemistry = 1079
        atom_translation = 1080
        atom_atom_number = 1081
        atom_show_query = 1082
        atom_show_stereo = 1083
        atom_show_atom_number = 1084
        atom_link_count_low = 1085
        atom_link_count_high = 1086
        atom_isotopic_abundance = 1087
        atom_external_connection_type = 1088
        mole_racemic = 1280
        mole_absolute = 1281
        mole_relative = 1282
        mole_formula = 1283
        mole_weight = 1284
        frag_connection_order = 1285
        bond_order = 1536
        bond_display = 1537
        bond_display2 = 1538
        bond_double_position = 1539
        bond_begin = 1540
        bond_end = 1541
        bond_restrict_topology = 1542
        bond_restrict_rxn_participation = 1543
        bond_begin_attach = 1544
        bond_end_attach = 1545
        bond_cip_stereochemistry = 1546
        bond_bond_ordering = 1547
        bond_show_query = 1548
        bond_show_stereo = 1549
        bond_crossing_bonds = 1550
        bond_show_rxn = 1551
        text = 1792
        justification = 1793
        line_height = 1794
        word_wrap_width = 1795
        line_starts = 1796
        label_alignment = 1797
        label_line_height = 1798
        caption_line_height = 1799
        interpret_chemically = 1800
        mac_print_info = 2048
        win_print_info = 2049
        print_margins = 2050
        chain_angle = 2051
        bond_spacing = 2052
        bond_length = 2053
        bold_width = 2054
        line_width = 2055
        margin_width = 2056
        hash_spacing = 2057
        label_style = 2058
        caption_style = 2059
        caption_justification = 2060
        fractional_widths = 2061
        magnification = 2062
        width_pages = 2063
        height_pages = 2064
        drawing_space_type = 2065
        width = 2066
        height = 2067
        page_overlap = 2068
        header = 2069
        header_position = 2070
        footer = 2071
        footer_position = 2072
        print_trim_marks = 2073
        label_style_font = 2074
        caption_style_font = 2075
        label_style_size = 2076
        caption_style_size = 2077
        label_style_face = 2078
        caption_style_face = 2079
        label_style_color = 2080
        caption_style_color = 2081
        bond_spacing_abs = 2082
        label_justification = 2083
        fix_inplace_extent = 2084
        side = 2085
        fix_inplace_gap = 2086
        window_is_zoomed = 2304
        window_position = 2305
        window_size = 2306
        graphic_type = 2560
        line_type = 2561
        arrow_type = 2562
        rectangle_type = 2563
        oval_type = 2564
        orbital_type = 2565
        bracket_type = 2566
        symbol_type = 2567
        curve_type = 2568
        arrow_head_size = 2592
        arc_angular_size = 2593
        bracket_lip_size = 2594
        curve_points = 2595
        bracket_usage = 2596
        polymer_repeat_pattern = 2597
        polymer_flip_type = 2598
        bracketed_objects = 2599
        bracket_repeat_count = 2600
        bracket_component_order = 2601
        bracket_sru_label = 2602
        bracket_graphic_id = 2603
        bracket_bond_id = 2604
        bracket_inner_atom_id = 2605
        curve_points3d = 2606
        picture_edition = 2656
        picture_edition_alias = 2657
        mac_pict = 2658
        windows_metafile = 2659
        ole_object = 2660
        enhanced_metafile = 2661
        spectrum_x_spacing = 2688
        spectrum_x_low = 2689
        spectrum_x_type = 2690
        spectrum_y_type = 2691
        spectrum_x_axis_label = 2692
        spectrum_y_axis_label = 2693
        spectrum_data_point = 2694
        spectrum_class = 2695
        spectrum_y_low = 2696
        spectrum_y_scale = 2697
        tlc_origin_fraction = 2720
        tlc_solvent_front_fraction = 2721
        tlc_show_origin = 2722
        tlc_show_solvent_front = 2723
        tlc_show_borders = 2724
        tlc_show_side_ticks = 2725
        tlc_rf = 2736
        tlc_tail = 2737
        tlc_show_rf = 2738
        named_alternative_group_text_frame = 2816
        named_alternative_group_group_frame = 2817
        named_alternative_group_valence = 2818
        geometric_feature = 2944
        relation_value = 2945
        basis_objects = 2946
        constraint_type = 2947
        constraint_min = 2948
        constraint_max = 2949
        ignore_unconnected_atoms = 2950
        dihedral_is_chiral = 2951
        point_is_directed = 2952
        reaction_step_atom_map = 3072
        reaction_step_reactants = 3073
        reaction_step_products = 3074
        reaction_step_plusses = 3075
        reaction_step_arrows = 3076
        reaction_step_objects_above_arrow = 3077
        reaction_step_objects_below_arrow = 3078
        reaction_step_atom_map_manual = 3079
        reaction_step_atom_map_auto = 3080
        object_tag_type = 3328
        unused6 = 3329
        unused7 = 3330
        object_tag_tracking = 3331
        object_tag_persistent = 3332
        object_tag_value = 3333
        positioning = 3334
        positioning_angle = 3335
        positioning_offset = 3336
        sequence_identifier = 3584
        cross_reference_container = 3840
        cross_reference_document = 3841
        cross_reference_identifier = 3842
        cross_reference_sequence = 3843
        template_pane_height = 4096
        template_num_rows = 4097
        template_num_columns = 4098
        group_integral = 4352
        splitter_positions = 8176
        page_definition = 8177
        user_temporary_begin = 16384
        user_temporary_end = 17408
        obj_document = 32768
        obj_page = 32769
        obj_group = 32770
        obj_fragment = 32771
        obj_node = 32772
        obj_bond = 32773
        obj_text = 32774
        obj_graphic = 32775
        obj_curve = 32776
        obj_embedded_object = 32777
        obj_named_alternative_group = 32778
        obj_template_grid = 32779
        obj_registry_number = 32780
        obj_reaction_scheme = 32781
        obj_reaction_step = 32782
        obj_object_definition = 32783
        obj_spectrum = 32784
        obj_object_tag = 32785
        obj_ole_client_item = 32786
        obj_sequence = 32787
        obj_cross_reference = 32788
        obj_splitter = 32789
        obj_table = 32790
        obj_bracketed_group = 32791
        obj_bracket_attachment = 32792
        obj_crossing_bond = 32793
        obj_border = 32800
        obj_geometry = 32801
        obj_constraint = 32802
        obj_tlc_plate = 32803
        obj_tlc_lane = 32804
        obj_tlc_spot = 32805
        obj_unknown_object = 36863

        @classmethod
        def _missing_(cls, value):
            from types import SimpleNamespace
            val = SimpleNamespace()
            setattr(val, 'value', value)
            return val

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.header = self._root.Header(self._io, self, self._root)
        self._raw_document = self._io.read_bytes_full()
        io = KaitaiStream(BytesIO(self._raw_document))
        self.document = self._root.Document(io, self, self._root)

    class CdxCipStereoAtom(KaitaiStruct):

        class Stereo(Enum):
            u = 0
            n = 1
            r = 2
            s = 3
            pr = 4
            ps = 5
            unspecified = 6
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.stereo = self._root.CdxCipStereoAtom.Stereo(self._io.read_s1())


    class CdxRawString(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = (self._io.read_bytes_full()).decode(u"cp1251")


    class Int16ListWithCounts(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_values = self._io.read_u2le()
            self.values = [None] * (self.num_values)
            for i in range(self.num_values):
                self.values[i] = self._io.read_u2le()



    class CdxFontTable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.platform = self._io.read_u2le()
            self.num_styleruns = self._io.read_u2le()
            self.styleruns = [None] * (self.num_styleruns)
            for i in range(self.num_styleruns):
                self.styleruns[i] = self._root.CdxFontTable.Stylerun(self._io, self, self._root)


        class Stylerun(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.font_id = self._io.read_u2le()
                self.charset = self._io.read_u2le()
                self.font_name_length = self._io.read_u2le()
                self.font_name = (self._io.read_bytes(self.font_name_length)).decode(u"cp1251")



    class CdxString(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_styleruns = self._io.read_u2le()
            self.styleruns = [None] * (self.num_styleruns)
            for i in range(self.num_styleruns):
                self.styleruns[i] = self._root.CdxString.Stylerun(self._io, self, self._root)

            self.text = (self._io.read_bytes_full()).decode(u"cp1251")

        class Stylerun(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.starts = self._io.read_u2le()
                self.style = self._root.CdxFontStyle(self._io, self, self._root)



    class Document(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.content = []
            i = 0
            while not self._io.is_eof():
                self.content.append(self._root.Entity(self._io, self, self._root))
                i += 1



    class CdxObjectId(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.obj_id = self._io.read_u4le()


    class CdxFontStyle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.font_table_index = self._io.read_u2le()
            self.flags = self._io.read_u2le()
            self.size = self._io.read_u2le()
            self.color = self._io.read_u2le()


    class CdxDate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.year = self._io.read_s2le()
            self.month = self._io.read_s2le()
            self.day = self._io.read_s2le()
            self.hour = self._io.read_s2le()
            self.minute = self._io.read_s2le()
            self.second = self._io.read_s2le()
            self.milliseconds = self._io.read_s2le()


    class CdxObjectIdArrayWithCounts(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_objs = self._io.read_u2le()
            self.objs = [None] * (self.num_objs)
            for i in range(self.num_objs):
                self.objs[i] = self._root.CdxObjectId(self._io, self, self._root)



    class Obj(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.obj_id = self._io.read_u4le()
            self.content = []
            i = 0
            while True:
                _ = self._root.Entity(self._io, self, self._root)
                self.content.append(_)
                if _.tag == self._root.Proptype.end_object:
                    break
                i += 1


    class CdxRectangle(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tlbr = [None] * (4)
            for i in range(4):
                self.tlbr[i] = self._io.read_s4le()



    class CdxObject(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._root.CdxUnknown(self._io, self, self._root)


    class CdxCurvePoints3d(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_points = self._io.read_u2le()
            self.points = [None] * (self.num_points)
            for i in range(self.num_points):
                self.points[i] = self._root.CdxPoint3d(self._io, self, self._root)



    class CdxObjectIdArray(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.objs = []
            i = 0
            while not self._io.is_eof():
                self.objs.append(self._root.CdxObjectId(self._io, self, self._root))
                i += 1



    class CdxPoint3d(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.zyx = [None] * (3)
            for i in range(3):
                self.zyx[i] = self._io.read_s4le()



    class CdxRepresentsProperty(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.obj_id = self._root.CdxObjectId(self._io, self, self._root)
            self.prop_tag = self._io.read_u2le()


    class CdxCipStereoBond(KaitaiStruct):

        class Stereo(Enum):
            u = 0
            n = 1
            e = 2
            z = 3
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.stereo = self._root.CdxCipStereoBond.Stereo(self._io.read_s1())


    class Entity(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tag = self._root.Proptype(self._io.read_u2le())
            if  ((self.tag.value < 32768) and (self.tag != self._root.Proptype.end_object)) :
                self.prop = self._root.Prop(self._io, self, self._root)

            if  ((self.tag.value >= 32768) and (self.tag != self._root.Proptype.end_object)) :
                self.obj = self._root.Obj(self._io, self, self._root)



    class CdxBooleanImplied(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.content = self._io.read_bytes(self._parent.len)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = self._parent.len > 0
            return self._m_value if hasattr(self, '_m_value') else None


    class CdxCoordinate(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s4le()


    class CdxBoolean(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s1()


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.ensure_fixed_contents(struct.pack('22b', 86, 106, 67, 68, 48, 49, 48, 48, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


    class CdxFormula(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._root.CdxUnknown(self._io, self, self._root)


    class Prop(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_u2le()
            _on = self._parent.tag
            if _on == self._root.Proptype.fix_inplace_extent:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.tlc_tail:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.creation_date:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxDate(io, self, self._root)
            elif _on == self._root.Proptype.rotation_angle:
                self.content = self._io.read_s4le()
            elif _on == self._root.Proptype.bond_double_position:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_group:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.atom_external_connection_type:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.atom_restrict_substituents_up_to:
                self.content = self._io.read_u1()
            elif _on == self._root.Proptype.word_wrap_width:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_sequence:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.tlc_show_rf:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.registry_authority:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.atom_restrict_free_sites:
                self.content = self._io.read_u1()
            elif _on == self._root.Proptype.arrow_head_size:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_curve:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.window_size:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.bold_width:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.oval_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.windows_metafile:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.polymer_flip_type:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.atom_show_atom_number:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.basis_objects:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.atom_abnormal_valence:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.bond_end_attach:
                self.content = self._io.read_u1()
            elif _on == self._root.Proptype.header:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.top_left:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.constraint_type:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.atom_show_stereo:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.tlc_show_borders:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.obj_fragment:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.bond_display2:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.header_position:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.atom_isotopic_abundance:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.node_attachments:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArrayWithCounts(io, self, self._root)
            elif _on == self._root.Proptype.spectrum_x_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bracket_component_order:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.color_table:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxColorTable(io, self, self._root)
            elif _on == self._root.Proptype.tlc_solvent_front_fraction:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.bracket_inner_atom_id:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectId(io, self, self._root)
            elif _on == self._root.Proptype.atom_restrict_implicit_hydrogens:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.magnification:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.label_style_color:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.unused2:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.obj_tlc_plate:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.atom_element_list:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxElementList(io, self, self._root)
            elif _on == self._root.Proptype.label_style_size:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bracket_graphic_id:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectId(io, self, self._root)
            elif _on == self._root.Proptype.reaction_step_atom_map:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.atom_alt_group_id:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectId(io, self, self._root)
            elif _on == self._root.Proptype.atom_restrict_ring_bond_count:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.obj_object_tag:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.x3d_tail:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint3d(io, self, self._root)
            elif _on == self._root.Proptype.bond_length:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.x3d_head:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint3d(io, self, self._root)
            elif _on == self._root.Proptype.spectrum_y_axis_label:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.mole_relative:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.top_right:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.chemical_warning:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.reaction_step_arrows:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.footer_position:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.atom_restrict_substituents_exactly:
                self.content = self._io.read_u1()
            elif _on == self._root.Proptype.reaction_step_plusses:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.creation_user_name:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.bond_spacing:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.width_pages:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.spectrum_y_scale:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.atom_geometry:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.window_position:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.named_alternative_group_text_frame:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxRectangle(io, self, self._root)
            elif _on == self._root.Proptype.obj_tlc_spot:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.atom_radical:
                self.content = self._io.read_u1()
            elif _on == self._root.Proptype.bond_begin_attach:
                self.content = self._io.read_u1()
            elif _on == self._root.Proptype.named_alternative_group_group_frame:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxRectangle(io, self, self._root)
            elif _on == self._root.Proptype.label_style_font:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.positioning:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.reaction_step_products:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.obj_document:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.label_line_height:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_cross_reference:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.atom_h_dot:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.bond_bond_ordering:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.end_object:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.reaction_step_objects_above_arrow:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.caption_justification:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.object_tag_persistent:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.obj_spectrum:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.mac_print_info:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.obj_named_alternative_group:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.interpret_chemically:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.bond_end:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectId(io, self, self._root)
            elif _on == self._root.Proptype.orbital_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.fractional_widths:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.bond_show_rxn:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.bond_begin:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectId(io, self, self._root)
            elif _on == self._root.Proptype.spectrum_x_spacing:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.spectrum_y_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.drawing_space_type:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.margin_width:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.visible:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.obj_unknown_object:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.reaction_step_atom_map_auto:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.background_color:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bond_restrict_topology:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.caption_line_height:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.mole_racemic:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.cross_reference_document:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.modification_user_name:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.bond_crossing_bonds:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.bond_show_query:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.atom_num_hydrogens:
                self.content = self._io.read_u2le()
            elif _on == self._root.Proptype.line_starts:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.Int16ListWithCounts(io, self, self._root)
            elif _on == self._root.Proptype.mole_weight:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.point_is_directed:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.reaction_step_atom_map_manual:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.bounding_box:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxRectangle(io, self, self._root)
            elif _on == self._root.Proptype.x2d_extent:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.splitter_positions:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.bottom_right:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.obj_bracket_attachment:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.template_num_rows:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.label_style_face:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.label_style:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxFontStyle(io, self, self._root)
            elif _on == self._root.Proptype.unused3:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bracket_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.win_print_info:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.label_alignment:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.hash_spacing:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.caption_style_color:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bracket_bond_id:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectId(io, self, self._root)
            elif _on == self._root.Proptype.atom_bond_ordering:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.atom_formula:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxFormula(io, self, self._root)
            elif _on == self._root.Proptype.obj_constraint:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.relation_value:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.bond_order:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.atom_translation:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.spectrum_x_axis_label:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.obj_geometry:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.curve_points:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCurvePoints(io, self, self._root)
            elif _on == self._root.Proptype.text:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.atom_h_dash:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.constraint_min:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.spectrum_y_low:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.name:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxRawString(io, self, self._root)
            elif _on == self._root.Proptype.height:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.node_label_display:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.ignore_unconnected_atoms:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.bracket_repeat_count:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bond_restrict_rxn_participation:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.footer:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.caption_style_font:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_embedded_object:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.width:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.object_tag_tracking:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.atom_link_count_low:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.positioning_offset:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.atom_cip_stereochemistry:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCipStereoAtom(io, self, self._root)
            elif _on == self._root.Proptype.justification:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.atom_generic_nickname:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.comment:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.page_overlap:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.graphic_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.z_order:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.foreground_color:
                self.content = self._io.read_u2le()
            elif _on == self._root.Proptype.obj_table:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.page_definition:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.sequence_identifier:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.symbol_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_text:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.picture_edition:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.represents_property:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxRepresentsProperty(io, self, self._root)
            elif _on == self._root.Proptype.modification_program:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.positioning_angle:
                self.content = self._io.read_s4le()
            elif _on == self._root.Proptype.picture_edition_alias:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.bond_spacing_abs:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.reaction_step_reactants:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.line_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.spectrum_x_low:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.reaction_step_objects_below_arrow:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.tlc_show_solvent_front:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.enhanced_metafile:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.atom_link_count_high:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.curve_points3d:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCurvePoints3d(io, self, self._root)
            elif _on == self._root.Proptype.caption_style_size:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.atom_restrict_rxn_stereo:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.unused7:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.object_tag_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.caption_style_face:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.polymer_repeat_pattern:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.atom_atom_number:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.spectrum_class:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.geometric_feature:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.line_width:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.user_temporary_end:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.registry_number:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.tlc_show_side_ticks:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.bond_display:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.arc_angular_size:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_splitter:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.arrow_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.cross_reference_sequence:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.atom_restrict_unsaturated_bonds:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.modification_date:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxDate(io, self, self._root)
            elif _on == self._root.Proptype.dihedral_is_chiral:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.x3d_extent:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint3d(io, self, self._root)
            elif _on == self._root.Proptype.obj_bracketed_group:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.caption_style:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxFontStyle(io, self, self._root)
            elif _on == self._root.Proptype.unused5:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.frag_connection_order:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.named_alternative_group_valence:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.x3d_position:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint3d(io, self, self._root)
            elif _on == self._root.Proptype.obj_bond:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.chain_angle:
                self.content = self._io.read_s4le()
            elif _on == self._root.Proptype.ole_object:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.atom_show_query:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.cross_reference_identifier:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.label_justification:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.curve_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.group_integral:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.unused4:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bottom_left:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.unused1:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.creation_program:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.ignore_warnings:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.print_trim_marks:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.obj_tlc_lane:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.height_pages:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.mac_pict:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.user_temporary_begin:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.mole_formula:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxFormula(io, self, self._root)
            elif _on == self._root.Proptype.bond_show_stereo:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.line_height:
                self.content = self._io.read_u2le()
            elif _on == self._root.Proptype.bounds_in_parent:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxRectangle(io, self, self._root)
            elif _on == self._root.Proptype.obj_object_definition:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.bracket_usage:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.object_tag_value:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxVaries(io, self, self._root)
            elif _on == self._root.Proptype.spectrum_data_point:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.cross_reference_container:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.bond_cip_stereochemistry:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCipStereoBond(io, self, self._root)
            elif _on == self._root.Proptype.obj_crossing_bond:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.obj_registry_number:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.template_pane_height:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxCoordinate(io, self, self._root)
            elif _on == self._root.Proptype.obj_reaction_step:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.side:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.node_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.obj_page:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.obj_graphic:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.obj_reaction_scheme:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.tlc_origin_fraction:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.font_table:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxFontTable(io, self, self._root)
            elif _on == self._root.Proptype.node_element:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.tlc_rf:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.unused6:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)
            elif _on == self._root.Proptype.obj_node:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.obj_template_grid:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.obj_ole_client_item:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.tlc_show_origin:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.print_margins:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxRectangle(io, self, self._root)
            elif _on == self._root.Proptype.bracket_lip_size:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.bracket_sru_label:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxString(io, self, self._root)
            elif _on == self._root.Proptype.obj_border:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObject(io, self, self._root)
            elif _on == self._root.Proptype.x2d_position:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.atom_isotope:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.constraint_max:
                self.content = self._io.read_f8le()
            elif _on == self._root.Proptype.mole_absolute:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBoolean(io, self, self._root)
            elif _on == self._root.Proptype.fix_inplace_gap:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxPoint2d(io, self, self._root)
            elif _on == self._root.Proptype.atom_restrict_rxn_change:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.bracketed_objects:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxObjectIdArray(io, self, self._root)
            elif _on == self._root.Proptype.window_is_zoomed:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxBooleanImplied(io, self, self._root)
            elif _on == self._root.Proptype.rectangle_type:
                self.content = self._io.read_s2le()
            elif _on == self._root.Proptype.atom_charge:
                self.content = self._io.read_s1()
            elif _on == self._root.Proptype.template_num_columns:
                self.content = self._io.read_s2le()
            else:
                self._raw_content = self._io.read_bytes(self.len)
                io = KaitaiStream(BytesIO(self._raw_content))
                self.content = self._root.CdxUnknown(io, self, self._root)


    class CdxElementList(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_elements = self._io.read_s2le()
            self.elements = [None] * ((-(self.num_elements) if self.num_elements < 0 else self.num_elements))
            for i in range((-(self.num_elements) if self.num_elements < 0 else self.num_elements)):
                self.elements[i] = self._io.read_s2le()


        @property
        def negation(self):
            if hasattr(self, '_m_negation'):
                return self._m_negation if hasattr(self, '_m_negation') else None

            self._m_negation = self.num_elements < 0
            return self._m_negation if hasattr(self, '_m_negation') else None


    class CdxUnknown(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes_full()


    class CdxCurvePoints(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_points = self._io.read_u2le()
            self.points = [None] * (self.num_points)
            for i in range(self.num_points):
                self.points[i] = self._root.CdxPoint2d(self._io, self, self._root)



    class CdxPoint2d(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.yx = [None] * (2)
            for i in range(2):
                self.yx[i] = self._io.read_s4le()



    class CdxVaries(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._root.CdxUnknown(self._io, self, self._root)


    class CdxColorTable(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_colors = self._io.read_u2le()
            self.colors = [None] * (self.num_colors)
            for i in range(self.num_colors):
                self.colors[i] = self._root.CdxColorTable.Color(self._io, self, self._root)


        class Color(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.rgb = [None] * (3)
                for i in range(3):
                    self.rgb[i] = self._io.read_u2le()





