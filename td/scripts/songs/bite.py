intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
build_a = {'bg_column': 2}
build_b = {'bg_column': 3}
noodles = {'bg_column': 4}
straight_a = {'bg_column': 5}
straight_b = {'bg_column': 6}
quiet_a = {'bg_column': 7}
quiet_b = {'bg_column': 8}
verse_a = {'bg_column': 9, 'pulse_clear': True}
verse_b = {'bg_column': 10, 'resync': True}
verse_c = {'bg_column': 11}
verse_d = {'bg_column': 12}
verse_e = {'bg_column': 13}
buildup = {'bg_column': 14}
chill_a = {'bg_column': 15}
chill_b = {'bg_column': 16, 'transition_time': 0.25}
shrieky_i = {'bg_column': 17, 'transition_time': 0.0}
fverse_a = {'bg_column': 18}
fverse_b = {'bg_column': 19}
fverse_c = {'bg_column': 20}
fverse_cprime = {'bg_column': 21}
riff = {'bg_column': 22}
end = {'bg_column': 23}

controls = [
    None, intro, build_a,
    noodles, straight_a, straight_b, quiet_a,
    verse_a, verse_b, verse_c, verse_b,
    verse_a, verse_b, verse_c, verse_d,
    verse_e, quiet_a, verse_e, quiet_b,
    verse_e, quiet_a, verse_e, buildup,
    chill_a, chill_b,
    shrieky_i,
    fverse_a, fverse_b, fverse_c,
    fverse_a, fverse_b, fverse_c,
    fverse_a, fverse_b, fverse_c,
    fverse_a, fverse_b, fverse_cprime,
    verse_a, verse_b, verse_c, 
    chill_a,
    verse_a, noodles, verse_b, riff,
    verse_e, noodles, end
]
