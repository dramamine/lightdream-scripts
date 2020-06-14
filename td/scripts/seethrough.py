#from functools import partial
#from resolume_commands import send, simple_effects_hit, dashboardKnobPre1, dashboardKnobPre2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off
import effects

intro_a = {**effects.blank, 'bg_column': 1, }
intro_b = {**effects.blank, 'bg_column': 2, }
pre_verse = {**effects.blank, 'bg_column': 3, }
verse_a = {**effects.blank, 'bg_column': 4, }
verse_b = {**effects.blank, 'bg_column': 5, }
pre_chorus = {**effects.blank, 'bg_column': 6, }
drop_into_chorus = {**effects.blank, 'bg_column': 7, }
chorus_a = {**effects.blank, 'bg_column': 8, }
chorus_b = {**effects.blank, 'bg_column': 9, }
postchorus_a = {**effects.blank, 'bg_column': 10, }
postchorus_b = {**effects.blank, 'bg_column': 11, }
endriff_a = {**effects.blank, 'bg_column': 12, }
endriff_b = {**effects.blank, 'bg_column': 13, }
end = {**effects.blank, 'bg_column': 14, }

controls = {
    0: effects.clear,
    1: intro_a,
    2: intro_b,
    3: pre_verse,
    4: verse_a,
    5: verse_b,
    6: verse_a,
    7: verse_b,
    8: pre_chorus,
    9: drop_into_chorus,
    10: chorus_a,
    11: chorus_b,
    12: chorus_a,
    13: chorus_b,
    14: postchorus_a,
    15: postchorus_b,
    16: endriff_a,
    17: endriff_b,
    18: end
}
