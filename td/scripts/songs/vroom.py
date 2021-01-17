intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
buildup_a = {'bg_column': 2}
buildup_b = {'bg_column': 3}
combo_a = {'bg_column': 4}
throwdown = {'bg_column': 5}
verse_a = {'bg_column': 6, 'pulse_clear': True}
verse_b = {'bg_column': 7}
verse_c = {'bg_column': 8}
chorus_a = {'bg_column': 9}
chorus_b = {'bg_column': 10}
chorus_c = {'bg_column': 11}
vroom_a = {'bg_column': 12}
vroom_b = {'bg_column': 13}
end = {'bg_column': 14, 'pulse_clear': True}


controls = [
    None, intro, 
    
    buildup_a, buildup_b, throwdown,
    verse_a, verse_b, verse_c,
    chorus_a, chorus_b, chorus_a,
    vroom_a, vroom_b,

    buildup_a, buildup_b, combo_a,
    chorus_a, chorus_b, chorus_a,
    vroom_a, vroom_b,
    end
]
