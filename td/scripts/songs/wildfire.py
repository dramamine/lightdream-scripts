intro = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
verse_a = {'bg_column': 2}
verse_b = {'bg_column': 3}
funky = {'bg_column': 4}
verse_c = {'bg_column': 5}
verse_d = {'bg_column': 6}
verse_e = {'bg_column': 7}
chorus_a = {'bg_column': 8, 'pulse_clear': True}
chorus_b = {'bg_column': 9}
chorus_c = {'bg_column': 10}
bridge_a = {'bg_column': 11}
bridge_b = {'bg_column': 12}
quiet_a = {'bg_column': 13, 'pulse_clear': True}
quiet_b = {'bg_column': 14}
outro = {'bg_column': 15}
end = {'bg_column': 16}

controls = [
    None, intro,
    verse_a, verse_b, verse_a, verse_b, funky,
    chorus_a, chorus_b, 
    verse_c, verse_d, 
    verse_e,
    chorus_a, chorus_b, chorus_c,
    bridge_a, bridge_b, 
    chorus_a, chorus_b,
    quiet_a, quiet_b, outro, end
]

## Intro video start is weird since the scale is at 100-0  or whatever
## Pulses not working
## Drums D opacity is weird
## what if quiet_a and quiet_b had offbeats only
## 14 layer 14 missing?
