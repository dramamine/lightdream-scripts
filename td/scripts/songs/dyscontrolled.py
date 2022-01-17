intro = {'bg_column': 1, 'pulse_toggle_on_load': True, 'resync': True}
pre_build = {'bg_column': 2, 'pulse_clear': True, 'resync': True}
build_a = {'bg_column': 3, 'pulse_toggle_on_load': True}
build_b = {'bg_column': 4, 'pulse_toggle_on_load': True}
build_dropout = {'bg_column': 5}
psy_a = {'bg_column': 6, 'pulse_toggle_on_load': True}
psy_b = {'bg_column': 7, 'pulse_toggle_on_load': True}
psy_c = {'bg_column': 8, 'pulse_toggle_on_load': True}
drop_w_big_hit = {'bg_column': 9}
drop_galaxy = {'bg_column': 10, 'resync': True}
wild_a = {'bg_column': 11, 'pulse_toggle_on_load': True, 'resync': True}
wild_b = {'bg_column': 12, 'pulse_toggle_on_load': True}
trills_a = {'bg_column': 13, 'pulse_toggle_on_load': True}
trills_b = {'bg_column': 14, 'pulse_toggle_on_load': True}
quiet = {'bg_column': 15, 'pulse_clear': True}
electro = {'bg_column': 16}
fade = {'bg_column': 17}
chorus_a = {'bg_column': 18, 'pulse_toggle_on_load': True}
chorus_a_prime = {'bg_column': 19, 'pulse_toggle_on_load': True}
chorus_b = {'bg_column': 20, 'pulse_toggle_on_load': True}
chorus_b_var = {'bg_column': 21,
                'pulse_toggle_on_load': True, 'transition_time': 0.1}
trans = {'bg_column': 22, 'transition_time': 0}
payoff = {'bg_column': 23}
outro = {'bg_column': 24}
end = {'bg_column': 25}


end = {'bg_column': 13, 'pulse_clear': True}

controls = [
    None, 
    intro, pre_build,
    build_a, build_b, build_dropout,
    psy_a, drop_w_big_hit, psy_a,
    psy_b, drop_w_big_hit, psy_b,
    psy_c, drop_galaxy,
    wild_a, 
    wild_b, drop_w_big_hit,
    trills_a, drop_w_big_hit,
    quiet, electro,
    trills_a, trills_b,
    fade,
    chorus_a, chorus_a_prime,
    chorus_b, chorus_b_var, chorus_b, chorus_b_var, chorus_b,
    trans,
    payoff, drop_w_big_hit,
    trills_a, 
    outro, end
]
