import random
total_clips = 82
total_effects = 29  # 21 + 8 blanks
intro = {'bg_column': 30, 'pulse_clear': True, 'transition_time': 0.5}

clips = [
  *range(1, total_clips), 
  *range(1, total_clips),
  *range(1, total_clips),
  *range(1, total_clips),
  *range(1, total_clips),
  *range(1, total_clips)
]

effects = [
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects),
  *range(1, total_effects)
]

random.shuffle(clips)
random.shuffle(effects)


def turn_into_column(a, b):
  return {'bg_column': a, 'effects_column': b}

controls = [
  None,
  intro,
  *map(turn_into_column, clips, effects)
]
