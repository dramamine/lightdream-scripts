from functools import partial
from resolume_commands import clear, simple_effects_hit, default_init

style_momentary = {
    # 'column': 0,  # intro A
    'init': default_init,
    'pulse': partial(simple_effects_hit, layer=6),
}

style_piano = {
    # 'column': 0,  # intro A
    'init': default_init,
    'pulse': partial(simple_effects_hit, layer=6),
}

style_clear = {
    'init': clear,
    'pulse': partial(simple_effects_hit, layer=6),
}
