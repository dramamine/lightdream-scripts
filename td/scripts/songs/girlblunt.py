from resolume_commands import pulse_clear_init
import effects

intro = {**effects.clear, 'bg_column': 1, 'init': pulse_clear_init}
chorus_a = {**effects.blank, 'bg_column': 2}
chorus_b = {**effects.blank, 'bg_column': 3}
verse_a = {**effects.blank, 'bg_column': 4}
verse_b = {**effects.blank, 'bg_column': 5}
verse_c = {**effects.blank, 'bg_column': 6}
verse_d = {**effects.blank, 'bg_column': 7}
dropout = {**effects.blank, 'bg_column': 8}
chorus_c = {**effects.blank, 'bg_column': 9}
chorus_d = {**effects.blank, 'bg_column': 10}
chorus_e = {**effects.blank, 'bg_column': 11}
chorus_f = {**effects.blank, 'bg_column': 12}
outro = {**effects.blank, 'bg_column': 13}
end = {**effects.blank, 'bg_column': 14}

controls = {
  0: effects.blank,
  1: intro,
  2: chorus_a,
  3: chorus_b,
  4: chorus_a,
  5: chorus_b,
  6: verse_a,
  7: verse_b,
  8: chorus_a,
  9: chorus_b,
  10: chorus_a,
  11: chorus_b,
  12: verse_c,
  13: verse_d,
  14: dropout,
  15: verse_c,
  16: verse_d,
  17: chorus_c,
  18: chorus_d,  
  19: chorus_e,
  20: chorus_f,
  21: outro,
  22: end
}

# intro
# chorus a 
# chorus b 
# chorus a 
# chorus b
# verse a 
# verse b
# chorus a
# chorus b
# chorus a
# chorus b
# verse c
# verse d
# dropout
# verse c
# verse d
# chorus c
# chorus d
# chorus c
# chorus d
# outro
