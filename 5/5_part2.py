memory = [int(num) for num in open("input2.txt", "r").readline().split(',')]

inputs = [5]

pointer = 0


def multiply(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    memory[memory[pointer + 3]] = param_1 * param_2


def add(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    memory[memory[pointer + 3]] = param_1 + param_2


def output():
    print memory[memory[pointer + 1]]


def input():
    location_to_put_input = memory[pointer + 1]
    memory[location_to_put_input] = inputs.pop()


def jump_if_true(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    if param_1 != 0:
        return param_2
    return pointer + 3


def jump_if_false(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    if param_1 == 0:
        return param_2
    return pointer + 3


def less_than(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    if param_1 < param_2:
        memory[memory[pointer + 3]] = 1
    else:
        memory[memory[pointer + 3]] = 0
    return pointer + 4


def equal_to(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    if param_1 == param_2:
        memory[memory[pointer + 3]] = 1
    else:
        memory[memory[pointer + 3]] = 0
    return pointer + 4

def get_parameters(parameter_modes):
    param_1 = memory[pointer + 1] if parameter_modes[0] == 1 else memory[memory[pointer + 1]]
    param_2 = memory[pointer + 2] if parameter_modes[1] == 1 else memory[memory[pointer + 2]]
    return param_1, param_2

while memory[pointer] != 99:
    # print pointer
    # print memory
    instruction = str(memory[pointer]).zfill(5)
    opcode = int(instruction[-2:])
    param_modes = [int(d) for d in instruction[:3]]
    param_modes.reverse()
    if opcode == 1:
        add(param_modes)
        pointer += 4
    elif opcode == 2:
        multiply(param_modes)
        pointer += 4
    elif opcode == 3:
        input()
        pointer += 2
    elif opcode == 4:
        output()
        pointer += 2
    elif opcode == 5:
        pointer = jump_if_true(param_modes)
    elif opcode == 6:
        pointer = jump_if_false(param_modes)
    elif opcode == 7:
        pointer = less_than(param_modes)
    elif opcode == 8:
        pointer = equal_to(param_modes)

# print pointer
# print memory