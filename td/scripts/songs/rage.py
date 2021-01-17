intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
verse_a = {'bg_column': 2, 'pulse_clear': True}
verse_b = {'bg_column': 3, 'pulse_clear': True}
verse_c = {'bg_column': 4}
verse_d = {'bg_column': 5}
ragin = {'bg_column': 6}
dropout = {'bg_column': 7}
outro = {'bg_column': 8}
end = {'bg_column': 9}

controls = [
    None, intro,
    verse_a, verse_b, verse_a, verse_b,
    ragin, dropout,
    verse_a, verse_c, dropout, 
    verse_b, verse_d, dropout,
    verse_a, verse_c,
    ragin, dropout,
    verse_a, verse_c, verse_d,
    outro, end
]
