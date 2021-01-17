import effects

intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
verse_a = {'bg_column': 2, }
verse_b = {'bg_column': 3, 'pulse_clear': True}
buildup_a = {'bg_column': 4, 'pulse_clear': True}
buildup_b = {'bg_column': 5, 'pulse_clear': True}
drop_a = {'bg_column': 6, 'pulse_clear': True}
drop_b = {'bg_column': 7, 'pulse_clear': True}
honk = {'bg_column': 8, 'pulse_clear': True}
drop_c = {'bg_column': 9, 'pulse_clear': True}
outro_a = {'bg_column': 10, 'pulse_clear': True}
outro_b = {'bg_column': 11, }
end = {'bg_column': 12, 'pulse_clear': True}

controls = [ 
  effects.blank, intro, verse_a, verse_b, buildup_a, buildup_b, 
  drop_a, drop_b, honk, 
  drop_a, drop_b, drop_c, honk, 
  drop_c, honk, 
  outro_a, outro_b, end
]
