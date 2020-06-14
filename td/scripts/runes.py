from functools import partial
from resolume_commands import send, simple_effects_hit, pulse_clear_init, dashboardKnobPre1, dashboardKnobPre2, dashboardKnobBG1, dashboardKnobBG2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off
# import sequences
import effects

#intro
# verse a ( 8 m)
# verse b ( 8 m)
# verse a
# verse b
# wonk (2 measures)
# quiet a
# quiet a
# quiet b
# quiet c
# verse++ a
# verse++ b
# verse++ a
# verse++ b
# verse++ c
# verse++ d
# pre-end
# end

intro = {
    **effects.blank,
    'bg_column': 1,
}

verse_a = {
    **effects.blank,
    'bg_column': 2,
    'init': pulse_clear_init
}
verse_b = {
    **effects.blank,
    'bg_column': 3,
}
wonk = {
    **effects.blank,
    'bg_column': 4,
}
quiet_a = { **effects.blank, 'bg_column': 5, }
quiet_b = { **effects.blank, 'bg_column': 6, }
quiet_c = { **effects.blank, 'bg_column': 7, }
verseplus_a = { **effects.blank, 'bg_column': 8, }
verseplus_b = { **effects.blank, 'bg_column': 9, }
verseplus_c = { **effects.blank, 'bg_column': 10, }
verseplus_d = { **effects.blank, 'bg_column': 11, }
pre_end = { **effects.blank, 'bg_column': 12, }
end = {**effects.blank, 'bg_column': 13, 'init': pulse_clear_init}


controls = {
    0: effects.clear,
    1: intro,
    2: verse_a,
    3: verse_b,
    4: verse_a,
    5: verse_b,
    6: wonk, 
    7: quiet_a,  # if im caught
    8: quiet_a,  # 1 measure
    9: quiet_b,  # 1 measure
    10: quiet_c,
    11: verseplus_a,
    12: verseplus_b,
    13: verseplus_a,
    14: verseplus_b,
    15: verseplus_c,
    16: verseplus_d,
    17: pre_end,
    18: end
}
