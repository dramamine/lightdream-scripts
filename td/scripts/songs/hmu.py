dubs_a = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
dubs_b = {'bg_column': 2}
dubs_c = {'bg_column': 3}
verse_a = {'bg_column': 4, 'pulse_clear': True}
verse_b = {'bg_column': 5}
verse_c = {'bg_column': 6}
verse_d = {'bg_column': 7}
chipsbag = {'bg_column': 8, 'pulse_toggle_on_load': True}
bangs = {'bg_column': 9, 'pulse_toggle_on_load': True}
outro = {'bg_column': 10}

controls = [
  None,
  dubs_a,
  verse_a, chipsbag, verse_a,
  verse_b, bangs, verse_b,
  verse_a, verse_b,

  verse_a, chipsbag, verse_a,
  verse_b, bangs, verse_b,
  verse_a, chipsbag, verse_a,
  verse_b,

  verse_c, verse_d,
  verse_c, verse_d,

  dubs_a, dubs_b, dubs_c, dubs_b,
  verse_a, chipsbag, verse_a,
  verse_b, bangs, verse_b,
  verse_a, verse_b,

  verse_a, chipsbag, verse_a,
  verse_b, bangs, verse_b,
  verse_a, chipsbag, verse_a,
  verse_b,

  outro
]

# chips n bangs need to be shorter: start right when weird sounds start
# dubs b->c transition: make it smooth