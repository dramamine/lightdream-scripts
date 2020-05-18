from functools import partial
from resolume_commands import send, clear, default_init, simple_effects_hit, dashboardKnobPre1, dashboardKnobPre2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off

style_momentary = {
    # 'column': 0,  # intro A
    'init': default_init,
    'pulse': partial(simple_effects_hit, column=0, layer=6),
    'buttons': [
        [partial(simple_effects_hit, layer=0)],
        [partial(simple_effects_hit, layer=1)],
        [partial(simple_effects_hit, layer=2)],
        [partial(simple_effects_hit, layer=3)],
        [partial(simple_effects_hit, layer=4)],
        [partial(simple_effects_hit, layer=5)],
    ],
    'knobs': [dashboardKnobPre1, dashboardKnobPre2]
}

style_piano = {
    # 'column': 0,  # intro A
    'init': default_init,
    'pulse': partial(simple_effects_hit, column=0, layer=6),
    'buttons': [
        [partial(opacity_piano_on, layer=0),
         partial(opacity_piano_off, layer=0)],
        [partial(opacity_piano_on, layer=1),
         partial(opacity_piano_off, layer=1)],
        [partial(opacity_piano_on, layer=2),
         partial(opacity_piano_off, layer=2)],
        [partial(opacity_piano_on, layer=3),
         partial(opacity_piano_off, layer=3)],
        [partial(opacity_piano_on, layer=4),
         partial(opacity_piano_off, layer=4)],
        [partial(opacity_piano_on, layer=5),
         partial(opacity_piano_off, layer=5)],
    ],
    'knobs': [dashboardKnobPre1, dashboardKnobPre2]
}

style_clear = {
    'init': clear
}
