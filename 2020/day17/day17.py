import copy


def main():
    with open('in.txt') as file:
        lines = [line.replace('.', '0').replace('#', '1') for line in file.read().splitlines()]

    lines = [[int(n) for n in list(line)] for line in lines]

    part1(lines)
    part2(lines)


def part1(lines):
    cubes = dict()
    for i in range(len(lines)):
        for j in range(len(lines[len(lines) - i - 1])):
            if lines[len(lines) - i - 1][j] == 1:
                cubes[(j, i, 0)] = 1

    for _ in range(6):
        cubes = run_one_cycle(cubes, 1)

    count_active = 0
    for cube in cubes.keys():
        if cubes[cube] == 1:
            count_active += 1

    print('Part 1:', count_active)


def part2(lines):
    cubes = dict()
    for i in range(len(lines)):
        for j in range(len(lines[len(lines) - i - 1])):
            if lines[len(lines) - i - 1][j] == 1:
                cubes[(j, i, 0, 0)] = 1

    for _ in range(6):
        cubes = run_one_cycle(cubes, 2)

    count_active = 0
    for cube in cubes.keys():
        if cubes[cube] == 1:
            count_active += 1

    print('Part 2:', count_active)


def run_one_cycle(cubes, part):
    new_cubes = copy.deepcopy(cubes)

    for cube in cubes:
        neighbors = get_neighbors(cube, part)
        count_active = len([neighbor for neighbor in neighbors if cubes.get(neighbor, 0) == 1])
        if cubes[cube] == 1 and (count_active < 2 or count_active > 3):
            new_cubes[cube] = 0
        if cubes[cube] == 0 and count_active == 3:
            new_cubes[cube] = 1

    for cube in get_all_neighbors(cubes, part):
        neighbors = get_neighbors(cube, part)
        count_active = len([neighbor for neighbor in neighbors if cubes.get(neighbor, 0) == 1])
        if cubes.get(cube, 0) == 1 and (count_active < 2 or count_active > 3):
            new_cubes[cube] = 0
        if cubes.get(cube, 0) == 0 and count_active == 3:
            new_cubes[cube] = 1

    return new_cubes


def get_neighbors(cube, part):
    if part == 1:
        return [(x, y, z) for x in range(cube[0] - 1, cube[0] + 2)
                for y in range(cube[1] - 1, cube[1] + 2)
                for z in range(cube[2] - 1, cube[2] + 2)
                if (x, y, z) != cube]
    elif part == 2:
        return [(x, y, z, w) for x in range(cube[0] - 1, cube[0] + 2)
                for y in range(cube[1] - 1, cube[1] + 2)
                for z in range(cube[2] - 1, cube[2] + 2)
                for w in range(cube[3] - 1, cube[3] + 2)
                if (x, y, z, w) != cube]


def get_all_neighbors(cubes, part):
    all_neighbors = []
    if part == 1:
        for cube in cubes:
            neighbors = [(x, y, z) for x in range(cube[0] - 1, cube[0] + 2)
                         for y in range(cube[1] - 1, cube[1] + 2)
                         for z in range(cube[2] - 1, cube[2] + 2)
                         if (x, y, z) != cube]
            all_neighbors.extend(neighbors)
    elif part == 2:
        for cube in cubes:
            neighbors = [(x, y, z, w) for x in range(cube[0] - 1, cube[0] + 2)
                         for y in range(cube[1] - 1, cube[1] + 2)
                         for z in range(cube[2] - 1, cube[2] + 2)
                         for w in range(cube[3] - 1, cube[3] + 2)
                         if (x, y, z, w) != cube]
            all_neighbors.extend(neighbors)
    return all_neighbors


if __name__ == '__main__':
    main()
