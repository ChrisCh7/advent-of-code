import copy


def part1(blocked: set[tuple[int, int]], sand_source: tuple[int, int]):
    blocked = copy.deepcopy(blocked)

    flowing_into_abyss = False
    units_counter = 0
    max_y_all = max(blocked, key=lambda pos: pos[1])[1]

    while not flowing_into_abyss:
        before_move = len(blocked)
        move_sand_unit(sand_source, blocked, max_y_all)
        after_move = len(blocked)
        if before_move == after_move:
            flowing_into_abyss = True
        else:
            units_counter += 1

    print('Part 1:', units_counter)


def part2(blocked: set[tuple[int, int]], sand_source: tuple[int, int]):
    blocked = copy.deepcopy(blocked)

    source_blocked = False
    units_counter = 0
    max_y_all = max(blocked, key=lambda pos: pos[1])[1] + 2

    while not source_blocked:
        before_move = len(blocked)
        move_sand_unit(sand_source, blocked, max_y_all, 2)
        after_move = len(blocked)
        if before_move == after_move:
            source_blocked = True
        else:
            units_counter += 1

    print('Part 2:', units_counter)


def move_sand_unit(source: tuple[int, int], blocked: set[tuple[int, int]], max_y_all: int, part: int = 1):
    current_pos = source
    rest = False

    while not rest and current_pos[1] < max_y_all:
        if part == 2:
            for dx in [-1, 0, 1]:
                if (current_pos[0] + dx, max_y_all) not in blocked:
                    blocked.add((current_pos[0] + dx, max_y_all))

        next_pos = current_pos[0], current_pos[1] + 1
        for dx in [-1, 1]:
            if next_pos in blocked:
                next_pos = current_pos[0] + dx, current_pos[1] + 1

        if next_pos in blocked:
            rest = True
        else:
            current_pos = next_pos

    if current_pos not in blocked and current_pos[1] < max_y_all:
        blocked.add(current_pos)


if __name__ == '__main__':
    with open('in.txt') as file:
        points = [[eval(point) for point in path.split(' -> ')] for path in file.read().splitlines()]

    blocked = set()

    for path in points:
        blocked.add(path[0])
        for i in range(len(path) - 1):
            if path[i][0] == path[i + 1][0]:
                min_y = min(path[i][1], path[i + 1][1])
                max_y = max(path[i][1], path[i + 1][1])
                for point in [(path[i][0], y) for y in range(min_y, max_y + 1)]:
                    blocked.add(point)
            elif path[i][1] == path[i + 1][1]:
                min_x = min(path[i][0], path[i + 1][0])
                max_x = max(path[i][0], path[i + 1][0])
                for point in [(x, path[i][1]) for x in range(min_x, max_x + 1)]:
                    blocked.add(point)

    sand_source = (500, 0)

    part1(blocked, sand_source)
    part2(blocked, sand_source)
