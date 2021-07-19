intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True, 'transition_time': 0.2}
verse_a = {'bg_column': 2, 'pulse_clear': True }
verse_b = {'bg_column': 3, 'pulse_clear': True }
verse_c = {'bg_column': 4, 'pulse_clear': True }
verse_d = {'bg_column': 5, 'pulse_clear': True }
guitars_a = {'bg_column': 6, 'pulse_clear': True, 'transition_time': 0.2 }
guitars_b = {'bg_column': 7, 'pulse_clear': True, 'transition_time': 0.0 }
guitars_c = {'bg_column': 8, 'pulse_clear': True, 'transition_time': 0.2 }
guitars_d = {'bg_column': 9, 'pulse_clear': True }
heightened_a = {'bg_column': 10, 'pulse_clear': True }
heightened_b = {'bg_column': 11, 'pulse_clear': True }
ooo_a = {'bg_column': 12, 'pulse_clear': True }
ooo_b = {'bg_column': 13, 'pulse_clear': True }
outro_jam = {'bg_column': 14, 'pulse_clear': True }
outro = {'bg_column': 15, 'pulse_clear': True }

end = {'bg_column': 16}

controls = [
  None,
  intro,
  verse_a, verse_b, verse_a,
  verse_c, verse_d, verse_a,
  guitars_a, guitars_b, guitars_a,
  heightened_a, ooo_a, guitars_a,
  guitars_b, guitars_c,
  heightened_a, ooo_a, guitars_c,
  guitars_d,
  heightened_b, ooo_b,
  outro_jam, outro, end
]

# before guitar c/d: slow fade
# turn down contra and fade effects and purp