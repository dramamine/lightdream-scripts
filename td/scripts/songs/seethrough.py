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

controls = [
  effects.clear,
  intro_a, intro_b,
  pre_verse,
  verse_a, verse_b,
  verse_a, verse_b,
  pre_chorus, drop_into_chorus,
  chorus_a, chorus_b,
  chorus_a, chorus_b,
  postchorus_a, postchorus_b,
  endriff_a, endriff_b,
  end
]
