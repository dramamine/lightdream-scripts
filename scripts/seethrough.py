from functools import partial
from utils import send, simple_effects_hit, dashboardKnobPre1, dashboardKnobPre2, opacity_piano_on, opacity_piano_off, clip_piano_on, clip_piano_off

## sections:
# intro
# intro b
# pre-verse
# verse a
# verse b
# verse a
# verse b
# pre-chorus
# RIGHT before chorus
# chorus a
# chorus b
# chorus a
# chorus b
# post-chorus a
# post-chorus b
# end riff a
# end-riff b
# end


def clear():
  send('/composition/layers/2/clear', 1)
  send('/composition/layers/3/clear', 1)
  send('/composition/layers/4/clear', 1)
  send('/composition/layers/5/clear', 1)
  send('/composition/layers/6/clear', 1)
  send('/composition/layers/7/clear', 1)
  send('/composition/layers/2/clear', 0)
  send('/composition/layers/3/clear', 0)
  send('/composition/layers/4/clear', 0)
  send('/composition/layers/5/clear', 0)
  send('/composition/layers/6/clear', 0)
  send('/composition/layers/7/clear', 0)
  return

def rings_init():
  print('rings init')
  send('/composition/layers/2/clips/1/connect', 1)
  return

def bolts_init():
  send('/composition/layers/2/clips/2/connect', 1)

  send('/composition/layers/3/clips/2/video/opacity/behaviour/playdirection', 2)
  send('/composition/layers/4/clips/2/video/opacity/behaviour/playdirection', 2)
  send('/composition/layers/5/clips/2/video/opacity/behaviour/playdirection', 2)
  send('/composition/layers/6/clips/2/video/opacity/behaviour/playdirection', 2)
  send('/composition/layers/7/clips/2/video/opacity/behaviour/playdirection', 2)

  send('/composition/layers/3/clips/2/video/opacity', 0.0)
  send('/composition/layers/4/clips/2/video/opacity', 0.0)
  send('/composition/layers/5/clips/2/video/opacity', 0.0)
  send('/composition/layers/6/clips/2/video/opacity', 0.0)
  send('/composition/layers/7/clips/2/video/opacity', 0.0)

  send('/composition/layers/3/clips/2/connect', 1)
  send('/composition/layers/4/clips/2/connect', 1)
  send('/composition/layers/5/clips/2/connect', 1)
  send('/composition/layers/6/clips/2/connect', 1)
  send('/composition/layers/7/clips/2/connect', 1)

  return

def lasers_init():
  clear()
  send('/composition/layers/2/clips/3/connect', 1)
  return

# set to 1 as long as button is pressed
def bolts_on(idx):
  send('/composition/layers/'+str(idx)+'/clips/2/video/opacity', 1.0)
  send('/composition/layers/'+str(idx) +
       '/clips/2/video/opacity/behaviour/playdirection', 2)
  return

# let it fade out
def bolts_off(idx):
  send('/composition/layers/'+str(idx) +
       '/clips/2/video/opacity/behaviour/playdirection', 0)
  return

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

eg = me.fetch('eg', 0)

controls = {
  'bg_offset': 0,
  0: {
    'column': 0,  # intro A
    'init': clear,
    'pulse': partial(simple_effects_hit, column=0, layer=6),
    'buttons': [
      [partial(simple_effects_hit, layer=0)],
      [partial(simple_effects_hit, layer=1)],
      [partial(simple_effects_hit, layer=2)],
      [partial(simple_effects_hit, layer=3)],
      [partial(simple_effects_hit, layer=4)],
      [partial(simple_effects_hit, layer=5)],
    ],
    'knobs': [dashboardKnobPre1, dashboardKnobPre2]
  },
  3: {
    'column': 4,  # pre-verse
    'init': None,
    'buttons': [
        [partial(clip_piano_on, layer=0), partial(clip_piano_off, layer=0)],
        [partial(clip_piano_on, layer=1), partial(clip_piano_off, layer=1)],
        [partial(clip_piano_on, layer=2), partial(clip_piano_off, layer=2)],
        [partial(clip_piano_on, layer=3), partial(clip_piano_off, layer=3)],
        [partial(clip_piano_on, layer=4), partial(clip_piano_off, layer=4)],
        [partial(clip_piano_on, layer=5), partial(clip_piano_off, layer=5)],
    ]
  },
  4: {
    'column': 5,  # pre-chorus
    'init': None,
    'buttons': [
        [partial(opacity_piano_on, layer=0), partial(opacity_piano_off, layer=0)],
        [partial(opacity_piano_on, layer=1), partial(opacity_piano_off, layer=1)],
        [partial(opacity_piano_on, layer=2), partial(opacity_piano_off, layer=2)],
        [partial(opacity_piano_on, layer=3), partial(opacity_piano_off, layer=3)],
        [partial(opacity_piano_on, layer=4), partial(opacity_piano_off, layer=4)],
        [partial(opacity_piano_on, layer=5), partial(opacity_piano_off, layer=5)],
    ]
  }
}

# print("seethrough loaded!!");
