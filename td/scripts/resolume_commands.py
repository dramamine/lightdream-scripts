
# background layer. note these are 1-indexed.
layer_bg = 1
layer_pulses = 2
layer_effects = 4


def send(loc, val):
  op('resolume').sendOSC(loc, [val])

# update the bg.


def activate_bg_column(column_id):
  send('/composition/layers/{}/clips/{}/connect'.format(layer_bg, column_id), 1)
  return


def activate_effects_column(column_id):
  send('/composition/layers/{}/clips/{}/connect'.format(layer_effects, column_id), 1)
  return


def do_autopilot(yes):
  val = 3 if yes else 1
  send("/composition/layers/1/autopilot", val)
  return

# update transition time for pulses/bgs layer


def update_transition_time(val, layers=2):
  for i in range(1, layers+1):
    print("updating duration:", i, val)
    send("/composition/layers/{}/transition/duration".format(i), val)
  return


def clear():
  send('/composition/layers/1/clear', 1)
  send('/composition/layers/2/clear', 1)
  send('/composition/layers/4/clear', 1)
  send('/composition/layers/1/clear', 0)
  send('/composition/layers/2/clear', 0)
  send('/composition/layers/4/clear', 0)
  return

# clears any active pulses


def pulse_clear():
  send("/composition/layers/{}/clear".format(layer_pulses), 1)
  send("/composition/layers/{}/clear".format(layer_pulses), 0)
  return


def pulse_hit(column):
  send("/composition/layers/{}/clips/{}/connect".format(layer_pulses, column), 1)
  return


def set_pulse_playback_direction(column, reversed):
  val = 0 if reversed else 2
  send("/composition/layers/{}/clips/{}/transport/position/behaviour/playdirection".format(layer_pulses, column), val)
  return


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
