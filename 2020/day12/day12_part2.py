def move(instruction, x, y, w_x, w_y):
    if instruction[0] == 'N':
        w_y += instruction[1]
    if instruction[0] == 'S':
        w_y -= instruction[1]
    if instruction[0] == 'E':
        w_x += instruction[1]
    if instruction[0] == 'W':
        w_x -= instruction[1]
    if instruction[0] in ['L', 'R']:
        w_x, w_y = turn(w_x, w_y, instruction[0], instruction[1])
    if instruction[0] == 'F':
        x, y = move_forward(instruction[1], x, y, w_x, w_y)
    return x, y, w_x, w_y


def turn(w_x, w_y, direction_to_switch, degrees):
    count_direction_switches = degrees // 90
    if direction_to_switch == 'L':
        for _ in range(count_direction_switches):
            w_x, w_y = -w_y, w_x
    elif direction_to_switch == 'R':
        for _ in range(count_direction_switches):
            w_x, w_y = w_y, -w_x
    return w_x, w_y


def move_forward(value, x, y, w_x, w_y):
    return x + value * w_x, y + value * w_y


def part2(instructions):
    x = 0
    y = 0

    w_x = 10
    w_y = 1

    for instruction in instructions:
        x, y, w_x, w_y = move(instruction, x, y, w_x, w_y)

    print('Part 2:', abs(x) + abs(y))


if __name__ == '__main__':
    with open('in.txt') as file:
        instructions = [[line[0], int(line[1:])] for line in file.read().splitlines()]
    part2(instructions)
