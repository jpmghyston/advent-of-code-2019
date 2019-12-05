memory = [int(num) for num in open("input.txt", "r").readline().split(',')]

inputs = [1]

pointer = 0


def multiply(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    memory[memory[pointer + 3]] = param_1 * param_2


def add(parameter_modes):
    param_1, param_2 = get_parameters(parameter_modes)
    memory[memory[pointer + 3]] = param_1 + param_2


def output():
    print memory[memory[pointer + 1]], pointer

def input():
    location_to_put_input = memory[pointer + 1]
    memory[location_to_put_input] = inputs.pop()


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
# print pointer
# print memory