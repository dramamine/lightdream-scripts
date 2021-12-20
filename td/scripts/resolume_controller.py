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

direction_is_reversed = False

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

load_song_by_index( int(op('rename1').chan('track_id')) )

# is this one of the decks where we want to turn on autopilot?
def should_autopilot(val):
  return val == 10

# one of the values in our 'rename1' chop has changed.
def onValueChange(channel, sampleIndex, val, prev):
  global direction_is_reversed

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
    resolume_commands.clear()

    if should_autopilot(val):
      resolume_commands.do_autopilot(True)
      resolume_commands.update_transition_time(0.5)
    elif should_autopilot(prev) and val != prev:
      resolume_commands.do_autopilot(False)

    # for safety, re-init the transition times
    resolume_commands.update_transition_time(0.)
    return
  
  if (channel.name == 'hit' and val > prev) or channel.name == 'pulse' and val > 0:
    try:
      column = controls[section]['bg_column']

      if ('direction_swap' in controls[section] and controls[section]['direction_swap']):
        direction_is_reversed = not direction_is_reversed
        resolume_commands.set_pulse_playback_direction(column, direction_is_reversed)
        return
      resolume_commands.pulse_hit(column)
    except (IndexError, KeyError):
      pass
    return

  return

# 'section' (i.e. section of the song) is used as an index to 'controls'.
# take the data from the section and make any resolume calls it designates.
#
# @param int new_section
#
def onSectionChange(new_section):
  global section
  section = new_section

  if section <= 0:
    return

  data = controls[section]

  try:
    resolume_commands.activate_bg_column(data['bg_column'])
  except (IndexError, KeyError):
    pass
  
  try:
    if data['pulse_clear']:
      print("clearing pulse")
      resolume_commands.pulse_clear()
  except (IndexError, KeyError):
    pass

  try:
    if data['resync']:
      resolume_commands.resync()
  except (IndexError, KeyError):
    pass

  try:
    if data['pulse_toggle_on_load']:
      resolume_commands.pulse_hit(data['bg_column'])
  except (IndexError, KeyError):
    pass

  try:
    if data['transition_time'] is not None:
      resolume_commands.update_transition_time(data['transition_time'])
  except (IndexError, KeyError):
    pass
  try:
    if data['transition_time_first_layer'] is not None:
      resolume_commands.update_transition_time(data['transition_time_first_layer'], 1)
  except (IndexError, KeyError):
    pass

  try:
    if data['effects_column']:
      resolume_commands.activate_effects_column(data['effects_column'])
  except (IndexError, KeyError):
    pass

  return
