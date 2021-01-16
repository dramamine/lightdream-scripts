from resolume_commands import pulse_clear_init
import effects

intro_a = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
intro_b = {'bg_column': 2}
wubs_a = {'bg_column': 3}
wubs_b = {'bg_column': 4}
hits_a = {'bg_column': 5}
hits_b = {'bg_column': 6, 'pulse_clear': True}
hits_c = {'bg_column': 7}
hits_drumz = {'bg_column': 8}
bass_a = {'bg_column': 9, 'pulse_clear': True}
bass_b = {'bg_column': 10}
dropout = {'bg_column': 11}
wows_a = {'bg_column': 12, 'pulse_clear': True}
wows_b = {'bg_column': 13}
wows_c = {'bg_column': 14}
end = {'bg_column': 15}

controls = [
    effects.blank, 
    intro_a, intro_b,
    wubs_a, wubs_b,
    hits_a, hits_b,
    bass_a, bass_b, dropout,
    hits_a, hits_b, dropout,
    hits_c, hits_drumz,
    wows_a, wows_b, wows_c,
    intro_a, intro_b, end
]

# Aquilam Seethrough "Ocean (Goja Remix)" "Put the runes on u" "Gone For Never -Crunch Mix-" "As I Need You" "HaPPY FaSTeR" "Red Lips (Skrillex RMX)" "Girl Blunt" "Chillmode" "Hustle Bones" "Vroom Vroom" "Hot Pink" "Rage" "Nofuture"
# Aquilam Seethrough Ocean Runes Crunch Asineedyou Faster Redlips Girlblunt CHILLMODE Bones Vroom Hotpink Rage Nofuture
