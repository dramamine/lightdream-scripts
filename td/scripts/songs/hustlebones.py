intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
verse_a = {'bg_column': 2}
verse_b = {'bg_column': 3}
duba = {'bg_column': 4}
bones = {'bg_column': 5}
chorus_a = {'bg_column': 6}
chorus_a_prime = {'bg_column': 7}
chorus_b = {'bg_column': 8}
chorus_b_prime = {'bg_column': 9}
chorus_duba = {'bg_column': 10}
chorus_eeee = {'bg_column': 11}
verse_c = {'bg_column': 12}
verse_d = {'bg_column': 13}
quiet = {'bg_column': 14}
verse_e = {'bg_column': 15, 'pulse_clear': True}
verse_f = {'bg_column': 16, 'pulse_clear': True}
chorus_c = {'bg_column': 17, 'pulse_clear': True}
chorus_d = {'bg_column': 18, 'pulse_clear': True}
chorus_duba_prime = {'bg_column': 19, 'pulse_clear': True}
end = {'bg_column': 20, 'pulse_clear': True}


controls = [
  None, intro, verse_a, duba, verse_b, bones, duba,

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
