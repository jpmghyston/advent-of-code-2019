program = [1, 50, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 5, 19, 23, 2, 9, 23, 27, 1, 6, 27, 31, 1, 31, 9, 35, 2, 35, 10, 39, 1, 5, 39, 43, 2, 43, 9, 47, 1, 5, 47, 51, 1, 51, 5, 55, 1, 55, 9, 59, 2, 59, 13, 63, 1, 63, 9, 67, 1, 9, 67, 71, 2, 71, 10, 75, 1, 75, 6, 79, 2, 10, 79, 83, 1, 5, 83, 87, 2, 87, 10, 91, 1, 91, 5, 95, 1, 6, 95, 99, 2, 99, 13, 103, 1, 103, 6, 107, 1, 107, 5, 111, 2, 6, 111, 115, 1, 115, 13, 119, 1, 119, 2, 123, 1, 5, 123, 0, 99, 2, 0, 14, 0]


target = 19690720

values = [(x, y) for x in range(99) for y in range(99)]

for noun, verb in values:
    pointer = 0
    memory = program[:]
    memory[1] = noun
    memory[2] = verb
    while memory[pointer] != 99:
        opcode = memory[pointer]
        num_1 = memory[memory[pointer + 1]]
        num_2 = memory[memory[pointer + 2]]
        store_location = memory[pointer + 3]
        memory[store_location] = num_1 + num_2 if opcode == 1 else num_1 * num_2
        pointer += 4
    if memory[0] == target:
        print 100 * noun + verb

