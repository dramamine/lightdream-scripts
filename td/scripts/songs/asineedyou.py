from functools import partial
from resolume_commands import send, simple_effects_hit, pulse_clear_init, dashboardKnobPre1, dashboardKnobPre2, dashboardKnobBG1, dashboardKnobBG2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off
# import sequences
import effects

intro_quiet_a = {**effects.heatinvert, 'bg_column': 1, 'init': pulse_clear_init}
intro_quiet_b = {**effects.heatinvert, 'bg_column': 2, }
intro_drums = {**effects.heatinvert, 'bg_column': 3, }
verse_a = {**effects.heatinvert, 'bg_column': 4, }
verse_b = {**effects.heatinvert, 'bg_column': 5, 'init': pulse_clear_init}
verse_hipass = {**effects.heatinvert, 'bg_column': 6, 'init': pulse_clear_init}
verse_aprime = {**effects.heatinvert, 'bg_column': 7, 'init': pulse_clear_init}
vocals_pre = {**effects.heatinvert, 'bg_column': 8, 'init': pulse_clear_init}
vocals_a = {**effects.heatinvert, 'bg_column': 9, 'init': pulse_clear_init}
vocals_b = {**effects.heatinvert, 'bg_column': 10, }
verse_singin = {**effects.heatinvert, 'bg_column': 11, }
vocals_dropout = {**effects.heatinvert, 'bg_column': 12, }
pv_a = {**effects.heatinvert, 'bg_column': 13, }
pv_b = {**effects.heatinvert, 'bg_column': 14, }
pv_hipass = {**effects.heatinvert, 'bg_column': 15, }
pv_aprime = {**effects.heatinvert, 'bg_column': 16, }
pv_dropoff = {**effects.heatinvert, 'bg_column': 17, }
end = {**effects.heatinvert, 'bg_column': 18, 'init': pulse_clear_init}
 
# intro quiet a
# intro quiet b
# intro quiet a
# intro drums come in
# verse a
# verse hipass
# verse b
# verse hipass
# vocals pre
# vocals a
# vocals b
# vocals a
# verse a
# verse a'
# verse b
# verse hipass or '
# verse a 
# verse a'
# verse singin
# vocals dropout
# post-verse a
# post-verse b
# post-verse hi
# post-verse a
# post-verse '
# post-verse b
# post-verse dropoff
# intro quiet a
# intro quiet b
# end

controls = {
    0: effects.clear,
    1: intro_quiet_a,
    2: intro_quiet_b,
    3: intro_quiet_a,
    4: intro_drums,
    5: verse_a,
    6: verse_hipass,
    7: verse_b,
    8: verse_hipass,
    9: vocals_pre,
    10: vocals_a, 
    11: vocals_b,
    12: vocals_a,
    13: verse_a,
    14: verse_aprime,
    15: verse_b,
    16: verse_hipass,  # ??
    17: verse_a,
    18: verse_aprime,
    19: verse_singin,
    20: vocals_dropout,
    21: pv_a,
    22: pv_b,
    23: pv_hipass,
    24: pv_a,
    25: pv_aprime,
    26: pv_b,
    27: pv_dropoff,
    28: intro_quiet_a,
    29: intro_quiet_b,
    30: end
}
