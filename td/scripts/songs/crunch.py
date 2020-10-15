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

controls = [ 
    effects.clear, intro, intro_offbeats, intro_basswonk, 
    verse_a, verse_b, intro_offbeats, intro_basswonk, 
    verse_c, verse_d, 
    space_a, space_b, outro, end
]
