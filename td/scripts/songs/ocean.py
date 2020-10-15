import effects

intro_a = {**effects.php, 'bg_column': 1}

intro_shift = {**effects.php, 'bg_column': 2}

intro_b = {**effects.php, 'bg_column': 3}

buildup_a = {**effects.rm, 'bg_column': 4}  # @TODO add bass hits
buildup_b = {**effects.rm, 'bg_column': 5}

pre_drop_a = {**effects.blank, 'bg_column': 6, 'resync': True}
pre_drop_b = {**effects.blank, 'bg_column': 7, 'resync': True}

drop_a = {**effects.eagle_spreader_inverter, 'bg_column': 8}
drop_b = {**effects.eagle_spreader_inverter, 'bg_column': 9}

# @TODO this one was special - maybe add bright/contrast to bg layer
drop_end = {**effects.eagle_spreader_inverter, 'bg_column': 10}

mid = {**effects.blank, 'bg_column': 11}

bridge_a = {**effects.colorwheel_quiet, 'bg_column': 12}
bridge_b = {**effects.colorwheel_loud, 'bg_column': 13}
end = {**effects.blank, 'bg_column': 14}

controls = [
  effects.clear,
  intro_a, intro_shift, intro_b, intro_shift, intro_a,
  buildup_a,  # you could put an ocean
  buildup_b,  # if im caught
  pre_drop_a,  # 1 measure
  pre_drop_b,  # 1 measure
  drop_a, drop_b, drop_end,
  drop_a, drop_b, drop_end,
  mid,
  bridge_a, bridge_b,
  intro_a,  # when my echos..
  buildup_a,  # you could put  an ocean
  buildup_b,
  pre_drop_a,  # 1 measure
  pre_drop_b,  # 1 measure
  drop_a, drop_b, drop_end,
  drop_a, drop_b, drop_end,
  end
]
