from effects_styles import *

php = {
    **style_momentary,
    'effects_column': 1
}

rm = {
    **style_piano,
    'effects_column': 2
}

eagle_spreader_inverter = {
    **style_piano,
    'effects_column': 3
}

colorwheel_quiet = {
    **style_piano, 
    'effects_column': 4
}

colorwheel_loud = {
    **style_piano, 
    'effects_column': 5
}

# buttons do nothing, knobs still work
blank = {
    **style_piano,
    'effects_column': -1
}

clear = {
    **style_clear,
    'effects_column': -1
}
