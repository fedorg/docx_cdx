meta:
  id: cdx
  file-extension: cdx
  endian: le
  ks-version: 0.8
  encoding: cp1251

seq:
  - id: header
    type: header
  - id: document
    type: document
    size-eos: true

enums:
  proptype:
    0x0000: end_object
    0x0001: creation_user_name
    0x0002: creation_date
    0x0003: creation_program
    0x0004: modification_user_name
    0x0005: modification_date
    0x0006: modification_program
    0x0007: unused1
    0x0008: name
    0x0009: comment
    0x000a: z_order
    0x000b: registry_number
    0x000c: registry_authority
    0x000d: unused2
    0x000e: represents_property
    0x000f: ignore_warnings
    0x0010: chemical_warning
    0x0011: visible
    0x0100: font_table
    0x0200: x2d_position
    0x0201: x3d_position
    0x0202: x2d_extent
    0x0203: x3d_extent
    0x0204: bounding_box
    0x0205: rotation_angle
    0x0206: bounds_in_parent
    0x0207: x3d_head
    0x0208: x3d_tail
    0x0209: top_left
    0x020a: top_right
    0x020b: bottom_right
    0x020c: bottom_left
    0x0300: color_table
    0x0301: foreground_color
    0x0302: background_color
    0x0400: node_type
    0x0401: node_label_display
    0x0402: node_element
    0x0403: atom_element_list
    0x0404: atom_formula
    0x0420: atom_isotope
    0x0421: atom_charge
    0x0422: atom_radical
    0x0423: atom_restrict_free_sites
    0x0424: atom_restrict_implicit_hydrogens
    0x0425: atom_restrict_ring_bond_count
    0x0426: atom_restrict_unsaturated_bonds
    0x0427: atom_restrict_rxn_change
    0x0428: atom_restrict_rxn_stereo
    0x0429: atom_abnormal_valence
    0x042a: unused3
    0x042b: atom_num_hydrogens
    0x042c: unused4
    0x042d: unused5
    0x042e: atom_h_dot
    0x042f: atom_h_dash
    0x0430: atom_geometry
    0x0431: atom_bond_ordering
    0x0432: node_attachments
    0x0433: atom_generic_nickname
    0x0434: atom_alt_group_id
    0x0435: atom_restrict_substituents_up_to
    0x0436: atom_restrict_substituents_exactly
    0x0437: atom_cip_stereochemistry
    0x0438: atom_translation
    0x0439: atom_atom_number
    0x043a: atom_show_query
    0x043b: atom_show_stereo
    0x043c: atom_show_atom_number
    0x043d: atom_link_count_low
    0x043e: atom_link_count_high
    0x043f: atom_isotopic_abundance
    0x0440: atom_external_connection_type
    0x0500: mole_racemic
    0x0501: mole_absolute
    0x0502: mole_relative
    0x0503: mole_formula
    0x0504: mole_weight
    0x0505: frag_connection_order
    0x0600: bond_order
    0x0601: bond_display
    0x0602: bond_display2
    0x0603: bond_double_position
    0x0604: bond_begin
    0x0605: bond_end
    0x0606: bond_restrict_topology
    0x0607: bond_restrict_rxn_participation
    0x0608: bond_begin_attach
    0x0609: bond_end_attach
    0x060a: bond_cip_stereochemistry
    0x060b: bond_bond_ordering
    0x060c: bond_show_query
    0x060d: bond_show_stereo
    0x060e: bond_crossing_bonds
    0x060f: bond_show_rxn
    0x0700: text
    0x0701: justification
    0x0702: line_height
    0x0703: word_wrap_width
    0x0704: line_starts
    0x0705: label_alignment
    0x0706: label_line_height
    0x0707: caption_line_height
    0x0708: interpret_chemically
    0x0800: mac_print_info
    0x0801: win_print_info
    0x0802: print_margins
    0x0803: chain_angle
    0x0804: bond_spacing
    0x0805: bond_length
    0x0806: bold_width
    0x0807: line_width
    0x0808: margin_width
    0x0809: hash_spacing
    0x080a: label_style
    0x080b: caption_style
    0x080c: caption_justification
    0x080d: fractional_widths
    0x080e: magnification
    0x080f: width_pages
    0x0810: height_pages
    0x0811: drawing_space_type
    0x0812: width
    0x0813: height
    0x0814: page_overlap
    0x0815: header
    0x0816: header_position
    0x0817: footer
    0x0818: footer_position
    0x0819: print_trim_marks
    0x081a: label_style_font
    0x081b: caption_style_font
    0x081c: label_style_size
    0x081d: caption_style_size
    0x081e: label_style_face
    0x081f: caption_style_face
    0x0820: label_style_color
    0x0821: caption_style_color
    0x0822: bond_spacing_abs
    0x0823: label_justification
    0x0824: fix_inplace_extent
    0x0825: side
    0x0826: fix_inplace_gap
    0x0900: window_is_zoomed
    0x0901: window_position
    0x0902: window_size
    0x0a00: graphic_type
    0x0a01: line_type
    0x0a02: arrow_type
    0x0a03: rectangle_type
    0x0a04: oval_type
    0x0a05: orbital_type
    0x0a06: bracket_type
    0x0a07: symbol_type
    0x0a08: curve_type
    0x0a20: arrow_head_size
    0x0a21: arc_angular_size
    0x0a22: bracket_lip_size
    0x0a23: curve_points
    0x0a24: bracket_usage
    0x0a25: polymer_repeat_pattern
    0x0a26: polymer_flip_type
    0x0a27: bracketed_objects
    0x0a28: bracket_repeat_count
    0x0a29: bracket_component_order
    0x0a2a: bracket_sru_label
    0x0a2b: bracket_graphic_id
    0x0a2c: bracket_bond_id
    0x0a2d: bracket_inner_atom_id
    0x0a2e: curve_points3d
    0x0a60: picture_edition
    0x0a61: picture_edition_alias
    0x0a62: mac_pict
    0x0a63: windows_metafile
    0x0a64: ole_object
    0x0a65: enhanced_metafile
    0x0a80: spectrum_x_spacing
    0x0a81: spectrum_x_low
    0x0a82: spectrum_x_type
    0x0a83: spectrum_y_type
    0x0a84: spectrum_x_axis_label
    0x0a85: spectrum_y_axis_label
    0x0a86: spectrum_data_point
    0x0a87: spectrum_class
    0x0a88: spectrum_y_low
    0x0a89: spectrum_y_scale
    0x0aa0: tlc_origin_fraction
    0x0aa1: tlc_solvent_front_fraction
    0x0aa2: tlc_show_origin
    0x0aa3: tlc_show_solvent_front
    0x0aa4: tlc_show_borders
    0x0aa5: tlc_show_side_ticks
    0x0ab0: tlc_rf
    0x0ab1: tlc_tail
    0x0ab2: tlc_show_rf
    0x0b00: named_alternative_group_text_frame
    0x0b01: named_alternative_group_group_frame
    0x0b02: named_alternative_group_valence
    0x0b80: geometric_feature
    0x0b81: relation_value
    0x0b82: basis_objects
    0x0b83: constraint_type
    0x0b84: constraint_min
    0x0b85: constraint_max
    0x0b86: ignore_unconnected_atoms
    0x0b87: dihedral_is_chiral
    0x0b88: point_is_directed
    0x0c00: reaction_step_atom_map
    0x0c01: reaction_step_reactants
    0x0c02: reaction_step_products
    0x0c03: reaction_step_plusses
    0x0c04: reaction_step_arrows
    0x0c05: reaction_step_objects_above_arrow
    0x0c06: reaction_step_objects_below_arrow
    0x0c07: reaction_step_atom_map_manual
    0x0c08: reaction_step_atom_map_auto
    0x0d00: object_tag_type
    0x0d01: unused6
    0x0d02: unused7
    0x0d03: object_tag_tracking
    0x0d04: object_tag_persistent
    0x0d05: object_tag_value
    0x0d06: positioning
    0x0d07: positioning_angle
    0x0d08: positioning_offset
    0x0e00: sequence_identifier
    0x0f00: cross_reference_container
    0x0f01: cross_reference_document
    0x0f02: cross_reference_identifier
    0x0f03: cross_reference_sequence
    0x1000: template_pane_height
    0x1001: template_num_rows
    0x1002: template_num_columns
    0x1100: group_integral
    0x1ff0: splitter_positions
    0x1ff1: page_definition
    0x4000: user_temporary_begin
    0x4400: user_temporary_end
    0x8000: obj_document
    0x8001: obj_page
    0x8002: obj_group
    0x8003: obj_fragment
    0x8004: obj_node
    0x8005: obj_bond
    0x8006: obj_text
    0x8007: obj_graphic
    0x8008: obj_curve
    0x8009: obj_embedded_object
    0x800a: obj_named_alternative_group
    0x800b: obj_template_grid
    0x800c: obj_registry_number
    0x800d: obj_reaction_scheme
    0x800e: obj_reaction_step
    0x800f: obj_object_definition
    0x8010: obj_spectrum
    0x8011: obj_object_tag
    0x8012: obj_ole_client_item
    0x8013: obj_sequence
    0x8014: obj_cross_reference
    0x8015: obj_splitter
    0x8016: obj_table
    0x8017: obj_bracketed_group
    0x8018: obj_bracket_attachment
    0x8019: obj_crossing_bond
    0x8020: obj_border
    0x8021: obj_geometry
    0x8022: obj_constraint
    0x8023: obj_tlc_plate
    0x8024: obj_tlc_lane
    0x8025: obj_tlc_spot
    0x8fff: obj_unknown_object

