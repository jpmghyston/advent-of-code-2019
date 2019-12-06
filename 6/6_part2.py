
orbit_input = [x.strip().split(')') for x in open('input.txt', 'r')]


def find_planets_being_orbited(planet, orbits, planets=[]):
    for orbit in orbits:
        if orbit[1] == planet:
            return find_planets_being_orbited(orbit[0], orbits, planets + orbit[:1])
    return planets


def find_common_orbit_planet(orbit_1, orbit_2):
    reversed_1 = orbit_1[::-1]
    reversed_2 = orbit_2[::-1]
    i = 0
    while reversed_1[i] == reversed_2[i]:
        i += 1
    return reversed_1[i-1]


santa_orbit = find_planets_being_orbited("SAN", orbit_input)
you_orbit = find_planets_being_orbited("YOU", orbit_input)
common_planet = find_common_orbit_planet(santa_orbit, you_orbit)
transfers = santa_orbit.index(common_planet) + you_orbit.index(common_planet)
print transfers
