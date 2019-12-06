def find_orbit_depth(planet, orbits, orbit_depth = 0):
    for orbit in orbits:
        if orbit[1] == planet:
            return find_orbit_depth(orbit[0], orbits, orbit_depth + 1)
    return orbit_depth

orbits = [x.strip().split(')') for x in open('input.txt', 'r')]

all_planets = set()

for orbit in orbits:
    for planet in orbit:
        all_planets.add(planet)

total_orbit_depth = 0
for planet in all_planets:
    total_orbit_depth += find_orbit_depth(planet, orbits)

print total_orbit_depth
