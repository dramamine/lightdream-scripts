# background layer. note these are 1-indexed.
layer_bg = 1
# pre- buttons layer. ex. effects that only affect the BG layer
layer_pre = 2
# which layer contains the first button?
layer_button_first = 3

layer_post = 10

# @TODO necessary?
eg = me.fetch('eg', 0)
# print("utils think eg is:", eg)

# @TODO necessary? not implemented yet.
def save_eg(new_eg):
  global eg
  eg = new_eg

def send(loc, val):
  op('resolume').sendOSC(loc, [val])


eg = me.fetch('eg', 0)
# print("utils ran and updated eg.")

# just run the clip.
# column (int): which column are we using?
# blayer (idx): which button was pressed? should be 0-index
def simple_effects_hit(layer, column=eg):
  # print("simple effects hit on column:" + str(eg) + "idx:" + str(layer))
  button_layer = layer_button_first + layer
  send('/composition/layers/' + str(button_layer) + '/clips/' + str(column) + '/connect', 1)


def clip_piano_on(layer, column=0):
  # print("opac on. using layer ", layer, "column:", column)
  button_layer = layer_button_first + layer
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/connect', 1.0)
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/transport/position', 1.0)
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/transport/position/behaviour/playdirection', 2)
  return


def clip_piano_off(layer, column=0):
  button_layer = layer_button_first + layer
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/transport/position/behaviour/playdirection', 0)
  return

def opacity_piano_on(layer, column=0):
  # print("opac on. using layer ", layer, "column:", column)
  button_layer = layer_button_first + layer
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/connect', 1.0)
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/video/opacity', 1.0)
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/video/opacity/behaviour/playdirection', 2)
  return

def opacity_piano_off(layer, column=0):
  button_layer = layer_button_first + layer
  send('/composition/layers/'+str(button_layer) +
       '/clips/' + str(column) + '/video/opacity/behaviour/playdirection', 0)
  return

# update the bg.
def simple_bg_update(idx):
  print("simple bg update called. trouble?", idx)
  send('/composition/layers/' + str(layer_bg) + '/clips/' + str(idx) + '/connect', 1)
  return

def dashboardKnobPre(val, layer, idx, link):
  send('/composition/layers/' + str(layer) + '/clips/' + str(idx) + '/dashboard/link' + str(link), val)
  return

# in layer 'Pre', control the 1st dashboard knob
def dashboardKnobPre1(val, idx=eg):
  dashboardKnobPre(val, layer_pre, idx, 1)
  return 

# in layer 'Pre', control the 1st dashboard knob
def dashboardKnobPre2(val, idx=eg):
  dashboardKnobPre(val, layer_pre, idx, 2)
  return


def dashboardKnobBG1(val, idx):
  dashboardKnobPre(val, layer_bg, idx, 1)
  return

def default_init(column):
  print("default init with column:", column)
  send('/composition/layers/' + str(layer_post) + '/clips/' + str(column) + '/connect', 1)  # pre
  send('/composition/layers/' + str(layer_pre) + '/clips/' + str(column) + '/connect', 1)  # pre
  send('/composition/layers/' + str(layer_bg) + '/clips/' + str(column) + '/connect', 1)  #bg
  return


def clear(opt=0):
  send('/composition/layers/1/clear', 1)
  send('/composition/layers/2/clear', 1)
  send('/composition/layers/3/clear', 1)
  send('/composition/layers/4/clear', 1)
  send('/composition/layers/5/clear', 1)
  send('/composition/layers/6/clear', 1)
  send('/composition/layers/7/clear', 1)
  send('/composition/layers/1/clear', 0)
  send('/composition/layers/2/clear', 0)
  send('/composition/layers/3/clear', 0)
  send('/composition/layers/4/clear', 0)
  send('/composition/layers/5/clear', 0)
  send('/composition/layers/6/clear', 0)
  send('/composition/layers/7/clear', 0)
  return
