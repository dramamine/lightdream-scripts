from resolume_commands import pulse_clear_init
import effects

intro = {**effects.heatinvert, 'bg_column': 1,} 
buildup = {**effects.heatinvert, 'bg_column': 2, }
redlips_always_lie = {**effects.heatinvert, 'bg_column': 3, }
drop_a = {**effects.heatinvert, 'bg_column': 4, }
drop_b = {**effects.heatinvert, 'bg_column': 5, }
drop_c = {**effects.heatinvert, 'bg_column': 6, }
drop_d = {**effects.heatinvert, 'bg_column': 7, }
drop_wonk = {**effects.heatinvert, 'bg_column': 8, }
stealthy_prize = {**effects.heatinvert, 'bg_column': 9, }
dontlet = {**effects.heatinvert, 'bg_column': 10, }
quiet = {**effects.heatinvert, 'bg_column': 11, }
skreech_a = {**effects.heatinvert, 'bg_column': 12, 'init': pulse_clear_init}
skreech_b = {**effects.heatinvert, 'bg_column': 13, }
outro_a = {**effects.heatinvert, 'bg_column': 14, }
outro_b = {**effects.heatinvert, 'bg_column': 15, }
end = {**effects.heatinvert, 'bg_column': 16, 'init': pulse_clear_init}

controls = [ 
    effects.clear, intro, buildup, redlips_always_lie, 
    drop_a, drop_wonk, drop_a, stealthy_prize, 
    drop_b, drop_wonk, drop_b, stealthy_prize, 
    
    dontlet, quiet, buildup, redlips_always_lie, 
    
    drop_c, skreech_a, drop_c, skreech_a, 
    drop_c, skreech_a, stealthy_prize, drop_c, skreech_b, 
    drop_c, skreech_b, drop_d, stealthy_prize, 
    
    outro_a, outro_b, end
}
