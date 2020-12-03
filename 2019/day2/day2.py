def run_program(program_og, noun, verb):
    program = program_og.copy()
    program[1] = noun
    program[2] = verb

    current_index = 0

    while current_index < len(program):
        value1 = program[program[current_index + 1]]
        value2 = program[program[current_index + 2]]
        result_index = program[current_index + 3]

        if program[current_index] == 1:
            program[result_index] = value1 + value2
        elif program[current_index] == 2:
            program[result_index] = value1 * value2
        elif program[current_index] == 99:
            return program

        current_index += 4


def part2(program):
    for noun in range(100):
        for verb in range(100):
            result = run_program(program, noun, verb)
            if result[0] == 19690720:
                print('noun:', noun, "verb:", verb, 'answer:', 100 * noun + verb)
                return


if __name__ == '__main__':
    with open('in.txt') as file:
        program = [int(nr) for nr in file.readline().strip().split(',')]
    program_part1 = run_program(program, 12, 2)
    print(program_part1[0])
    part2(program)
