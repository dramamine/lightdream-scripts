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
 
controls = [ effects.clear, 
  intro_quiet_a, intro_quiet_b, intro_quiet_a, intro_drums, 
  verse_a, verse_hipass, verse_b, verse_hipass, 
  vocals_pre, vocals_a,  vocals_b, vocals_a, verse_a, verse_aprime, 
  verse_b, verse_hipass,  
  verse_a, verse_aprime, verse_singin, vocals_dropout, 
  pv_a, pv_b, pv_hipass, pv_a, pv_aprime, pv_b, pv_dropoff, 
  intro_quiet_a, intro_quiet_b, end
]
