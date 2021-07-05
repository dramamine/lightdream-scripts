a = {'bg_column': 1, 'pulse_clear': True, 'resync': True, 'transition_time': 0.2}
b = {'bg_column': 2, 'pulse_clear': True }
c = {'bg_column': 3, 'pulse_clear': True }
d = {'bg_column': 4, 'pulse_clear': True }
e = {'bg_column': 5, 'pulse_clear': True }
f = {'bg_column': 6, 'pulse_clear': True }
g = {'bg_column': 7, 'pulse_clear': True }
h = {'bg_column': 8, 'pulse_clear': True }
ap = {'bg_column': 1, 'pulse_toggle_on_load': True}
bp = {'bg_column': 2, 'pulse_toggle_on_load': True}
cp = {'bg_column': 3, 'pulse_toggle_on_load': True}
dp = {'bg_column': 4, 'pulse_toggle_on_load': True}
ep = {'bg_column': 5, 'pulse_toggle_on_load': True}
fp = {'bg_column': 6, 'pulse_toggle_on_load': True}
gp = {'bg_column': 7, 'pulse_toggle_on_load': True}
hp = {'bg_column': 8, 'pulse_toggle_on_load': True}
end = {'bg_column': 9, 'transition_time': 0.0}

# 40 then the end

controls = [
  None,
  a, b, c, d, e, f,
  ap, bp, cp, dp, ep, fp,
  a, b, c, d, e, f,
  g, h, gp, hp,
  e, f, d, c, a, b,
  ep, fp, dp, cp, ap, bp,
  e, f, d, c, a, b,
  end
]

## TODO change transition times to what you need, then change them back at the end.
