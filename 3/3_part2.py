input_file = open("input.txt", "r")

path_directions_1 = input_file.readline().strip().split(',')
path_directions_2 = input_file.readline().strip().split(',')


def coords_for_path(path):
    _x = 0
    _y = 0
    path_coords_visited = []
    for instruction in path:
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == "R":
            path_coords_visited += [(new_x, _y) for new_x in range(_x, _x + distance)]
            _x += abs(distance)
        elif direction == "L":
            path_coords_visited += [(new_x, _y) for new_x in range(_x, _x - distance, -1)]
            _x -= abs(distance)
        elif direction == "U":
            path_coords_visited += [(_x, new_y) for new_y in range(_y, _y + distance)]
            _y += abs(distance)
        elif direction == "D":
            path_coords_visited += [(_x, new_y) for new_y in range(_y, _y - distance, -1)]
            _y -= abs(distance)
    return path_coords_visited


def distance_to_point(path, point):
    distance = 1
    for i in range(1, len(path)):
        new_location = path[i]
        if new_location == point:
            return distance
        x, y = new_location
        old_x, old_y = path[i - 1]
        distance += abs(x - old_x) + abs(y - old_y)


path_1 = coords_for_path(path_directions_1)
path_2 = coords_for_path(path_directions_2)

crosses = set(path_1).intersection(set(path_2))
crosses.remove((0, 0))

distances_to_crosses = [distance_to_point(path_1, cross) + distance_to_point(path_2, cross) for cross in crosses]
distances_to_crosses.sort()
print distances_to_crosses


