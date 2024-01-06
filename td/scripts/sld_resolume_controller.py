# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.
import sld_resolume_commands as resolume_commands
from collections import namedtuple
import random

NUM_SECTIONS = 4

LAYER_BG = 1
LAYER_MASK = 2
LAYER_TOP = 3

v = [1, 6, 11, 16]
bg_clips_by_intensity = [
  range(v[0], v[1]),
  # range(v[0], v[2]),
  range(v[1], v[2]),
  # range(v[1], v[3]),
  range(v[2], v[3]),
]

mask_clips_by_intensity = [
  range(1, 6),
  range(6, 11),
  range(11, 16),
]

top_clips_by_intensity = [
  range(1, 6),
  range(6, 11),
  range(11, 16),
]

def triple(str):
  return [str, str+"2", str+"3"]

bg_layer_effects = [
  "slide",
  "slide2",
  "slide3",
  "huerotate",
  "suckr"
]

mask_layer_effects = [
  "slide",
  "slide2",
  "slide3",
  # TODO radialmask needs to be paired with one of kaleidoscope(0-2)
  # "radialmask",
  # triple("displace"),
  # triple("distortion"),
  "trails",
  "ezradialcloner",
]

top_layer_effects = [
  "huerotate",
]

effects_by_layer = [
  bg_layer_effects,
  mask_layer_effects,
  top_layer_effects
]

IntensityTemplate = namedtuple('IntensityTemplate', [
  "active_layers",
  "clip_intensity",
  "effect_count",
  "effect_intensity"
])

intensity_templates = [
  [IntensityTemplate(1, 0, 0, 0)],
  [IntensityTemplate(2, 0, 0, 0)],
  [IntensityTemplate(2, 1, 0, 0)],
  [IntensityTemplate(2, 1, 1, 0)],

  [
    IntensityTemplate(2, 1, 1, 1),
    IntensityTemplate(2, 1, 2, 0),
    IntensityTemplate(2, 2, 1, 0),
  ],

  [
    IntensityTemplate(2, 1, 2, 1),
    IntensityTemplate(2, 2, 1, 1),
    IntensityTemplate(2, 2, 2, 0),
  ],

  [
    IntensityTemplate(2, 2, 2, 1),
  ],

  [
    IntensityTemplate(2, 2, 2, 2),
  ],

  [
    IntensityTemplate(3, 0, 1, 0),
  ],

  [
    IntensityTemplate(3, 1, 1, 0),
    IntensityTemplate(3, 0, 1, 1),
  ],

  [IntensityTemplate(3, 1, 2, 1)],
  [IntensityTemplate(3, 2, 2, 1)],
  [IntensityTemplate(3, 3, 2, 1)],
  [IntensityTemplate(3, 3, 3, 1)],
  [IntensityTemplate(3, 4, 3, 1)],
  [IntensityTemplate(3, 4, 4, 2)],
  [IntensityTemplate(3, 5, 4, 2)],
  [IntensityTemplate(3, 5, 4, 3)],
  [IntensityTemplate(3, 5, 5, 3)],
]


def divide_into_twos(num):
  if num <= 0:
    return [0, 0]
  numbers = sorted(random.sample(range(num), 1))
  bob1 = numbers[0]
  bob2 = num - numbers[0]
  return random.choice( [[bob1, bob2], [bob2, bob1]] )

def divide_into_threes(num):
  if num <= 0:
    return [0, 0, 0]
  numbers = sorted(random.sample(range(num), 2))
  bob1 = numbers[0]
  bob2 = numbers[1] - numbers[0]
  bob3 = num - numbers[1]
  return random.choice([ [bob1, bob2, bob3], [bob3, bob2, bob1] ])

def get_array_with_total(len, val, cap = None):
  res = [0] * len
  while val > 0:
    idx = random.randint(0, len - 1)
    if cap and res[idx] >= cap:
        val -=1
        continue
    res[idx] += 1
    val -= 1
  return res

def reduce_fx(fx, num):
  while (sum(fx) > num):
    idx = random.randint(0, len(fx) - 1)
    if fx[idx] > 0:
      fx[idx] -= 1
  return fx


def get_clips_intensity(active_layers, clip_intensity):
  if active_layers == 1:
    return [clip_intensity]
  if active_layers == 2:
    return divide_into_twos(clip_intensity)
  if active_layers == 3:
    return divide_into_threes(clip_intensity)

# text representation of what's going on currently with ActiveStuff.
# TODO maybe just call an op() and update its value
effects_state = ""

