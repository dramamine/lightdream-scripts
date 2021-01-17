import effects

intro_quiet_a = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
intro_quiet_b = {'bg_column': 2}
intro_drums = {'bg_column': 3}
verse_a = {'bg_column': 4}
verse_b = {'bg_column': 5, 'pulse_clear': True}
verse_hipass = {'bg_column': 6, 'pulse_clear': True}
verse_aprime = {'bg_column': 7, 'pulse_clear': True}
vocals_pre = {'bg_column': 8, 'pulse_clear': True}
vocals_a = {'bg_column': 9, 'pulse_clear': True}
vocals_b = {'bg_column': 10}
verse_singin = {'bg_column': 11}
vocals_dropout = {'bg_column': 12}
pv_a = {'bg_column': 13}
pv_b = {'bg_column': 14}
pv_hipass = {'bg_column': 15}
pv_aprime = {'bg_column': 16}
pv_dropoff = {'bg_column': 17}
end = {'bg_column': 18, 'pulse_clear': True}

controls = [ 
  effects.clear, 
  intro_quiet_a, intro_quiet_b, intro_quiet_a, intro_drums, 
  verse_a, verse_hipass, verse_b, verse_hipass, 
  vocals_pre, vocals_a,  vocals_b, vocals_a, verse_a, verse_aprime, 
  verse_b, verse_hipass,  
  verse_a, verse_aprime, verse_singin, vocals_dropout, 
  pv_a, pv_b, pv_hipass, pv_a, pv_aprime, pv_b, pv_dropoff, 
  intro_quiet_a, intro_quiet_b, end
]
