from functools import partial
from resolume_commands import send, simple_effects_hit, dashboardKnobPre1, dashboardKnobPre2, dashboardKnobBG1, dashboardKnobBG2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off
# import sequences
import effects

intro_a = {**effects.php,
    'bg_column': 1,
    'knobs': [dashboardKnobBG1, dashboardKnobPre2]
}

intro_shift = {**effects.php,
    'bg_column': 2,
    'knobs': [dashboardKnobBG1, dashboardKnobPre2]
}

intro_b = {**effects.php,
    'bg_column': 3,
    'knobs': [dashboardKnobBG1, dashboardKnobPre2]
}

buildup_a = {**effects.rm, 'bg_column': 4}  # @TODO add bass hits
buildup_b = {**effects.rm, 'bg_column': 5}

pre_drop_a = {**effects.blank, 'bg_column': 6, 'resync': True}
pre_drop_b = {**effects.blank, 'bg_column': 7, 'resync': True}

drop_a = {**effects.eagle_spreader_inverter, 'bg_column': 8,
          'knobs': [dashboardKnobBG1, dashboardKnobBG2]}
drop_b = {**effects.eagle_spreader_inverter, 'bg_column': 9,
          'knobs': [dashboardKnobBG1, dashboardKnobBG2]}

# @TODO this one was special - maybe add bright/contrast to bg layer
drop_end = {**effects.eagle_spreader_inverter, 'bg_column': 10}

mid = {**effects.blank, 'bg_column': 11}

bridge_a = {**effects.colorwheel_quiet, 'bg_column': 12}
bridge_b = {**effects.colorwheel_loud, 'bg_column': 13}
end = {**effects.blank, 'bg_column': 14}

controls = {
    0: effects.clear,
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
    15: drop_end,
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
