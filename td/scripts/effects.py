from effects_styles import style_momentary, style_piano, style_clear

# @TODO do I need any of these guys anymore??
php = {
    **style_momentary,
    'effects_column': 1
}

heatinvert = {
    **style_piano,
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
    'effects_column': -1,
    'bg_column': 0
}
