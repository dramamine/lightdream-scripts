import effects

intro = {'bg_column': 1, 'resync': True}
buildup = {'bg_column': 2}
redlips_always_lie = {'bg_column': 3}
drop_a = {'bg_column': 4}
drop_b = {'bg_column': 5}
drop_c = {'bg_column': 6}
drop_d = {'bg_column': 7}
drop_wonk = {'bg_column': 8}
stealthy_prize = {'bg_column': 9}
dontlet = {'bg_column': 10}
quiet = {'bg_column': 11}
skreech_a = {'bg_column': 12, 'pulse_clear': True}
skreech_b = {'bg_column': 13}
outro_a = {'bg_column': 14}
outro_b = {'bg_column': 15}
end = {'bg_column': 16, 'pulse_clear': True}

controls = [ 
    effects.clear, intro, buildup, redlips_always_lie, 
    drop_a, drop_wonk, drop_a, stealthy_prize, 
    drop_b, drop_wonk, drop_b, stealthy_prize, 
    
    dontlet, quiet, buildup, redlips_always_lie, 
    
    drop_c, skreech_a, drop_c, skreech_a, 
    drop_c, skreech_a, stealthy_prize, drop_c, skreech_b, 
    drop_c, skreech_b, drop_d, stealthy_prize, 
    
    outro_a, outro_b, end
]
