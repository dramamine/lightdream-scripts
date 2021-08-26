yep_a = {'bg_column': 1, 'pulse_clear': True,
         'resync': True}
yep_a_prime = {'bg_column': 2}
yep_a_buildup = {'bg_column': 3}
yep_b = {'bg_column': 4}
yep_b_prime = {'bg_column': 5}
clap_a = {'bg_column': 6}
clap_b = {'bg_column': 7}
yep_c = {'bg_column': 8}
yep_c_prime = {'bg_column': 9}
yep_c_buildup = {'bg_column': 10}
yep_d = {'bg_column': 11}
yep_d_prime = {'bg_column': 12}
pre_doowop = {'bg_column': 13}
doowop = {'bg_column': 14}
doowopout = {'bg_column': 15, 'pulse_toggle_on_load': True}
outro = {'bg_column': 16}

controls = [
    None,
    yep_a, yep_b,
    clap_a, clap_b,
    yep_a, yep_a_buildup,
    yep_b, yep_a_buildup,
    pre_doowop, doowop, doowopout,

    yep_c, yep_c_prime, yep_c_buildup,
    yep_d, yep_d_prime,
    yep_c, yep_c_prime,
    yep_d, yep_d_prime,

    yep_a, yep_a_prime,
    yep_b, yep_b_prime,
    yep_a, yep_a_prime,
    outro
]
