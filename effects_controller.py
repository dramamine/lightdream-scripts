# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.
from utils import simple_bg_update  # , save_eg
eg = me.fetch('eg', 0);
# print("effects_controller think eg is:", eg)
my_controls = mod('ocean').controls
# print("hi from file")


# def circle_init():
#   print("initializing controls");
#   op('resolume').sendOSC('/composition/layers/2/clips/2/connect', [1.0]);
#   op('resolume').sendOSC('/composition/layers/2/video/effects/circles/opacity', [0.0]);
#   return


# def circle_rotate(val):
#   return;


# def circle_inward():
#   print("circling inward");
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity/behaviour/playdirection', [0]);
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity', [0.8]);
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size/behaviour/playdirection', [0]);
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size', [1.0]);
#   return;


# def circle_outward():
#   print("circling outward");
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity/behaviour/playdirection', [1]);
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity', [0.75]);
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size/behaviour/playdirection', [1]);
#   op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size', [0.5]);
#   return;

# controls = {
#   1: [
#       circle_init,
#       circle_inward, circle_inward, circle_inward,
#       circle_outward, circle_outward, circle_outward,
#       circle_rotate, circle_rotate
#      ]
# }


def onOffToOn(channel, sampleIndex, val, prev):
  is_on = 1 - int(val)
  # print("offToOn index:" + str(channel.index) + " (" + channel.name + ")" + str(val))
  my_controls_dynamic = mod('ocean').controls

  ctrlname = channel.name[:4]
  if ctrlname == 'butt':
    # get the control id
    # assume it's named 'button1' etc... or things will break
    controlid = int(channel.name[6:]) - 1;
    # print("eg: " + str(eg) + ", controlid: " + str(controlid))
    try:
      column = my_controls_dynamic[eg]['column']
      my_controls_dynamic[eg]['buttons'][controlid][is_on](column=column)
    except (IndexError, KeyError):
      pass
    # if eg in my_controls_dynamic and controlid in my_controls_dynamic[eg]['buttons']:
    #   print("tryin")
  if ctrlname == 'puls' and val == 1:
    # print("got a hit!")
    try:
      my_controls_dynamic[eg]['pulse']()
    except (IndexError, KeyError):
      pass

  return

# def whileOn(channel, sampleIndex, val, prev):
#   return

onOnToOff = onOffToOn

# def whileOff(channel, sampleIndex, val, prev):
#   return

def onValueChange(channel, sampleIndex, val, prev):
  # print("onValueChange:" + str(channel.index) +
  #       " (" + channel.name + ")" + str(val))
  # expecting this to be effects group, otherwise use the on/offs to handle.
  # @todo might be different when we add knobs
  if channel.name[:4] == 'knob':
    my_controls_dynamic = mod('ocean').controls
    # knob 0 or 1
    controlid = int(channel.name[4:]) - 1
    print('lookin for knob:', controlid)
    try:
      my_controls_dynamic[eg]['knobs'][controlid](
          val=val, 
          column=my_controls_dynamic[eg]['column']
      )
    except (IndexError, KeyError):
      pass

  if channel.name == 'effects_group':
    onEffectsGroupUpdate(int(val))
    return
  # if channel.name == 'bg':
  #   onBGUpdate(int(val))
  #   return
  return

def onEffectsGroupUpdate(val):
  global eg
  # if val not in my_controls:
  #   print(str(val) + " does not exist in controls array yet");
  #   return;

  # me.store('eg', val)
  eg = val

  column = mod('ocean').controls[val]['column']
  print("using column", column)

  try:
    mod('ocean').controls[val]['init'](column)
    print("called init OK")
  except (IndexError, KeyError):
    pass
  
  # print("effects group changed to " + str(val));
  return

# def onBGUpdate(idx):
#   target = mod('ocean').controls['bg_offset'] + idx
#   # print("updating bg")
#   simple_bg_update(target)
#   return
