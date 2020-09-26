# copied from some other file... can/should probably get rid of everything
from resolume_commands import pulse_clear_init
# import sequences
import effects

intro = {**effects.heatinvert, 'bg_column': 1, 'init': pulse_clear_init}
verse_a = {**effects.heatinvert, 'bg_column': 2}
verse_b = {**effects.heatinvert, 'bg_column': 3}
duba = {**effects.heatinvert, 'bg_column': 4}
bones = {**effects.heatinvert, 'bg_column': 5}
chorus_a = {**effects.heatinvert, 'bg_column': 6}
chorus_a_prime = {**effects.heatinvert, 'bg_column': 7}
chorus_b = {**effects.heatinvert, 'bg_column': 8}
chorus_b_prime = {**effects.heatinvert, 'bg_column': 9}
chorus_duba = {**effects.heatinvert, 'bg_column': 10}
chorus_eeee = {**effects.heatinvert, 'bg_column': 11}
verse_c = {**effects.heatinvert, 'bg_column': 12}
verse_d = {**effects.heatinvert, 'bg_column': 13}
quiet = {**effects.heatinvert, 'bg_column': 14}
verse_e = {**effects.heatinvert, 'bg_column': 15, 'init': pulse_clear_init}
verse_f = {**effects.heatinvert, 'bg_column': 16, 'init': pulse_clear_init}
chorus_c = {**effects.heatinvert, 'bg_column': 17, 'init': pulse_clear_init}
chorus_d = {**effects.heatinvert, 'bg_column': 18, 'init': pulse_clear_init}
chorus_duba_prime = {**effects.heatinvert, 'bg_column': 19, 'init': pulse_clear_init}
end = {**effects.heatinvert, 'bg_column': 20, 'init': pulse_clear_init}


controls = [
  effects.blank, intro, verse_a, duba, verse_b, bones, duba, 

  chorus_a, chorus_duba, chorus_b, chorus_eeee, 
  chorus_a, chorus_duba, chorus_b, chorus_eeee, chorus_duba, 

  verse_c, quiet, verse_c, verse_d, duba, 
  verse_c, duba, 

  chorus_a_prime, chorus_duba, chorus_b_prime, chorus_eeee, 
  chorus_a_prime, chorus_duba, chorus_b_prime, chorus_eeee, chorus_duba, 

  verse_e, duba, verse_f, duba,
  verse_e, duba, verse_f, duba,
  verse_e,

  chorus_c, chorus_duba_prime, chorus_d, chorus_duba_prime, 
  chorus_c, chorus_duba_prime, chorus_d, chorus_duba_prime, end
]
