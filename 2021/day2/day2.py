def part1(instructions: list[list[str | int]]):
    pos = [0, 0]

    for instr in instructions:
        match instr:
            case ['forward', x]:
                pos[0] += x
            case ['down', x]:
                pos[1] += x
            case ['up', x]:
                pos[1] -= x

    print('Part 1:', pos[0] * pos[1])


def part2(instructions: list[list[str | int]]):
    pos = [0, 0, 0]

    for instr in instructions:
        match instr:
            case ['forward', x]:
                pos[0] += x
                pos[1] += pos[2] * x
            case ['down', x]:
                pos[2] += x
            case ['up', x]:
                pos[2] -= x

    print('Part 2:', pos[0] * pos[1])


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    instructions = [[line.split()[0], int(line.split()[1])] for line in lines]

    part1(instructions)
    part2(instructions)
