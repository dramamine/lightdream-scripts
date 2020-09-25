# copied from some other file... can/should probably get rid of everything
from resolume_commands import pulse_clear_init
# import sequences
import effects

intro = {**effects.heatinvert, 'bg_column': 1, 'init': pulse_clear_init}

controls = {
    0: effects.blank,
    1: intro
}
