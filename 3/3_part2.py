input_file = open("input.txt", "r")

path_1 = input_file.readline().strip().split(',')
path_2 = input_file.readline().strip().split(',')


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
        print (_x, _y)
    return path_coords_visited


coords_1 = coords_for_path(path_1)
coords_2 = coords_for_path(path_2)

crosses = set(coords_for_path(path_1)).intersection(set(coords_for_path(path_2)))
crosses.remove(0, 0)

distances = [abs(x) + abs(y) for x, y in crosses]
distances.sort()
print distances
