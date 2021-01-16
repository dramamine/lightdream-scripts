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
  print("trying to load module:", module_name)
  module = mod(module_name)
  controls = module.controls
  section = int(op('rename1').chan('section'))
  return

# print("before load_song_by_index")
load_song_by_index( int(op('rename1').chan('track_id')) )
# print("after load_song_by_index")

# checking to see when buttons (button1-button6) are pressed,
# or released.
def onOffToOn(channel, sampleIndex, val, prev):
  # @TODO un-check in TouchDesigner

  # is_on = 1 - int(val)
  # print("offToOn index:" + str(channel.index) + " (" + channel.name + ")" + str(val))
  # column = controls[section]['effects_column']

  # ctrlname = channel.name[:6]
  # if ctrlname == 'button':
  #   # get the control id
  #   # assume it's named 'button1' etc... or things will break
  #   controlid = int(channel.name[6:]) - 1;
  #   try:
  #     controls[section]['buttons'][controlid][is_on](column=column)
  #   except (IndexError, KeyError):
  #     pass
  return

# using the same function as above
# @TODO remove
onOnToOff = onOffToOn

# is this one of the decks where we want to turn on autopilot?
def should_autopilot(val):
  return val == 10

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
    print("update deck is here:", val)
    resolume_commands.update_deck(val)
    if should_autopilot(val):
      resolume_commands.do_autopilot(True)
    elif should_autopilot(prev) and val != prev:
      resolume_commands.do_autopilot(False)
      
    return
  
  # # NOTE: on 6/2, changed this from 'effects_column' since my pulses and knobs
  # # have all been connected to the bg column I'm using.
  # try:
  #   column = controls[section]['bg_column']
  # except (IndexError, KeyError):
  #   print("ERR: could not find required entry bg_column in controls section:", section)
  #   return

  # if channel.name[:4] == 'knob':
  #   # knob 0 through 5
  #   controlid = int(channel.name[4:5])
  #   left = channel.name[5:6] == 'a'
  #   try:
  #     # controls[eg]['knobs'] is an array of knob functions, so
  #     # controls[eg]['knobs'][controlid] should access one of em.
  #     controls[section]['knobs'](
  #       val=val, 
  #       column=controls[section]['effects_column'],
  #       controlid=controlid,
  #       left=left
  #     )
  #   except (IndexError, KeyError):
  #     pass
  #   return

  if (channel.name == 'hit' and val > prev) or channel.name == 'pulse' and val > 0:
    try:
      column = controls[section]['bg_column']
      resolume_commands.pulse_hit(column)
    except (IndexError, KeyError):
      pass
    return

  return

def onSectionChange(new_section):
  # update global, in case I need it
  global section
  section = new_section

  data = controls[section]
  # print("hello from onSectionChange", section)
  try:
    resolume_commands.activate_bg_column(data['bg_column'])
  except (IndexError, KeyError):
    pass

  # old
  try:
    data['init'](data['bg_column'])
  except (IndexError, KeyError):
    pass
  
  # new
  try:
    if data['pulse_clear']:
      print("INFO: clearin")
      resolume_commands.pulse_clear()
  except (IndexError, KeyError):
    pass

  try:
    if data['resync']:
      print("INFO: resyncin")
      resolume_commands.resync()
  except (IndexError, KeyError):
    pass
  return
