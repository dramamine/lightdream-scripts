from functools import partial
from resolume_commands import clear, default_init, simple_effects_hit, updated_knob_handler, opacity_piano_on, opacity_piano_off

style_momentary = {
    # 'column': 0,  # intro A
    'init': default_init,
    'pulse': partial(simple_effects_hit, layer=6),
    'buttons': [
        [partial(simple_effects_hit, layer=0)],
        [partial(simple_effects_hit, layer=1)],
        [partial(simple_effects_hit, layer=2)],
        [partial(simple_effects_hit, layer=3)],
        [partial(simple_effects_hit, layer=4)],
        [partial(simple_effects_hit, layer=5)],
    ],
    'knobs': updated_knob_handler
}

style_piano = {
    # 'column': 0,  # intro A
    'init': default_init,
    'pulse': partial(simple_effects_hit, layer=6),
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
    'knobs': updated_knob_handler
}

style_clear = {
    'init': clear,
    'pulse': partial(simple_effects_hit, layer=6),
}
