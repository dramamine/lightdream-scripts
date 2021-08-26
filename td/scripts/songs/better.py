riff_0 = {'bg_column': 1, 'pulse_clear': True}
riff_a = {'bg_column': 2, 'pulse_clear': True}
riff_b = {'bg_column': 3}
drums = {'bg_column': 4, 'pulse_toggle_on_load': True}
drums_b = {'bg_column': 5, 'pulse_toggle_on_load': True}
jam_a = {'bg_column': 6, 'pulse_clear': True}
jam_b = {'bg_column': 7}
chorus_a = {'bg_column': 8, 'pulse_clear': True}
chorus_b = {'bg_column': 9, 'pulse_clear': True}
bridge_0 = {'bg_column': 10, 'pulse_clear': True}
bridge_a = {'bg_column': 11, 'pulse_clear': True}
bridge_b = {'bg_column': 12}
quiet_0 = {'bg_column': 13}
quiet_a = {'bg_column': 14}
quiet_b = {'bg_column': 15}
outro_a = {'bg_column': 16, 'pulse_clear': True}
outro_b = {'bg_column': 17}

controls = [
  None,
  riff_0, riff_a, riff_b, drums,
  jam_a, jam_b, drums,
  chorus_a, drums,
  chorus_b, drums,
  riff_a, riff_b, drums,
  chorus_a, drums,
  chorus_b, drums,
  bridge_0, drums_b,
  bridge_a, bridge_b,
  quiet_0, quiet_a, quiet_b, drums_b,
  chorus_a, chorus_b,
  outro_a, outro_b
]
