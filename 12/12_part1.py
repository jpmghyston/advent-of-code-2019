import re
from itertools import combinations


class Moon():
    def __init__(self, x, y, z):
        self.x, self.initial_x = x, x
        self.y, self.initial_y = y, y
        self.z, self.initial_z = z, z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    @staticmethod
    def velocity_change(own_pos, other_pos):
        if own_pos > other_pos:
            return -1
        elif own_pos < other_pos:
            return 1
        else:
            return 0

    def update_velocity(self, other_moon):
        self.vel_x += self.velocity_change(self.x, other_moon.x)
        self.vel_y += self.velocity_change(self.y, other_moon.y)
        self.vel_z += self.velocity_change(self.z, other_moon.z)

    def update_position(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def in_same_position_as_initial(self):
        return self.total_energy() == 0 and self.x == self.initial_x and self.y == self.initial_y and self.z == self.initial_z

    def print_position(self):
        print "pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(self.x, self.y, self.z, self.vel_x, self.vel_y,
                                                                      self.vel_z)

    def total_energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z))


moons = [Moon(int(match.group(1)), int(match.group(2)), int(match.group(3))) for match in
         [re.search('x=([-\d]+), y=([-\d]+), z=([-\d]+)', line) for line in [line for line in open("input.txt", "r")]]]
moon_pairs = list(combinations(moons, 2))

for i in range(100):
    # for moon in moons:
    #     moon.print_position()
    for moon_a, moon_b in moon_pairs:
        moon_a.update_velocity(moon_b)
        moon_b.update_velocity(moon_a)
    for moon in moons:
        moon.update_position()
    if all(map(lambda x: x.in_same_position_as_initial(), moons)):
        break
    else:
        i += 1


print i
