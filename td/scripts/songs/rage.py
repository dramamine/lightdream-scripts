from resolume_commands import pulse_clear_init
import effects

intro = {**effects.clear, 'bg_column': 1, 'init': pulse_clear_init}
verse_a = {**effects.clear, 'bg_column': 2, 'init': pulse_clear_init}
verse_b = {**effects.blank, 'bg_column': 3, 'init': pulse_clear_init}
verse_c = {**effects.blank, 'bg_column': 4}
verse_d = {**effects.blank, 'bg_column': 5}
ragin = {**effects.blank, 'bg_column': 6}
dropout = {**effects.blank, 'bg_column': 7}
outro = {**effects.blank, 'bg_column': 8}
end = {**effects.blank, 'bg_column': 9}

controls = [
    effects.blank, intro,
    verse_a, verse_b, verse_a, verse_b,
    ragin, dropout,
    verse_a, verse_c, dropout, 
    verse_b, verse_d, dropout,
    verse_a, verse_c,
    ragin, dropout,
    verse_a, verse_c, verse_d,
    outro, end
]
