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

controls = [ 
  effects.blank, intro, verse_a, verse_b, buildup_a, buildup_b, 
  drop_a, drop_b, honk, 
  drop_a, drop_b, drop_c, honk, 
  drop_c, honk, 
  outro_a, outro_b, end
]
