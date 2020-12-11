import copy


def part1(lines):
    lines = [list(line) for line in lines]

    lines = move_around(lines)
    state1 = flatten_lines(lines)

    lines = move_around(lines)
    state2 = flatten_lines(lines)

    while state1 != state2:
        lines = move_around(lines)
        state1 = flatten_lines(lines)
        lines = move_around(lines)
        state2 = flatten_lines(lines)

    print(state1.count('#'))


def move_around(lines):
    lines_new = copy.deepcopy(lines)
    for row in range(len(lines)):
        for column in range(len(lines[0])):
            if lines[row][column] == '.':
                continue
            nr_occupied = get_count_occupied(row, column, lines)
            if lines[row][column] == 'L' and nr_occupied == 0:
                lines_new[row][column] = '#'
            elif lines[row][column] == '#' and nr_occupied >= 4:
                lines_new[row][column] = 'L'
    return lines_new


def move_around_p2(lines):
    lines_new = copy.deepcopy(lines)
    for row in range(len(lines)):
        for column in range(len(lines[0])):
            if lines[row][column] == '.':
                continue
            nr_occupied = get_count_occupied_p2(row, column, lines)
            if lines[row][column] == 'L' and nr_occupied == 0:
                lines_new[row][column] = '#'
            elif lines[row][column] == '#' and nr_occupied >= 5:
                lines_new[row][column] = 'L'
    return lines_new


def get_count_occupied(row, column, lines):
    count = 0
    count += count_spot(row, column, lines, -1, -1)
    count += count_spot(row, column, lines, 0, -1)
    count += count_spot(row, column, lines, 1, -1)
    count += count_spot(row, column, lines, -1, 0)
    count += count_spot(row, column, lines, 1, 0)
    count += count_spot(row, column, lines, -1, 1)
    count += count_spot(row, column, lines, 0, 1)
    count += count_spot(row, column, lines, 1, 1)
    return count


def get_count_occupied_p2(row, column, lines):
    count = 0
    count += count_spot_p2(row, column, lines, -1, -1)
    count += count_spot_p2(row, column, lines, 0, -1)
    count += count_spot_p2(row, column, lines, 1, -1)
    count += count_spot_p2(row, column, lines, -1, 0)
    count += count_spot_p2(row, column, lines, 1, 0)
    count += count_spot_p2(row, column, lines, -1, 1)
    count += count_spot_p2(row, column, lines, 0, 1)
    count += count_spot_p2(row, column, lines, 1, 1)
    return count


def count_spot(row, column, lines, dx, dy):
    if 0 <= row + dy < len(lines) and 0 <= column + dx < len(lines[0]) and lines[row + dy][column + dx] == '#':
        return 1
    return 0


def count_spot_p2(row, column, lines, dx, dy):
    if 0 <= row + dy < len(lines) and 0 <= column + dx < len(lines[0]):
        if lines[row + dy][column + dx] == '#':
            return 1
        elif lines[row + dy][column + dx] == '.':
            return count_spot_p2(row, column, lines, get_new_d_p2(dx), get_new_d_p2(dy))
    return 0


def get_new_d_p2(d):
    if d == 0:
        return 0
    elif d > 0:
        return d + 1
    elif d < 0:
        return d - 1


def flatten_lines(lines):
    return ''.join([''.join(line) for line in lines])


def part2(lines):
    lines = [list(line) for line in lines]

    lines = move_around_p2(lines)
    state1 = flatten_lines(lines)

    lines = move_around_p2(lines)
    state2 = flatten_lines(lines)

    while state1 != state2:
        lines = move_around_p2(lines)
        state1 = flatten_lines(lines)
        lines = move_around_p2(lines)
        state2 = flatten_lines(lines)

    print(state1.count('#'))


def main():
    with open('in.txt') as file:
        lines = file.read().splitlines()

    part1(lines)
    part2(lines)


if __name__ == '__main__':
    main()
