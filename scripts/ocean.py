from functools import partial
from utils import send, simple_effects_hit, dashboardKnobPre1, dashboardKnobPre2, dashboardKnobBG1, dashboardKnobBG2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off
import sequences

# sections
# intro a
# intro shift
# intro b
# intro shift
# intro a
# buildup a
# buildup b
# drop a
# drop b
# drop end
# drop a
# drop b
# drop end
# mid
# bridge a
# bridge b
# bridge a
# buildup a (dank version)
# buildup b (dank version)
# pre-drop
# drop a
# drop b
# drop end
# drop a
# drop b
# drop end
# real end.


intro_a = {**sequences.simple_effects_hits, 
  'column': 1,
  'knobs': [dashboardKnobBG1, dashboardKnobPre2]
}

intro_shift = {**sequences.simple_effects_hits, 
  'column': 2,
  'knobs': [dashboardKnobBG1, dashboardKnobPre2]
}

intro_b = {**sequences.simple_effects_hits, 
  'column': 3,
  'knobs': [dashboardKnobBG1, dashboardKnobPre2]
}

buildup_a = {**sequences.opacity_pianos, 'column': 4} # @TODO add bass hits
buildup_b = {**sequences.opacity_pianos, 'column': 5}

pre_drop_a = {**sequences.opacity_pianos, 'column': 6, 'resync': True}
pre_drop_b = {**sequences.opacity_pianos, 'column': 7, 'resync': True}

drop_a = {**sequences.opacity_pianos, 'column': 8,
          'knobs': [dashboardKnobBG1, dashboardKnobBG2]}
drop_b = {**sequences.opacity_pianos, 'column': 9,
          'knobs': [dashboardKnobBG1, dashboardKnobBG2]}
drop_end = {**sequences.opacity_pianos, 'column': 10}

mid = {**sequences.opacity_pianos, 'column': 11}

bridge_a = {**sequences.opacity_pianos, 'column': 12}
bridge_b = {**sequences.opacity_pianos, 'column': 13}
end = {**sequences.opacity_pianos, 'column': 14}

controls = {
  0: sequences.sequence_clear,
  1: intro_a,
  2: intro_shift,
  3: intro_b,
  4: intro_shift, 
  5: intro_a,
  6: buildup_a,  # you could put an ocean 
  7: buildup_b,  # if im caught
  8: pre_drop_a,  # 1 measure
  9: pre_drop_b,  # 1 measure
  10: drop_a,
  11: drop_b,
  12: drop_end,
  13: drop_a,
  14: drop_b,
  15: drop_end, # @TODO dont do this, jsut continue with drop_b maybe?
  16: mid,
  17: bridge_a, 
  18: bridge_b,  
  19: intro_a,  # when my echos.. 
  20: buildup_a,  # you could put  an ocean
  21: buildup_b,
  22: pre_drop_a,  # 1 measure
  23: pre_drop_b,  # 1 measure
  24: drop_a,
  25: drop_b,
  26: drop_end,
  27: drop_a,
  28: drop_b,
  29: drop_end,
  30: end
}

