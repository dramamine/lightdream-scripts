import effects

intro_a = {'bg_column': 1, 'resync': True}
intro_shift = {'bg_column': 2}
intro_b = {'bg_column': 3}
buildup_a = {'bg_column': 4}  # @TODO add bass hits
buildup_b = {'bg_column': 5}
pre_drop_a = {'bg_column': 6, 'resync': True}
pre_drop_b = {'bg_column': 7, 'resync': True}
drop_a = {'bg_column': 8}
drop_b = {'bg_column': 9}

# @TODO this one was special - maybe add bright/contrast to bg layer
drop_end = {'bg_column': 10}
mid = {'bg_column': 11}
bridge_a = {'bg_column': 12}
bridge_b = {'bg_column': 13}
end = {'bg_column': 14}

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
