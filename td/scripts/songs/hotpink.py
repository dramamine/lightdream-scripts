import effects

verse_a = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
verse_a_prime = {'bg_column': 2}
verse_b = {'bg_column': 3}
verse_b_prime = {'bg_column': 4}
prechorus = {'bg_column': 5}
chorus_a = {'bg_column': 6}
chorus_a_prime = {'bg_column': 7}
chorus_b = {'bg_column': 8}
chorus_b_prime = {'bg_column': 9}
chorus_c = {'bg_column': 10}
chorus_c_prime = {'bg_column': 11}
bridge_a = {'bg_column': 12}
bridge_a_prime = {'bg_column': 13}
bridge_b = {'bg_column': 14}
bridge_b_prime = {'bg_column': 15}
outro = {'bg_column': 16}
end = {'bg_column': 17}

controls = [
    effects.blank, verse_a, verse_a_prime,
    verse_b, verse_b_prime,
    prechorus, chorus_a, chorus_a_prime, 
    bridge_a, bridge_a_prime, bridge_b, bridge_b_prime,
    chorus_a, chorus_a_prime, chorus_b, chorus_b_prime, 
    chorus_c, chorus_c_prime, outro, end
]
