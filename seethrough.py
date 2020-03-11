from functools import partial
from utils import send
def rings_init():
  send('/composition/layers/2/clips/1/connect', 1.0);
  return;

def rings0():
  print("rings0 called");
  op('resolume').sendOSC('/composition/layers/2/clips/1/connect', [1.0]);
  return

def rings_on(idx):
  send('/composition/layers/'+str(idx)+'/clips/1/connect', 1.0)
  return

def rings_off(idx):
  print("off called!!")
  op('resolume').sendOSC('/composition/layers/'+str(idx)+'/clips/1/connect', [0.0])
  return

def rings_hue(val):
  send('/composition/layers/2/clips/1/video/effects/huerotate/effect/huerotate', val)
  return

def rings_contrast(val):
  # the range gets converted from 0.0-1.0 to  -1.0-1.0, but we only want positive contrast
  send('/composition/layers/2/clips/1/video/effects/brightnesscontrast/effect/contrast', 
      0.5 + val/2)
  return

controls = {
  1: {
    'init': rings_init,
    'buttons': [
        [partial(rings_on, idx=3)],
        [partial(rings_on, idx=4)],
        [partial(rings_on, idx=5)],
        [],
        [],
        []
    ],
    'knobs': [rings_hue, rings_contrast]
  }
}

print("seethrough loaded!");
