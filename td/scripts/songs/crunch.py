import effects

intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
intro_offbeats = { 'bg_column': 2, }
intro_basswonk = { 'bg_column': 3, }
verse_a = { 'bg_column': 4, }
verse_b = {'bg_column': 5, 'pulse_clear': True}
verse_c = {'bg_column': 6, 'pulse_clear': True}
verse_d = {'bg_column': 7, 'pulse_clear': True}
space_a = {'bg_column': 8, 'pulse_clear': True}
space_b = {'bg_column': 9, }
outro = {'bg_column': 10, }
end = {'bg_column': 11, 'pulse_clear': True}

controls = [ 
    effects.clear, intro, intro_offbeats, intro_basswonk, 
    verse_a, verse_b, intro_offbeats, intro_basswonk, 
    verse_c, verse_d, 
    space_a, space_b, outro, end
]
