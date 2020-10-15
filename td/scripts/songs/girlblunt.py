from resolume_commands import pulse_clear_init
import effects

intro = {**effects.clear, 'bg_column': 1, 'init': pulse_clear_init}
chorus_a = {**effects.blank, 'bg_column': 2}
chorus_b = {**effects.blank, 'bg_column': 3}
verse_a = {**effects.blank, 'bg_column': 4}
verse_b = {**effects.blank, 'bg_column': 5}
verse_c = {**effects.blank, 'bg_column': 6}
verse_d = {**effects.blank, 'bg_column': 7}
dropout = {**effects.blank, 'bg_column': 8}
chorus_c = {**effects.blank, 'bg_column': 9}
chorus_d = {**effects.blank, 'bg_column': 10}
chorus_e = {**effects.blank, 'bg_column': 11}
chorus_f = {**effects.blank, 'bg_column': 12}
outro = {**effects.blank, 'bg_column': 13}
end = {**effects.blank, 'bg_column': 14}

controls = [ 
  effects.blank, intro, 
  chorus_a, chorus_b, chorus_a, chorus_b, 
  verse_a, verse_b, 
  chorus_a, chorus_b, chorus_a, chorus_b, 
  verse_c, verse_d, dropout, 
  verse_c, verse_d, 
  chorus_c, chorus_d,   
  chorus_e, chorus_f, 
  outro, end
]
