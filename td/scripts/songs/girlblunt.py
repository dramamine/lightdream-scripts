import effects

intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
chorus_a = {'bg_column': 2}
chorus_b = {'bg_column': 3}
verse_a = {'bg_column': 4}
verse_b = {'bg_column': 5}
verse_c = {'bg_column': 6}
verse_d = {'bg_column': 7}
dropout = {'bg_column': 8}
chorus_c = {'bg_column': 9}
chorus_d = {'bg_column': 10}
chorus_e = {'bg_column': 11}
chorus_f = {'bg_column': 12}
outro = {'bg_column': 13}
end = {'bg_column': 14}

controls = [ 
  effects.blank, intro, 
  chorus_a, chorus_b, chorus_a, chorus_b, 
  verse_a, verse_b, 
  chorus_a, chorus_b, chorus_a, chorus_b, 
  verse_c, verse_d, dropout, 
  verse_c, verse_d, 
  chorus_c, chorus_d,   
  chorus_e, chorus_f, 
  outro, end
]
