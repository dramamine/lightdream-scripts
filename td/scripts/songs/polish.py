intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
pads_a = {'bg_column': 2}
pads_b = {'bg_column': 3}
pads_c = {'bg_column': 4}
pads_d = {'bg_column': 5}
drums_a = {'bg_column': 6}
drums_b = {'bg_column': 7}
drums_c = {'bg_column': 8, 'pulse_clear': True}
drums_d = {'bg_column': 9, 'pulse_clear': True}
waah_a = {'bg_column': 10, 'pulse_clear': True}
waah_b = {'bg_column': 11}
waah_c = {'bg_column': 12}
quiet_a = {'bg_column': 13}
quiet_b = {'bg_column': 14}
end = {'bg_column': 15}

controls = [ 
  None, intro, pads_a, pads_b, pads_c, pads_d,
  quiet_a, quiet_b,
  drums_a, drums_b, drums_c, drums_d,
  waah_a, waah_b, waah_c,
  drums_a, drums_b, drums_c,
  quiet_a, quiet_b
]

## Intro video start is weird since the scale is at 100-0  or whatever
## Pulses not working
## Drums D opacity is weird
## what if quiet_a and quiet_b had offbeats only
## 14 layer 14 missing?