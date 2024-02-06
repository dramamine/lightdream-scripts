# background layer. note these are 1-indexed.
import random

TRANSITION_DURATION = 2.0

layer_bg = 1
layer_pulses = 2
layer_effects = 4

LAYER_BG = 1
LAYER_MASK = 2
LAYER_TOP = 3

def send(loc, val):
  op('resolume').sendOSC(loc, [val])


def activate_clip(layer, column_id):
  send('/composition/layers/{}/clips/{}/connect'.format(layer, column_id), 1)
  return

def activate_effect(layer, effect_name):
  send('/composition/layers/{}/video/effects/{}/bypassed'.format(layer, effect_name), 0)
  return

def deactivate_effect(layer, effect_name):
  send('/composition/layers/{}/video/effects/{}/bypassed'.format(layer, effect_name), 1)
  return










# update the bg.
def activate_bg_column(column_id):
  send('/composition/layers/{}/clips/{}/connect'.format(layer_bg, column_id), 1)
  return


# def activate_effects_column(column_id):
#   send('/composition/layers/{}/clips/{}/connect'.format(layer_effects, column_id), 1)
#   return


def do_autopilot(yes):
  val = 3 if yes else 1
  send("/composition/layers/1/autopilot", val)
  return

# update transition time for bg layer. value given in seconds
def update_transition_time(layer, val):
  print("updating duration:", layer, val)
  send("/composition/layers/{}/transition/duration".format(layer), val/10)
  return

def update_blend_mode(layer, val):
  send("/composition/layers/{}/video/transition/mixer/blendmode".format(layer), val)
  return

# # update transition time for pulses/bgs layer
# def update_transition_time(val, layers=2):
#   for i in range(1, layers+1):
#     print("updating duration:", i, val)
#     send("/composition/layers/{}/transition/duration".format(i), val)
#   return


def clear():
  send('/composition/layers/1/clear', 1)
  send('/composition/layers/2/clear', 1)
  send('/composition/layers/3/clear', 1)
  send('/composition/layers/4/clear', 1)
  send('/composition/layers/1/clear', 0)
  send('/composition/layers/2/clear', 0)
  send('/composition/layers/3/clear', 0)
  send('/composition/layers/4/clear', 0)
  return

# clears any active pulses


# def pulse_clear():
#   send("/composition/layers/{}/clear".format(layer_pulses), 1)
#   send("/composition/layers/{}/clear".format(layer_pulses), 0)
#   return


# def pulse_hit(column):
#   send("/composition/layers/{}/clips/{}/connect".format(layer_pulses, column), 1)
#   return


# def set_pulse_playback_direction(column, reversed):
#   val = 0 if reversed else 2
#   send("/composition/layers/{}/clips/{}/transport/position/behaviour/playdirection".format(layer_pulses, column), val)
#   return


def update_tempo(bpm):
  send('/composition/tempocontroller/tempo', bpm)
  return


def resync():
  send('/composition/tempocontroller/resync', 1)
  send('/composition/tempocontroller/resync', 0)
  return


def update_deck(idx):
  send("/composition/decks/{}/select".format(int(idx)), 1)
  return


def heartbeat():
  print("heartbeat called.")
  return


def first_layer_only_instant_fadeout_others(first_clip_idx = 1):
  print("first_layer_only_instant_fadeout_others")
  send('/composition/layers/2/clear', 0)
  send('/composition/layers/3/clear', 0)
  send('/composition/layers/4/clear', 0)
  send('/composition/layers/1/clips/{}/connect'.format(first_clip_idx), 1)
  return


# choose one effect to be the audio-responsive effect out of these
bg_layer_audio_effects = [
    'huerotate',
    'suckr'
]


def pick_random_bg_layer_audio_effect():
  mychoice = random.choice(bg_layer_audio_effects)
  for effect in bg_layer_audio_effects:
    val = 0 if effect == mychoice else 1
    send('/composition/layers/1/video/effects/{}/bypassed'.format(effect), val)


# what to do on change

# 0-3
section = 0

# 0-3
intensity = 0

current_mask = -1
max_mask = 18


def update_section():
  if section == 0:
    add_mask()
  return


def add_mask():
  global current_mask
  target = current_mask
  while target == current_mask:
    target = random.randint(0, max_mask)

  # set appropriate transition
  send('/composition/layers/2/video/opacity/behaviour/duration',
       TRANSITION_DURATION / 604800.0)
  send('/composition/layers/2/video/opacity/behaviour/playdirection', 2)

  # activate clip
  send('/composition/layers/2/clips/{}/connect'.format(target), 1)
  current_mask = target
  return

