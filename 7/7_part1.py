import functools

class Computer():
    def __init__(self, valve_setting):
        self.memory = [int(num) for num in open("input.txt", "r").readline().split(',')]
        self.pointer = 0
        self.inputs = [valve_setting]

    def multiply(self, parameter_modes):
        param_1, param_2 = self.get_parameters(parameter_modes)
        self.memory[self.memory[self.pointer + 3]] = param_1 * param_2

    def add(self, parameter_modes):
        param_1, param_2 = self.get_parameters(parameter_modes)
        self.memory[self.memory[self.pointer + 3]] = param_1 + param_2

    def output(self):
        self.output_value = self.memory[self.memory[self.pointer + 1]]

    def input(self):
        location_to_put_input = self.memory[self.pointer + 1]
        self.memory[location_to_put_input] = self.inputs.pop()

    def jump_if_true(self, parameter_modes):
        param_1, param_2 = self.get_parameters(parameter_modes)
        if param_1 != 0:
            return param_2
        return self.pointer + 3

    def jump_if_false(self, parameter_modes):
        param_1, param_2 = self.get_parameters(parameter_modes)
        if param_1 == 0:
            return param_2
        return self.pointer + 3

    def less_than(self, parameter_modes):
        param_1, param_2 = self.get_parameters(parameter_modes)
        if param_1 < param_2:
            self.memory[self.memory[self.pointer + 3]] = 1
        else:
            self.memory[self.memory[self.pointer + 3]] = 0
        return self.pointer + 4

    def equal_to(self, parameter_modes):
        param_1, param_2 = self.get_parameters(parameter_modes)
        if param_1 == param_2:
            self.memory[self.memory[self.pointer + 3]] = 1
        else:
            self.memory[self.memory[self.pointer + 3]] = 0
        return self.pointer + 4

    def get_parameters(self, parameter_modes):
        param_1 = self.memory[self.pointer + 1] if parameter_modes[0] == 1 else self.memory[self.memory[self.pointer + 1]]
        param_2 = self.memory[self.pointer + 2] if parameter_modes[1] == 1 else self.memory[self.memory[self.pointer + 2]]
        return param_1, param_2

    def run_program(self, input_value):
        self.inputs.append(input_value)
        while self.memory[self.pointer] != 99:
            instruction = str(self.memory[self.pointer]).zfill(5)
            opcode = int(instruction[-2:])
            param_modes = [int(d) for d in instruction[:3]]
            param_modes.reverse()
            if opcode == 1:
                self.add(param_modes)
                self.pointer += 4
            elif opcode == 2:
                self.multiply(param_modes)
                self.pointer += 4
            elif opcode == 3:
                self.input()
                self.pointer += 2
            elif opcode == 4:
                return self.output()
            elif opcode == 5:
                self.pointer = self.jump_if_true(param_modes)
            elif opcode == 6:
                self.pointer = self.jump_if_false(param_modes)
            elif opcode == 7:
                self.pointer = self.less_than(param_modes)
            elif opcode == 8:
                self.pointer = self.equal_to(param_modes)
        return self.output_value


possible_valve_settings = [[a, b, c, d, e]
                           for a in range(5)
                           for b in range(5)
                           for c in range(5)
                           for d in range(5)
                           for e in range(5)]

print len(possible_valve_settings)

outputs = []

for setting in possible_valve_settings:
    computers = [Computer(valve_value) for valve_value in setting]
    output = functools.reduce(lambda value, computer: computer.run_program(value), computers, 0)
    outputs.append(output)
