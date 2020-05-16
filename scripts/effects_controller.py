# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.
from utils import resync  # simple_bg_update  # , save_eg
# @TODO necessary?
eg = me.fetch('eg', 0);

module = None
controls = None

def load_song(module_name):
  global module, controls
  module = mod(module_name)
  controls = module.controls
  return

load_song('ocean')
# @TODO make this dynamic
# load_song( op('udp_recent_values')['module_name', 1] ))

# checking to see when buttons (button1-button6) are pressed,
# or released.
def onOffToOn(channel, sampleIndex, val, prev):
  is_on = 1 - int(val)
  # print("offToOn index:" + str(channel.index) + " (" + channel.name + ")" + str(val))
  column = controls[eg]['column']

  ctrlname = channel.name[:4]
  if ctrlname == 'butt':
    # get the control id
    # assume it's named 'button1' etc... or things will break
    controlid = int(channel.name[6:]) - 1;
    try:
      controls[eg]['buttons'][controlid][is_on](column=column)
    except (IndexError, KeyError):
      pass


  return

onOnToOff = onOffToOn

# one of the values in our 'rename1' chop has changed.
def onValueChange(channel, sampleIndex, val, prev):
  column = controls[eg]['column']
  # print("onValueChange:" + str(channel.index) +
  #       " (" + channel.name + ")" + str(val))
  if channel.name[:4] == 'knob':
    # knob 0 or 1
    controlid = int(channel.name[4:]) - 1
    print('lookin for knob:', controlid)
    try:
      controls[eg]['knobs'][controlid](
          val=val, 
          column=column
      )
    except (IndexError, KeyError):
      pass
    return

  if channel.name == 'effects_group':
    onEffectsGroupUpdate(int(val))
    return

  if channel.name == 'hit' and val > prev:
    try:
      controls[eg]['pulse'](column=column)
    except (IndexError, KeyError):
      pass
    return

  return

# called when we update an effects group.
def onEffectsGroupUpdate(val):
  global eg
  eg = val

  column = controls[val]['column']
  print("using column", column)

  try:
    controls[val]['init'](column)
  except (IndexError, KeyError):
    pass
  
  try:
    if controls[val]['resync']:
      resync()
  except (IndexError, KeyError):
    pass

  return
