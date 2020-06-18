from functools import partial
from resolume_commands import send, simple_effects_hit, pulse_clear_init, dashboardKnobPre1, dashboardKnobPre2, dashboardKnobBG1, dashboardKnobBG2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off
# import sequences
import effects

intro = {**effects.heatinvert, 'bg_column': 1, 'init': pulse_clear_init}
intro_offbeats = { **effects.heatinvert, 'bg_column': 2, }
intro_basswonk = { **effects.heatinvert, 'bg_column': 3, }
verse_a = { **effects.heatinvert, 'bg_column': 4, }
verse_b = {**effects.heatinvert, 'bg_column': 5, 'init': pulse_clear_init}
verse_c = {**effects.heatinvert, 'bg_column': 6, 'init': pulse_clear_init}
verse_d = {**effects.heatinvert, 'bg_column': 7, 'init': pulse_clear_init}
space_a = {**effects.heatinvert, 'bg_column': 8, 'init': pulse_clear_init}
space_b = {**effects.heatinvert, 'bg_column': 9, }
outro = {**effects.heatinvert, 'bg_column': 10, }
end = {**effects.heatinvert, 'bg_column': 11, 'init': pulse_clear_init}

# intro (w pulses)
# intro offbeats
# intro basswonk
# verse a
# verse b
# intro offbeats?
# intro basswonk
# verse c
# verse d
# space a
# space b
# outro


controls = {
    0: effects.clear,
    1: intro,
    2: intro_offbeats,
    3: intro_basswonk,
    4: verse_a,
    5: verse_b,
    6: intro_offbeats,
    7: intro_basswonk,
    8: verse_c,
    9: verse_d,
    10: space_a,
    11: space_b,
    12: outro,
    13: end
}
