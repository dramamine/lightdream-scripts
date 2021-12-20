intro = {'bg_column': 1, 'resync': True}
verse_a = {'bg_column': 2, 'pulse_toggle_on_load': True,
           'transition_time_first_layer': 0.10}
verse_b = {'bg_column': 3, 'pulse_toggle_on_load': True}
verse_c = {'bg_column': 4, 'pulse_toggle_on_load': True}
verse_d = {'bg_column': 5, 'pulse_toggle_on_load': True}
verse_e = {'bg_column': 6, 'pulse_toggle_on_load': True}
quiet_a = {'bg_column': 7, 'pulse_clear': True}
quiet_b = {'bg_column': 8, 'pulse_clear': True}
quiet_c = {'bg_column': 9, 'pulse_clear': True}
buildup = {'bg_column': 10, 'pulse_toggle_on_load': True}
vox_a = {'bg_column': 11, 'pulse_toggle_on_load': True, 'transition_time_first_layer': 0.25}
vox_b = {'bg_column': 12, 'pulse_toggle_on_load': True}
vox_c = {'bg_column': 13, 'pulse_toggle_on_load': True}
vox_d = {'bg_column': 14, 'pulse_clear': True, 'transition_time_first_layer': 0.25}
vox_e = {'bg_column': 15, 'pulse_toggle_on_load': True}
vox_f = {'bg_column': 16, 'pulse_toggle_on_load': True}
dropout = {'bg_column': 17, 'resync': True, 'pulse_clear': True, 'transition_time_first_layer': 0}
end = {'bg_column': 18}

controls = [
    None, intro,
    verse_a, verse_b, verse_a, quiet_a, quiet_b, buildup,
    verse_c, verse_d, verse_c, verse_d, verse_e, dropout,
    vox_a, vox_b, vox_c, vox_a, vox_b, vox_c,
    vox_a, vox_b, vox_c, dropout,
    vox_d, vox_e, vox_f, vox_d, vox_e, vox_f,
    quiet_a, quiet_b, quiet_c, 
    end
]
