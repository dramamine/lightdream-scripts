slices = {'bg_column': 1, 'pulse_clear': True, 'resync': True}
tornadoes = {'bg_column': 2, 'resync': True}
meedles = {'bg_column': 3}
hits = {'bg_column': 4, 'pulse_clear': True}
prechorus_a = {'bg_column': 5}
prechorus_b = {'bg_column': 6}
chorus_a = {'bg_column': 7}
chorus_b = {'bg_column': 8}
damn_a = {'bg_column': 9}
damn_b = {'bg_column': 10}
drums_only = {'bg_column': 11, 'pulse_toggle_on_load': True}
end = {'bg_column': 12}

controls = [
    None, 
    slices, tornadoes, slices, tornadoes,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    prechorus_a, prechorus_b,
    tornadoes, slices, tornadoes,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    prechorus_a, prechorus_b, chorus_a, chorus_b,
    damn_a, damn_b, drums_only,
    meedles, hits, meedles, hits, meedles, hits, meedles, hits,
    meedles, hits, end
]
