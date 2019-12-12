import re
from itertools import combinations

X = 0
Y = 1
Z = 2

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

    def in_initial_position(self):
        return self.total_energy() == 0 and self.x == self.initial_x and self.y == self.initial_y and self.z == self.initial_z

    def back_at_start_in_axis(self, axis):
        if axis == X:
            return self.x == self.initial_x and self.vel_x == 0
        elif axis == Y:
            return self.y == self.initial_y and self.vel_y == 0
        else:
            return self.z == self.initial_z and self.vel_z == 0

    def total_energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z))


moons = [Moon(int(match.group(1)), int(match.group(2)), int(match.group(3))) for match in
         [re.search('x=([-\d]+), y=([-\d]+), z=([-\d]+)', line) for line in [line for line in open("input.txt", "r")]]]
moon_pairs = list(combinations(moons, 2))

axis_numbers = [None, None, None]

i = 0

while True:
    # for moon in moons:
    #     moon.print_position()
    for moon_a, moon_b in moon_pairs:
        moon_a.update_velocity(moon_b)
        moon_b.update_velocity(moon_a)
    for moon in moons:
        moon.update_position()
    for axis in [X, Y, Z]:
        if axis_numbers[axis] is None and all(map(lambda x: x.back_at_start_in_axis(axis), moons)):
            axis_numbers[axis] = i + 1
    if all(map(lambda axis_number: axis_number is not None, axis_numbers)):
        break
    else:
        i += 1

print "Answer is the lowest common multiple of:"
print axis_numbers
