# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.
import resolume_commands

module = None
controls = None
section = 0

def load_song_by_index(row):
  load_song(op('track_info')[row, 'module_name'])
  return

def load_song(module_name):
  global module, controls, section
  module = mod(module_name)
  controls = module.controls
  section = int(op('rename1').chan('section'))
  return

load_song_by_index( int(op('rename1').chan('track_id')) )

# checking to see when buttons (button1-button6) are pressed,
# or released.
def onOffToOn(channel, sampleIndex, val, prev):
  is_on = 1 - int(val)
  # print("offToOn index:" + str(channel.index) + " (" + channel.name + ")" + str(val))
  column = controls[section]['effects_column']

  ctrlname = channel.name[:6]
  if ctrlname == 'button':
    # get the control id
    # assume it's named 'button1' etc... or things will break
    controlid = int(channel.name[6:]) - 1;
    try:
      controls[section]['buttons'][controlid][is_on](column=column)
    except (IndexError, KeyError):
      pass
  return

# using the same function as above
onOnToOff = onOffToOn

# one of the values in our 'rename1' chop has changed.
def onValueChange(channel, sampleIndex, val, prev):
  if channel.name == 'track_id':
    module_name = op('track_info')[int(val), 'module_name']
    print("retreived module", module_name, "for track id", val)
    load_song(module_name)
    return

  if channel.name == 'section':
    onSectionChange(int(val))
    return
  
  if channel.name == 'deck':
    resolume_commands.update_deck(val)
  
  column = controls[section]['effects_column']
  # print("onValueChange:" + str(channel.index) +
  #       " (" + channel.name + ")" + str(val))
  if channel.name[:4] == 'knob':
    # knob 0 or 1
    controlid = int(channel.name[4:]) - 1
    try:
      # controls[eg]['knobs'] is an array of knob functions, so
      # controls[eg]['knobs'][controlid] should access one of em.
      controls[section]['knobs'][controlid](
          val=val, 
          column=column
      )
    except (IndexError, KeyError):
      pass
    return

  if channel.name == 'hit' and val > prev:
    try:
      controls[section]['pulse'](column=column)
    except (IndexError, KeyError):
      pass
    return

  return

def onSectionChange(new_section):
  global section
  section = new_section
  print("hello from onSectionChange", section)
  resolume_commands.simple_bg_update(controls[section]['bg_column'])

  try:
    controls[section]['init'](controls[section]['effects_column'])
  except (IndexError, KeyError):
    pass
  
  try:
    if controls[section]['resync']:
      resolume_commands.resync()
  except (IndexError, KeyError):
    pass
  return
