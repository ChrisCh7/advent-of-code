def part1(dots: list[tuple[int, int]], instructions: list[list[str | int]]):
    print('Part 1:', len(fold(dots, instructions[0])))


def part2(dots: list[tuple[int, int]], instructions: list[list[str | int]]):
    for instr in instructions:
        dots = fold(dots, instr)

    width = max(dots, key=lambda d: d[0])[0] + 1
    height = max(dots, key=lambda d: d[1])[1] + 1

    print('Part 2:')

    for y in range(height):
        for x in range(width):
            print('#' if (x, y) in dots else '.', end='')
        print('\n', end='')


def fold(dots: list[tuple[int, int]], instruction: list[str | int]):
    along = instruction[0]
    n = instruction[1]

    if along == 'y':
        top = [dot for dot in dots if dot[1] < n]
        bottom = [dot for dot in dots if dot[1] > n]

        for dot in bottom:
            diff = dot[1] - n
            top.append((dot[0], n - diff))

        final_dots = top
    else:
        left = [dot for dot in dots if dot[0] < n]
        right = [dot for dot in dots if dot[0] > n]

        for dot in right:
            diff = dot[0] - n
            left.append((n - diff, dot[1]))

        final_dots = left

    return list(set(final_dots))


if __name__ == '__main__':
    with open('in.txt') as file:
        content = file.read()

    dots, instructions = content.split('\n\n')
    dots = [tuple(int(n) for n in dot.split(',')) for dot in dots.splitlines()]

    instructions = [instr.split('=') for instr in instructions.splitlines()]
    instructions = [[instr[0][-1], int(instr[1])] for instr in instructions]

    part1(dots, instructions)
    part2(dots, instructions)
