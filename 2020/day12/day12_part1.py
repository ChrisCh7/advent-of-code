def move(instruction, x, y, direction):
    if instruction[0] == 'N':
        y += instruction[1]
    if instruction[0] == 'S':
        y -= instruction[1]
    if instruction[0] == 'E':
        x += instruction[1]
    if instruction[0] == 'W':
        x -= instruction[1]
    if instruction[0] in ['L', 'R']:
        direction = turn(direction, instruction[0], instruction[1])
    if instruction[0] == 'F':
        x, y = move_forward(direction, instruction[1], x, y)
    return x, y, direction


def turn(current_direction, direction_to_switch, degrees):
    directions = ['E', 'N', 'W', 'S']
    count_direction_switches = degrees // 90
    index_direction = directions.index(current_direction)
    if direction_to_switch == 'L':
        index_direction = (index_direction + count_direction_switches) % len(directions)
    elif direction_to_switch == 'R':
        index_direction = index_direction - count_direction_switches
    return directions[index_direction]


def move_forward(current_direction, value, x, y):
    if current_direction == 'E':
        return x + value, y
    if current_direction == 'N':
        return x, y + value
    if current_direction == 'W':
        return x - value, y
    if current_direction == 'S':
        return x, y - value


def part1(instructions):
    x = 0
    y = 0
    direction = 'E'

    for instruction in instructions:
        x, y, direction = move(instruction, x, y, direction)

    print('Part 1:', abs(x) + abs(y))


if __name__ == '__main__':
    with open('in.txt') as file:
        instructions = [[line[0], int(line[1:])] for line in file.read().splitlines()]
    part1(instructions)
