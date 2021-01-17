import effects

intro = {'bg_column': 1, 'resync': True}

verse_a = {'bg_column': 2, 'pulse_clear': True}
verse_b = {'bg_column': 3}
wonk = {'bg_column': 4}
quiet_a = {'bg_column': 5}
quiet_b = {'bg_column': 6}
quiet_c = {'bg_column': 7}
verseplus_a = {'bg_column': 8}
verseplus_b = {'bg_column': 9}
verseplus_c = {'bg_column': 10}
verseplus_d = {'bg_column': 11}
pre_end = {'bg_column': 12}
end = {'bg_column': 13, 'pulse_clear': True}

controls = [
  effects.clear,
  intro,
  verse_a, verse_b,
  verse_a, verse_b,
  wonk, 
  quiet_a,  # if im caught
  quiet_a,  # 1 measure
  quiet_b,  # 1 measure
  quiet_c,
  verseplus_a, verseplus_b,
  verseplus_a, verseplus_b,
  verseplus_c, verseplus_d,
  pre_end, end
]
