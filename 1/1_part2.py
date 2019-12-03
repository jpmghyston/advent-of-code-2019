input = [
    144365,
    124674,
    99039,
    132924,
    126960,
    103950,
    78451,
    123596,
    119950,
    116772,
    134137,
    50247,
    99543,
    147151,
    103063,
    59247,
    59281,
    141531,
    104417,
    75105,
    57868,
    149148,
    76973,
    87424,
    135220,
    141885,
    106241,
    128482,
    54020,
    67575,
    97719,
    110237,
    137361,
    70772,
    103397,
    117471,
    99611,
    142905,
    135345,
    122338,
    62708,
    103663,
    146189,
    81657,
    126628,
    133113,
    135399,
    52731,
    116597,
    61749,
    61519,
    56234,
    64306,
    127237,
    133320,
    79782,
    132431,
    142449,
    91926,
    146277,
    55314,
    111507,
    126347,
    124086,
    120868,
    127433,
    126838,
    77814,
    144388,
    86786,
    134780,
    109082,
    101772,
    140013,
    100282,
    115632,
    73057,
    139318,
    85633,
    67693,
    55545,
    53545,
    125871,
    115201,
    105202,
    148104,
    68677,
    64761,
    54368,
    110380,
    102082,
    106684,
    89933,
    71703,
    147332,
    99699,
    98447,
    96963,
    148686,
    92651]

def fuel_calc(mass):
    fuel = (mass / 3) - 2
    if fuel < 0:
        return 0
    return fuel

def fuel_for_module(mass):
    fuel_required = fuel_calc(mass)
    if fuel_calc(fuel_required) <= 0:
        return fuel_required
    next_fuel_needed = fuel_calc(fuel_required)
    fuel_required += next_fuel_needed
    while next_fuel_needed != 0:
        next_fuel_needed = fuel_calc(next_fuel_needed)
        fuel_required += next_fuel_needed
    return fuel_required


print fuel_calc(100756)
print fuel_for_module(100756)

print sum([fuel_for_module(x) for x in input])
