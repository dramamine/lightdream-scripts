# background layer. note these are 1-indexed.
layer_bg = 1
# pre- buttons layer. ex. effects that only affect the BG layer
# layer_pre = 2

layer_pulses = 2

# which layer contains the first button?
layer_button_first = 3

# layer_post = 10

def send(loc, val):
  op('resolume').sendOSC(loc, [val])

# # just run the clip.
# # column (int): which column are we using?
# # blayer (idx): which button was pressed? should be 0-index
def simple_effects_hit(layer, column):
  if column <= 0:
    print("WARN: simple_effects_hit called with column <= 0")
  send("/composition/layers/{}/clips/{}/connect".format(layer_pulses, column), 1)

def clip_piano_on(layer, column=0):
  button_layer = layer_button_first + layer
  send("/composition/layers/{}/clips/{}/connect".format(button_layer, column), 1.0)
  send("/composition/layers/{}/clips/{}/transport/position".format(button_layer, column), 1.0)
  send("/composition/layers/{}/clips/{}/transport/position/behaviour/playdirection".format(button_layer, column), 2)
  return

def clip_piano_off(layer, column=0):
  button_layer = layer_button_first + layer
  send("/composition/layers/{}/clips/{}/transport/position/behaviour/playdirection".format(button_layer, column), 0)
  return

def opacity_piano_on(layer, column=0):
  # print("opac on. using layer ", layer, "column:", column)
  button_layer = layer_button_first + layer
  send("/composition/layers/{}/clips/{}/connect".format(button_layer, column), 1.0)
  send("/composition/layers/{}/clips/{}/video/opacity".format(button_layer, column), 1.0)
  send("/composition/layers/{}/clips/{}/video/opacity/behaviour/playdirection".format(button_layer, column), 2)
  return

def opacity_piano_off(layer, column=0):
  button_layer = layer_button_first + layer
  send("/composition/layers/{}/clips/{}/video/opacity/behaviour/playdirection".format(button_layer, column), 0)
  return

# update the bg.
def simple_bg_update(idx):
  # print("INFO: simple_bg_update: ", idx)
  if (idx <= 0):
    send('/composition/layers/1/clear', 1)
    send('/composition/layers/1/clear', 0)
    return
  send('/composition/layers/{}/clips/{}/connect'.format(layer_bg, idx), 1)
  return

# just clear out the last pulse.
def default_init(column):
  # print("INFO: default init with column:", column)
  # send("/composition/layers/{}/clips/{}/connect".format(# layer_post, column), 1)  # post
  # send("/composition/layers/{}/clips/{}/connect".format(layer_pulses, column), 1)  # pre
  return

def do_autopilot(yes):
  if yes:
    send("/composition/layers/1/transition/duration", 0.5)
    send("/composition/layers/1/autopilot", 3)
  else:
    send("/composition/layers/1/transition/duration", 0.0)
    send("/composition/layers/1/autopilot", 1)
  return

# def dashboardKnobPre(val, layer, column, link):
#   send("/composition/layers/{}/clips/{}/dashboard/link{}".format(layer, column, link), val)
#   return

# # in layer 'Pre', control the 1st dashboard knob
# def dashboardKnobPre1(val, column):
#   if column <= 0:
#     print("WARN: dashboardKnobPre1 called with column <= 0")
#   dashboardKnobPre(val, layer_pre, column, 1)
#   return 

# # in layer 'Pre', control the 1st dashboard knob
# def dashboardKnobPre2(val, column):
#   if column <= 0:
#     print("WARN: dashboardKnobPre1 called with column <= 0")
#   dashboardKnobPre(val, layer_pre, column, 2)
#   return


# def dashboardKnobBG1(val, column):
#   dashboardKnobPre(val, layer_bg, column, 1)
#   return

# def dashboardKnobBG2(val, column):
#   dashboardKnobPre(val, layer_bg, column, 2)
#   return

# keeping it simple:
# controlid refers to the integer of "knob1"-"knob6"
# this maps to a layer
def updated_knob_handler(val, column, controlid, left):
  # print("coming soon", val, column, controlid, left)
  layer = controlid + 2
  link = 1 if left else 2
  send("/composition/layers/{}/clips/{}/dashboard/link{}".format(layer, column, link), val)
  return

def clear(opt=0):
  send('/composition/layers/1/clear', 1)
  send('/composition/layers/2/clear', 1)
  # send('/composition/layers/3/clear', 1)
  # send('/composition/layers/4/clear', 1)
  # send('/composition/layers/5/clear', 1)
  # send('/composition/layers/6/clear', 1)
  # send('/composition/layers/7/clear', 1)
  # send('/composition/layers/8/clear', 1)
  # send('/composition/layers/9/clear', 1)
  send('/composition/layers/1/clear', 0)
  send('/composition/layers/2/clear', 0)
  # send('/composition/layers/3/clear', 0)
  # send('/composition/layers/4/clear', 0)
  # send('/composition/layers/5/clear', 0)
  # send('/composition/layers/6/clear', 0)
  # send('/composition/layers/7/clear', 0)
  # send('/composition/layers/8/clear', 0)
  # send('/composition/layers/9/clear', 0)
  return

# clears any active pulses
def pulse_clear_init(column):
  send("/composition/layers/{}/clear".format(layer_pulses), 1)
  send("/composition/layers/{}/clear".format(layer_pulses), 0)
  default_init(column)
  return


def update_tempo(bpm):
    send('/composition/tempocontroller/tempo', bpm)
    return

def resync():
    send('/composition/tempocontroller/resync', 1)
    send('/composition/tempocontroller/resync', 0)
    return

def update_deck(idx):
  print("update deck called.")
  send("/composition/decks/{}/select".format(int(idx)), 1)
  return
