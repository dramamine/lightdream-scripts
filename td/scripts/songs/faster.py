#from functools import partial
from resolume_commands import pulse_clear_init
# import sequences
import effects

intro = {**effects.heatinvert, 'bg_column': 1, 'init': pulse_clear_init}
verse_a = {**effects.heatinvert, 'bg_column': 2, }
verse_b = {**effects.heatinvert, 'bg_column': 3, 'init': pulse_clear_init}
buildup_a = {**effects.heatinvert, 'bg_column': 4, 'init': pulse_clear_init}
buildup_b = {**effects.heatinvert, 'bg_column': 5, 'init': pulse_clear_init}
drop_a = {**effects.heatinvert, 'bg_column': 6, 'init': pulse_clear_init}
drop_b = {**effects.heatinvert, 'bg_column': 7, 'init': pulse_clear_init}
honk = {**effects.heatinvert, 'bg_column': 8, 'init': pulse_clear_init}
drop_c = {**effects.heatinvert, 'bg_column': 9, 'init': pulse_clear_init}
outro_a = {**effects.heatinvert, 'bg_column': 10, 'init': pulse_clear_init}
outro_b = {**effects.heatinvert, 'bg_column': 11, }
end = {**effects.heatinvert, 'bg_column': 12, 'init': pulse_clear_init}

controls = {
  0: effects.blank,
  1: intro,
  2: verse_a,
  3: verse_b,
  4: buildup_a,
  5: buildup_b,
  6: drop_a,
  7: drop_b,
  8: honk,
  9: drop_a,
  10: drop_b,
  11: drop_c,
  12: honk,
  13: drop_c,
  14: honk,
  15: outro_a,
  16: outro_b,
  17: end
}
