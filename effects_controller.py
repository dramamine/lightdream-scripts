# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.
eg = me.fetch('eg', 0);
import seethrough
my_controls = seethrough.controls
print("hi from file")

def circle_init():
  print("initializing controls");
  op('resolume').sendOSC('/composition/layers/2/clips/2/connect', [1.0]);
  op('resolume').sendOSC('/composition/layers/2/video/effects/circles/opacity', [0.0]);
  return


def circle_rotate(val):
  return;


def circle_inward():
  print("circling inward");
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity/behaviour/playdirection', [0]);
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity', [0.8]);
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size/behaviour/playdirection', [0]);
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size', [1.0]);
  return;


def circle_outward():
  print("circling outward");
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity/behaviour/playdirection', [1]);
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/opacity', [0.75]);
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size/behaviour/playdirection', [1]);
  op('resolume').sendOSC('/composition/layers/2/clips/2/video/effects/circles/effect/size', [0.5]);
  return;

controls = {
  1: [
      circle_init,
      circle_inward, circle_inward, circle_inward,
      circle_outward, circle_outward, circle_outward,
      circle_rotate, circle_rotate
     ]
}


def onOffToOn(channel, sampleIndex, val, prev):
  is_on = 1 - int(val)
  print("offToOn index:" + str(channel.index) + " (" + channel.name + ")" + str(val))
  my_controls_dynamic = mod('seethrough').controls

  ctrlname = channel.name[:4]
  if ctrlname == 'butt':
    # get the control id
    # assume it's named 'button1' etc... or things will break
    controlid = int(channel.name[6:]) - 1;
    print("eg: " + str(eg) + ", controlid: " + str(controlid))
    try:
      my_controls_dynamic[eg]['buttons'][controlid][is_on]()
    except (IndexError, KeyError):
      pass
    # if eg in my_controls_dynamic and controlid in my_controls_dynamic[eg]['buttons']:
    #   print("tryin")

  return

# def whileOn(channel, sampleIndex, val, prev):
#   return

onOnToOff = onOffToOn

# def whileOff(channel, sampleIndex, val, prev):
#   return

def onValueChange(channel, sampleIndex, val, prev):
  # expecting this to be effects group, otherwise use the on/offs to handle.
  # @todo might be different when we add knobs
  if channel.name[:4] == 'knob':
    my_controls_dynamic = mod('seethrough').controls
    controlid = int(channel.name[4:]) - 1
    # print('lookin for knob:', controlid)
    try:
      my_controls_dynamic[eg]['knobs'][controlid](val=val)
    except (IndexError, KeyError):
      pass

  if channel.name == 'effects_group':
    onEffectsGroupUpdate(int(val))
    return
  return

def onEffectsGroupUpdate(val):
  if val not in controls:
    print(str(val) + "does not exist in controls array yet");
    return;

  me.store('eg', val);

  controls[val][0]();

  print("effects group changed to " + str(val));
  return