types:

  cdx_unknown:
    -webide-representation: '{data}'
    seq:
      - id: data
        size-eos: true
  
  cdx_font_style:
    # types:
    #   font_flags:
    #     enums:
    #       font_script:
    #         0: plain
    #         1: sub
    #         2: super
    #         3: formula
    #     seq:
    #       - id: bold
    #         type: b1
    #       - id: italic
    #         type: b1
    #       - id: underline
    #         type: b1
    #       - id: outline
    #         type: b1
    #       - id: shadow
    #         type: b1
    #       - id: font_script
    #         type: b2
    #         enum: font_script
    seq:
      - id: font_table_index
        type: u2
      - id: flags
        type: u2 #font_flags
      - id: size
        type: u2
      - id: color
        type: u2

  cdx_raw_string:
    seq:
      - id: value
        type: str
        size-eos: true

  cdx_string:
    -webide-representation: '{text}'
    types:
      stylerun:
        seq:
          - id: starts
            type: u2
          - id: style
            type: cdx_font_style
    seq:
      - id: num_styleruns
        type: u2
      - id: styleruns
        type: stylerun
        repeat: expr
        repeat-expr: num_styleruns
      - id: text
        type: str
        size-eos: true

  cdx_boolean:
    seq:
      - id: value
        type: s1

  cdx_coordinate:
    seq:
      - id: value
        type: s4

  cdx_point2d:
    seq:
      - id: yx
        type: s4
        repeat: expr
        repeat-expr: 2


  cdx_point3d:
    seq:
      - id: zyx
        type: s4
        repeat: expr
        repeat-expr: 3

  cdx_rectangle:
    seq:
      - id: tlbr
        type: s4
        repeat: expr
        repeat-expr: 4

  cdx_color_table:
    types:
      color:
        seq:
          - id: rgb
            type: u2
            repeat: expr
            repeat-expr: 3
    seq:
      - id: num_colors
        type: u2
      - id: colors
        type: color
        repeat: expr
        repeat-expr: num_colors

  cdx_curve_points:
    seq:
      - id: num_points
        type: u2
      - id: points
        type: cdx_point2d
        repeat: expr
        repeat-expr: num_points

  cdx_curve_points3d:
    seq:
      - id: num_points
        type: u2
      - id: points
        type: cdx_point3d
        repeat: expr
        repeat-expr: num_points

  cdx_element_list:
    seq:
      - id: num_elements
        type: s2
      - id: elements
        type: s2
        repeat: expr
        repeat-expr: (num_elements < 0 ? -num_elements : num_elements)
    instances:
      negation:
        value: (num_elements < 0)

  cdx_object_id:
    seq:
      - id: obj_id
        type: u4

  cdx_object_id_array:
    seq:
      - id: objs
        type: cdx_object_id
        repeat: eos

  cdx_object_id_array_with_counts:
    seq:
      - id: num_objs
        type: u2
      - id: objs
        type: cdx_object_id
        repeat: expr
        repeat-expr: num_objs

  cdx_represents_property:
    seq:
      - id: obj_id
        type: cdx_object_id
      - id: prop_tag
        type: u2


  cdx_font_table:
    types:
      stylerun:
        -webide-representation: '{font_name}'
        seq:
          - id: font_id
            type: u2
          - id: charset
            type: u2
          - id: font_name_length
            type: u2
          - id: font_name
            type: str
            size: font_name_length
    seq:
      - id: platform
        type: u2
      - id: num_styleruns
        type: u2
      - id: styleruns
        type: stylerun
        repeat: expr
        repeat-expr: num_styleruns

  cdx_date:
    seq:
      - id: year
        type: s2
      - id: month
        type: s2
      - id: day
        type: s2
      - id: hour
        type: s2
      - id: minute
        type: s2
      - id: second
        type: s2
      - id: milliseconds
        type: s2

  int16_list_with_counts:
    seq:
      - id: num_values
        type: u2
      - id: values
        type: u2
        repeat: expr
        repeat-expr: num_values

  cdx_object:
    seq:
      - id: value
        type: cdx_unknown

  cdx_formula:
    seq:
      - id: value
        type: cdx_unknown

  cdx_boolean_implied:
    seq:
      - id: content
        size: _parent.len
    instances:
      value:
        value: _parent.len > 0

  cdx_varies:
    seq:
      - id: value
        type: cdx_unknown


  cdx_cip_stereo_bond:
    enums:
      stereo:
        0:
          id: u
          doc: Undetermined
        1:
          id: n
          doc: Determined to be symmetric
        2:
          id: e
          doc: Asymmetric: (E)
        3:
          id: z
          doc: Asymmetric: (Z)
    seq:
      - id: stereo
        type: s1
        enum: stereo

  cdx_cip_stereo_atom:
    enums:
      stereo:
        0:
          id: u
          doc: Undetermined
        1:
          id: n
          doc: Determined to be symmetric
        2:
          id: r
          doc: Asymmetric: (R)
        3:
          id: s
          doc: Asymmetric: (S)
        4:
          id: pr
          doc: Pseudoasymmetric: (r)
        5:
          id: ps
          doc: Pseudoasymmetric: (s)
        6:
          id: unspecified
          doc: The node is not symmetric (might be asymmetric or pseudoasymmetric), but lacks a hash/wedge so absolute configuration cannot be determined
    seq:
      - id: stereo
        type: s1
        enum: stereo


  header:
    seq:
      - id: magic
        contents: [ 0x56, 0x6a, 0x43, 0x44,
                    0x30, 0x31, 0x30, 0x30,
                    0x04, 0x03, 0x02, 0x01,
                    0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00 ]

  prop:
    -webide-representation: '{content}'
    seq:
      - id: len
        type: u2
      - id: content
        size: len
        type:
          switch-on: _parent.tag
          cases:
            'proptype::end_object': s2
            'proptype::creation_user_name': cdx_string
            'proptype::creation_date': cdx_date
            'proptype::creation_program': cdx_string
            'proptype::modification_user_name': cdx_string
            'proptype::modification_date': cdx_date
            'proptype::modification_program': cdx_string
            'proptype::unused1': cdx_unknown
            'proptype::name': cdx_raw_string
            'proptype::comment': cdx_string
            'proptype::z_order': s2
            'proptype::registry_number': cdx_string
            'proptype::registry_authority': cdx_string
            'proptype::unused2': cdx_unknown
            'proptype::represents_property': cdx_represents_property
            'proptype::ignore_warnings': cdx_boolean_implied
            'proptype::chemical_warning': cdx_string
            'proptype::visible': cdx_boolean
            # fonts.
            'proptype::font_table': cdx_font_table
            # coordinates.
            'proptype::x2d_position': cdx_point2d
            'proptype::x3d_position': cdx_point3d
            'proptype::x2d_extent': cdx_point2d
            'proptype::x3d_extent': cdx_point3d
            'proptype::bounding_box': cdx_rectangle
            'proptype::rotation_angle': s4
            'proptype::bounds_in_parent': cdx_rectangle
            'proptype::x3d_head': cdx_point3d
            'proptype::x3d_tail': cdx_point3d
            'proptype::top_left': cdx_point2d
            'proptype::top_right': cdx_point2d
            'proptype::bottom_right': cdx_point2d
            'proptype::bottom_left': cdx_point2d
            # colors.
            'proptype::color_table': cdx_color_table
            'proptype::foreground_color': u2
            'proptype::background_color': s2
            # atom properties.
            'proptype::node_type': s2
            'proptype::node_label_display': s1
            'proptype::node_element': s2
            'proptype::atom_element_list': cdx_element_list
            'proptype::atom_formula': cdx_formula
            'proptype::atom_isotope': s2
            'proptype::atom_charge': s1
            'proptype::atom_radical': u1
            'proptype::atom_restrict_free_sites': u1
            'proptype::atom_restrict_implicit_hydrogens': cdx_boolean_implied
            'proptype::atom_restrict_ring_bond_count': s1
            'proptype::atom_restrict_unsaturated_bonds': s1
            'proptype::atom_restrict_rxn_change': cdx_boolean_implied
            'proptype::atom_restrict_rxn_stereo': s1
            'proptype::atom_abnormal_valence': cdx_boolean_implied
            'proptype::unused3': s2
            'proptype::atom_num_hydrogens': u2
            'proptype::unused4': s2
            'proptype::unused5': s2
            'proptype::atom_h_dot': cdx_boolean_implied
            'proptype::atom_h_dash': cdx_boolean_implied
            'proptype::atom_geometry': s1
            'proptype::atom_bond_ordering': cdx_object_id_array
            'proptype::node_attachments': cdx_object_id_array_with_counts
            'proptype::atom_generic_nickname': cdx_string
            'proptype::atom_alt_group_id': cdx_object_id
            'proptype::atom_restrict_substituents_up_to': u1
            'proptype::atom_restrict_substituents_exactly': u1
            'proptype::atom_cip_stereochemistry': cdx_cip_stereo_atom
            'proptype::atom_translation': s1
            'proptype::atom_atom_number': cdx_string
            'proptype::atom_show_query': cdx_boolean
            'proptype::atom_show_stereo': cdx_boolean
            'proptype::atom_show_atom_number': cdx_boolean
            'proptype::atom_link_count_low': s2
            'proptype::atom_link_count_high': s2
            'proptype::atom_isotopic_abundance': s1
            'proptype::atom_external_connection_type': s1
            # molecule properties.
            'proptype::mole_racemic': cdx_boolean
            'proptype::mole_absolute': cdx_boolean
            'proptype::mole_relative': cdx_boolean
            'proptype::mole_formula': cdx_formula
            'proptype::mole_weight': f8
            'proptype::frag_connection_order': cdx_object_id_array
            # bond properties.
            'proptype::bond_order': s2
            'proptype::bond_display': s2
            'proptype::bond_display2': s2
            'proptype::bond_double_position': s2
            'proptype::bond_begin': cdx_object_id
            'proptype::bond_end': cdx_object_id
            'proptype::bond_restrict_topology': s1
            'proptype::bond_restrict_rxn_participation': s1
            'proptype::bond_begin_attach': u1
            'proptype::bond_end_attach': u1
            'proptype::bond_cip_stereochemistry': cdx_cip_stereo_bond
            'proptype::bond_bond_ordering': cdx_object_id_array
            'proptype::bond_show_query': cdx_boolean
            'proptype::bond_show_stereo': cdx_boolean
            'proptype::bond_crossing_bonds': cdx_object_id_array
            'proptype::bond_show_rxn': cdx_boolean
            # text properties.
            'proptype::text': cdx_string
            'proptype::justification': s1
            'proptype::line_height': u2
            'proptype::word_wrap_width': s2
            'proptype::line_starts': int16_list_with_counts
            'proptype::label_alignment': s1
            'proptype::label_line_height': s2
            'proptype::caption_line_height': s2
            'proptype::interpret_chemically': cdx_boolean_implied
            # document properties.
            'proptype::mac_print_info': cdx_unknown
            'proptype::win_print_info': cdx_unknown
            'proptype::print_margins': cdx_rectangle
            'proptype::chain_angle': s4
            'proptype::bond_spacing': s2
            'proptype::bond_length': cdx_coordinate
            'proptype::bold_width': cdx_coordinate
            'proptype::line_width': cdx_coordinate
            'proptype::margin_width': cdx_coordinate
            'proptype::hash_spacing': cdx_coordinate
            'proptype::label_style': cdx_font_style
            'proptype::caption_style': cdx_font_style
            'proptype::caption_justification': s1
            'proptype::fractional_widths': cdx_boolean_implied
            'proptype::magnification': s2
            'proptype::width_pages': s2
            'proptype::height_pages': s2
            'proptype::drawing_space_type': s1
            'proptype::width': cdx_coordinate
            'proptype::height': cdx_coordinate
            'proptype::page_overlap': cdx_coordinate
            'proptype::header': cdx_string
            'proptype::header_position': cdx_coordinate
            'proptype::footer': cdx_string
            'proptype::footer_position': cdx_coordinate
            'proptype::print_trim_marks': cdx_boolean_implied
            'proptype::label_style_font': s2
            'proptype::caption_style_font': s2
            'proptype::label_style_size': s2
            'proptype::caption_style_size': s2
            'proptype::label_style_face': s2
            'proptype::caption_style_face': s2
            'proptype::label_style_color': s2
            'proptype::caption_style_color': s2
            'proptype::bond_spacing_abs': cdx_coordinate
            'proptype::label_justification': s1
            'proptype::fix_inplace_extent': cdx_point2d
            'proptype::side': s2
            'proptype::fix_inplace_gap': cdx_point2d
            # window properties.
            'proptype::window_is_zoomed': cdx_boolean_implied
            'proptype::window_position': cdx_point2d
            'proptype::window_size': cdx_point2d
            
            # graphic object properties.
            'proptype::graphic_type': s2
            'proptype::line_type': s2
            'proptype::arrow_type': s2
            'proptype::rectangle_type': s2
            'proptype::oval_type': s2
            'proptype::orbital_type': s2
            'proptype::bracket_type': s2
            'proptype::symbol_type': s2
            'proptype::curve_type': s2
            'proptype::arrow_head_size': s2
            'proptype::arc_angular_size': s2
            'proptype::bracket_lip_size': s2
            'proptype::curve_points': cdx_curve_points
            'proptype::bracket_usage': s1
            'proptype::polymer_repeat_pattern': s1
            'proptype::polymer_flip_type': s1
            'proptype::bracketed_objects': cdx_object_id_array
            'proptype::bracket_repeat_count': s2
            'proptype::bracket_component_order': s2
            'proptype::bracket_sru_label': cdx_string
            'proptype::bracket_graphic_id': cdx_object_id
            'proptype::bracket_bond_id': cdx_object_id
            'proptype::bracket_inner_atom_id': cdx_object_id
            'proptype::curve_points3d': cdx_curve_points3d
            # embedded pictures.
            'proptype::picture_edition': cdx_unknown
            'proptype::picture_edition_alias': cdx_unknown
            'proptype::mac_pict': cdx_unknown
            'proptype::windows_metafile': cdx_unknown
            'proptype::ole_object': cdx_unknown
            'proptype::enhanced_metafile': cdx_unknown
            # spectrum properties
            'proptype::spectrum_x_spacing': f8
            'proptype::spectrum_x_low': f8
            'proptype::spectrum_x_type': s2
            'proptype::spectrum_y_type': s2
            'proptype::spectrum_x_axis_label': cdx_string
            'proptype::spectrum_y_axis_label': cdx_string
            'proptype::spectrum_data_point': f8
            'proptype::spectrum_class': s2
            'proptype::spectrum_y_low': f8
            'proptype::spectrum_y_scale': f8
            # tlc properties
            'proptype::tlc_origin_fraction': f8
            'proptype::tlc_solvent_front_fraction': f8
            'proptype::tlc_show_origin': cdx_boolean
            'proptype::tlc_show_solvent_front': cdx_boolean
            'proptype::tlc_show_borders': cdx_boolean
            'proptype::tlc_show_side_ticks': cdx_boolean
            'proptype::tlc_rf': f8
            'proptype::tlc_tail': cdx_coordinate
            'proptype::tlc_show_rf': cdx_boolean
            # alternate group properties
            'proptype::named_alternative_group_text_frame': cdx_rectangle
            'proptype::named_alternative_group_group_frame': cdx_rectangle
            'proptype::named_alternative_group_valence': s2
            # geometry and constraint properties
            'proptype::geometric_feature': s1
            'proptype::relation_value': s1
            'proptype::basis_objects': cdx_object_id_array
            'proptype::constraint_type': s1
            'proptype::constraint_min': f8
            'proptype::constraint_max': f8
            'proptype::ignore_unconnected_atoms': cdx_boolean_implied
            'proptype::dihedral_is_chiral': cdx_boolean_implied
            'proptype::point_is_directed': cdx_boolean_implied
            # reaction properties
            'proptype::reaction_step_atom_map': cdx_object_id_array
            'proptype::reaction_step_reactants': cdx_object_id_array
            'proptype::reaction_step_products': cdx_object_id_array
            'proptype::reaction_step_plusses': cdx_object_id_array
            'proptype::reaction_step_arrows': cdx_object_id_array
            'proptype::reaction_step_objects_above_arrow': cdx_object_id_array
            'proptype::reaction_step_objects_below_arrow': cdx_object_id_array
            'proptype::reaction_step_atom_map_manual': cdx_object_id_array
            'proptype::reaction_step_atom_map_auto': cdx_object_id_array
            # cdobject_tag properties
            'proptype::object_tag_type': s2
            'proptype::unused6': cdx_unknown
            'proptype::unused7': cdx_unknown
            'proptype::object_tag_tracking': cdx_boolean
            'proptype::object_tag_persistent': cdx_boolean
            'proptype::object_tag_value': cdx_varies
            'proptype::positioning': s1
            'proptype::positioning_angle': s4
            'proptype::positioning_offset': cdx_point2d
            # cdsequence properties
            'proptype::sequence_identifier': cdx_string
            # cdcross_reference properties
            'proptype::cross_reference_container': cdx_string
            'proptype::cross_reference_document': cdx_string
            'proptype::cross_reference_identifier': cdx_string
            'proptype::cross_reference_sequence': cdx_string
            # miscellaneous properties.
            'proptype::template_pane_height': cdx_coordinate
            'proptype::template_num_rows': s2
            'proptype::template_num_columns': s2
            'proptype::group_integral': cdx_boolean
            'proptype::splitter_positions': cdx_object_id_array
            'proptype::page_definition': cdx_object_id_array
            # user defined properties
            # first 1024 tags are reserved for temporary tags used only during the runtime.
            'proptype::user_temporary_begin': cdx_unknown
            'proptype::user_temporary_end': cdx_unknown
            # objects.
            'proptype::obj_document': cdx_object
            'proptype::obj_page': cdx_object
            'proptype::obj_group': cdx_object
            'proptype::obj_fragment': cdx_object
            'proptype::obj_node': cdx_object
            'proptype::obj_bond': cdx_object
            'proptype::obj_text': cdx_object
            'proptype::obj_graphic': cdx_object
            'proptype::obj_curve': cdx_object
            'proptype::obj_embedded_object': cdx_object
            'proptype::obj_named_alternative_group': cdx_object
            'proptype::obj_template_grid': cdx_object
            'proptype::obj_registry_number': cdx_object
            'proptype::obj_reaction_scheme': cdx_object
            'proptype::obj_reaction_step': cdx_object
            'proptype::obj_object_definition': cdx_object
            'proptype::obj_spectrum': cdx_object
            'proptype::obj_object_tag': cdx_object
            'proptype::obj_ole_client_item': cdx_object
            'proptype::obj_sequence': cdx_object
            'proptype::obj_cross_reference': cdx_object
            'proptype::obj_splitter': cdx_object
            'proptype::obj_table': cdx_object
            'proptype::obj_bracketed_group': cdx_object
            'proptype::obj_bracket_attachment': cdx_object
            'proptype::obj_crossing_bond': cdx_object
            'proptype::obj_border': cdx_object
            'proptype::obj_geometry': cdx_object
            'proptype::obj_constraint': cdx_object
            'proptype::obj_tlc_plate': cdx_object
            'proptype::obj_tlc_lane': cdx_object
            'proptype::obj_tlc_spot': cdx_object
            
            'proptype::obj_unknown_object': cdx_object
            _: cdx_unknown
  
  entity:
    -webide-representation: '{tag}: {prop}{obj.objId}'
    seq:
      - id: tag
        type: u2
        enum: proptype
      - id: prop
        type: prop
        if: (tag.to_i < 0x8000) and (tag != proptype::end_object)
      - id: obj
        type: obj
        if: (tag.to_i >= 0x8000) and (tag != proptype::end_object)

  obj:
    seq:
      - id: obj_id
        type: u4
      - id: content
        type: entity
        repeat: until
        repeat-until: _.tag == proptype::end_object
  
  document:
    seq:
      - id: content
        type: entity
        repeat: eos



