intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
part_a = {'bg_column': 2, 'resync': True, 'pulse_clear': True}
part_b = {'bg_column': 3}
nice_part_a = {'bg_column': 4, 'resync': True, 'pulse_clear': True}
nice_part_b = {'bg_column': 5}
part_c = {'bg_column': 6, 'pulse_toggle_on_load': True}
part_c_minus = {'bg_column': 7, 'pulse_toggle_on_load': True}
part_d = {'bg_column': 8, 'pulse_toggle_on_load': True}
part_d_minus = {'bg_column': 9, 'pulse_toggle_on_load': True}
nice_part_b_plus = {'bg_column': 10, 'resync': True, 'pulse_clear': True}
top_a = {'bg_column': 11, 'pulse_toggle_on_load': True}
top_b = {'bg_column': 12, 'pulse_toggle_on_load': True}
top_c = {'bg_column': 13, 'pulse_toggle_on_load': True}
top_d = {'bg_column': 14, 'pulse_toggle_on_load': True}
end = {'bg_column': 15, 'pulse_clear': True}


controls = [
    None, intro, 
    part_a, part_b,
    nice_part_a, nice_part_b,
    part_c, part_c_minus,
    part_c, part_c_minus,
    part_d, part_d_minus,
    part_d, part_d_minus,
    nice_part_a, nice_part_b, nice_part_b_plus,
    top_a, top_b,
    top_c, top_d,
    top_a, top_b,
    part_c, part_c_minus,
    part_c, part_c_minus,
    part_d, part_d_minus, 
    part_a,
    end
]