class ActiveStuff:
  def __init__(self, mb):
    self.mb = mb
    # fx is a list of tuples (layer, effect_name) which correspond to the OSC
    # commands used to trigger those effects
    # layer is 1-indexed
    self.fx = []
    # clips is a list of tuples (layer, clip_idx) which correspond to the OSC
    # commands used to trigger those clips.
    # layer is 1-indexed
    # clip_idx is 1-indexed
    self.clips = []

  def load(self, mb):
    self.mb = mb

  def prepare(self):
    # TODO maybe set transitions here.

    clips_intensity = get_clips_intensity(self.mb.active_layers, self.mb.clip_intensity)
    clips = []
    for i in range(self.mb.active_layers):
      idx = clips_intensity[i]
      chosen_clip = random.choice(bg_clips_by_intensity[idx])
      clips.append( (i+1, chosen_clip) )
    self.clips = clips

    # TODO intensity
    # effect_intensities = get_array_with_total(self.mb.effect_count, self.mb.effect_intensity, 2)

    fx = []
    for i in range(self.mb.effect_count):
      layer = random.randint(0, self.mb.active_layers-1)
      options = effects_by_layer[layer]
      chosen_effect = random.choice(options)
      fx.append( (layer+1, chosen_effect) )

    self.fx = fx
    return

  def activate(self):
      print("activating...")
      for c in self.clips:
        print("activate layer {} clip {}".format(c[0], c[1]))
        resolume_commands.activate_clip(c[0], c[1])
      # activate fx
      for f in self.fx:
        # TODO call resolume about this
        print("activate layer {} fx {}".format(f[0], f[1]))
        resolume_commands.activate_effect(f[0], f[1])

      self.pretty_print()
      return

  # debug string about current state of ActiveStuff
  def pretty_print(self):
    global effects_state

    mb_string = "active_layers: {}, clip_intensity: {}, effect_count: {}, effect_intensity: {}".format(
      self.mb.active_layers,
      self.mb.clip_intensity,
      self.mb.effect_count,
      self.mb.effect_intensity
    )
    clips_string = "CLIPS:" + ", ".join(["({}, {})".format(c[0], c[1]) for c in self.clips])
    fx_string = "FX:" + ", ".join(["({}, {})".format(f[0], f[1]) for f in self.fx])

    effects_state = "\n".join([mb_string, clips_string, fx_string])
    return effects_state


  def deactivate(self):
    # deactivate fx
    for f in self.fx:
      # TODO call resolume about this
      print("deactivate fx {} on layer {}".format(f[1], f[0]))
      resolume_commands.deactivate_effect(f[0], f[1])
    return

ast = ActiveStuff(IntensityTemplate(2, 0, 1, 0))

def demo_update():
  global ast
  print("demo_update called")
  # ast.load(intensity_templates[0])
  ast.deactivate()
  ast.prepare()
  ast.activate()
  return

def full_reset():
  global ast
  print("full_reset called")
  ast.deactivate()

  resolume_commands.clear()

  for i in range(0, len(effects_by_layer)):
    for effect_name in effects_by_layer[i]:
      resolume_commands.deactivate_effect(i+1, effect_name)
    # for effect_name in effects_by_layer[i]:
    #   resolume_commands.deactivate_effect(i+1, effect_name)

  return

def choose_and_activate_template(intensity):
  print("using intensity", intensity)
  # choose a pattern
  assert intensity < len(intensity_templates), "intensity out of range"
  ast.deactivate()

  pattern = random.choice(intensity_templates[intensity])
  ast.load(pattern)
  ast.prepare()
  ast.activate()
  return


# some range
intensity = 0

# section of song; 0-3
section = 0

active_template_fn = None

first_layer_ranges = {
  'light': range(1, 5)
}

transitions = []

def gradually_add_mask():
  print("gradually_add_mask called")
  if section == 0:
    # update transition
    resolume_commands.update_transition_time(LAYER_BG, 2.0)
    resolume_commands.update_blend_mode(LAYER_BG, 10)

    range = first_layer_ranges['light']
    idx = random.choice(range)
    resolume_commands.first_layer_only_instant_fadeout_others(idx)
  return



allowed_templates_by_intensity = [
  [gradually_add_mask]
]

def set_intensity(num):
  global intensity
  intensity = num
  return

def update_section(num):
  global section
  section = num
  op('section').par.Value0 = section
  return

def increment_section():
  update_section((section + 1) % NUM_SECTIONS)
  return

def choose_template():
  global active_template_fn
  choices = allowed_templates_by_intensity[intensity]
  next = random.choice(choices)
  active_template_fn = next
  op('active_template_display').par.Value0 = active_template_fn.__name__
  return

def next():
  increment_section()
  if section == 0:
    choose_template()
  if active_template_fn:
    active_template_fn()
  return

def flush():
  update_section(0)
  if active_template_fn:
    active_template_fn()

  return













print("sld_resolume_controller.py loaded.")
