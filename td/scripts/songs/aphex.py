intro = {'bg_column': 1, 'pulse_clear': True}
verse_a = {'bg_column': 2, 'resync': True}
verse_b = {'bg_column': 3, 'pulse_clear': True}
verse_c = {'bg_column': 4, 'pulse_clear': True}
verse_d = {'bg_column': 5, 'pulse_clear': True}
pre_a = {'bg_column': 6, 'pulse_clear': True}
pre_b = {'bg_column': 7, 'pulse_clear': True}
chorus_a = {'bg_column': 8, 'pulse_clear': True}
chorus_b = {'bg_column': 9, 'pulse_clear': True}
chorus_c = {'bg_column': 10, 'pulse_clear': True}
chorus_d = {'bg_column': 11, 'pulse_clear': True}
chill_a = {'bg_column': 12, 'resync': True,
         'pulse_clear': True}
chill_b = {'bg_column': 13, 'pulse_clear': True}
chill_c = {'bg_column': 14, 'pulse_clear': True}
chill_d = {'bg_column': 15, 'pulse_clear': True}
fade_out = {'bg_column': 16, 'pulse_clear': True}
end = {'bg_column': 17, 'pulse_clear': True}

controls = [
    None, intro,
    verse_a, verse_b,
    pre_a,
    verse_c, verse_d, 
    verse_c, verse_d, 
    chorus_a, chorus_b, 
    chorus_c, chorus_d,
    verse_c, pre_b, verse_d, pre_a,
    chill_a, chill_b, chill_c,
    chill_a, chill_c, 
    chill_b, chill_c, chill_a, 
    intro,
    chill_a,
    pre_b, pre_a, pre_b,
    fade_out,
    end
]
