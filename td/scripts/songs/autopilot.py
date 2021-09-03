import random
total_clips = 33
intro = {'bg_column': 30, 'pulse_clear': True, 'transition_time': 0.5}

options = [
  *range(1, total_clips), 
  *range(1, total_clips),
  *range(1, total_clips),
  *range(1, total_clips),
  *range(1, total_clips),
  *range(1, total_clips)
  ]

random.shuffle(options)


def turn_into_column(n):
  return {'bg_column': n}

controls = [
  None,
  intro,
  *map(turn_into_column, options)
]
