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

controls = {
    0: effects.clear,
    1: intro,
    2: buildup,
    3: redlips_always_lie,
    4: drop_a,
    5: drop_wonk,
    6: drop_a,
    7: stealthy_prize,
    8: drop_b,
    9: drop_wonk,
    10: drop_b,
    11: stealthy_prize,
    12: dontlet,
    13: quiet,
    14: buildup,
    15: redlips_always_lie,
    16: drop_c,
    17: skreech_a,
    18: drop_c,
    19: skreech_a,
    20: drop_c,
    21: skreech_a,
    22: stealthy_prize,
    23: drop_c,
    24: skreech_b,
    25: drop_c,
    26: skreech_b,
    27: drop_d,
    28: stealthy_prize,
    29: outro_a,
    30: outro_b,
    31: end
}
