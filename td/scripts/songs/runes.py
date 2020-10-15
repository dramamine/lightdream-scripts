import effects
from resolume_commands import pulse_clear_init

intro = {
    **effects.heatinvert,
    'bg_column': 1,
}

verse_a = {
    **effects.heatinvert,
    'bg_column': 2,
    'init': pulse_clear_init
}
verse_b = {
    **effects.heatinvert,
    'bg_column': 3,
}
wonk = {
    **effects.heatinvert,
    'bg_column': 4,
}
quiet_a = {**effects.heatinvert, 'bg_column': 5, }
quiet_b = {**effects.heatinvert, 'bg_column': 6, }
quiet_c = {**effects.heatinvert, 'bg_column': 7, }
verseplus_a = {**effects.heatinvert, 'bg_column': 8, }
verseplus_b = {**effects.heatinvert, 'bg_column': 9, }
verseplus_c = {**effects.heatinvert, 'bg_column': 10, }
verseplus_d = {**effects.heatinvert, 'bg_column': 11, }
pre_end = {**effects.heatinvert, 'bg_column': 12, }
end = {**effects.heatinvert, 'bg_column': 13, 'init': pulse_clear_init}

controls = [
  effects.clear,
  intro,
  verse_a, verse_b,
  verse_a, verse_b,
  wonk, 
  quiet_a,  # if im caught
  quiet_a,  # 1 measure
  quiet_b,  # 1 measure
  quiet_c,
  verseplus_a, verseplus_b,
  verseplus_a, verseplus_b,
  verseplus_c, verseplus_d,
  pre_end, end
]
