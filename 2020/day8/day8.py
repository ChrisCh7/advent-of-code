import copy


def execute(instructions, index, accumulator, passed_indexes, terminated):
    if index == len(instructions):
        terminated = True
        return {'accumulator': accumulator, 'terminated': terminated}
    if index in passed_indexes:
        return {'accumulator': accumulator, 'terminated': terminated}
    if instructions[index][0] == 'nop':
        passed_indexes.append(index)
        return execute(instructions, index + 1, accumulator, passed_indexes, terminated)
    if instructions[index][0] == 'acc':
        passed_indexes.append(index)
        accumulator += int(instructions[index][1])
        return execute(instructions, index + 1, accumulator, passed_indexes, terminated)
    if instructions[index][0] == 'jmp':
        passed_indexes.append(index)
        index += int(instructions[index][1])
        return execute(instructions, index, accumulator, passed_indexes, terminated)


def part1(instructions):
    result = execute(instructions, 0, 0, [], False)
    print('Part 1:', result['accumulator'])


def part2(instructions: list):
    instr = copy.deepcopy(instructions)
    instructions_to_test = [instruction for instruction in instructions if instruction[0] in ['nop', 'jmp']]
    index_instruction_in_instructions_to_test = 0
    instruction_to_test = instructions_to_test[index_instruction_in_instructions_to_test]
    index_test = instructions.index(instruction_to_test)
    while True:
        mutate(instr, index_test)
        result = execute(instr, 0, 0, [], False)
        if result['terminated']:
            print('Part 2:', result['accumulator'])
            break
        instr = copy.deepcopy(instructions)
        index_instruction_in_instructions_to_test += 1
        instruction_to_test = instructions_to_test[index_instruction_in_instructions_to_test]
        index_test = instructions.index(instruction_to_test)


def mutate(instructions, index_test):
    instruction = instructions[index_test]
    if instruction[0] == 'nop':
        instruction[0] = 'jmp'
    else:
        instruction[0] = 'nop'


if __name__ == '__main__':
    with open('in.txt') as file:
        instructions = [line.split() for line in file.read().splitlines()]
    part1(instructions)
    part2(instructions)
