# copied from some other file... can/should probably get rid of everything
from resolume_commands import pulse_clear_init
# import sequences
import effects

# intro
# buildup a
# buildup b
# throwdown 
# verse a
# verse b
# verse c
# chorus a
# chorus b
# chorus a 
# vroom a
# vroom b
# buildup a
# buildup b
# combo a
# chorus a
# chorus b 
# vroom a
# vroom b 
# end

intro = {**effects.heatinvert, 'bg_column': 1, 'init': pulse_clear_init}
buildup_a = {**effects.heatinvert, 'bg_column': 2}
buildup_b = {**effects.heatinvert, 'bg_column': 3}
combo_a = {**effects.heatinvert, 'bg_column': 4}
throwdown = {**effects.heatinvert, 'bg_column': 5}
verse_a = {**effects.heatinvert, 'bg_column': 6, 'init': pulse_clear_init}
verse_b = {**effects.heatinvert, 'bg_column': 7}
verse_c = {**effects.heatinvert, 'bg_column': 8}
chorus_a = {**effects.heatinvert, 'bg_column': 9}
chorus_b = {**effects.heatinvert, 'bg_column': 10}
chorus_c = {**effects.heatinvert, 'bg_column': 11}
vroom_a = {**effects.heatinvert, 'bg_column': 12}
vroom_b = {**effects.heatinvert, 'bg_column': 13}
end = {**effects.heatinvert, 'bg_column': 14, 'init': pulse_clear_init}


controls = [
    effects.blank, intro, 
    
    buildup_a, buildup_b, throwdown,
    verse_a, verse_b, verse_c,
    chorus_a, chorus_b, chorus_a,
    vroom_a, vroom_b,

    buildup_a, buildup_b, combo_a,
    chorus_a, chorus_b, chorus_a,
    vroom_a, vroom_b,
    end
]
