from collections import defaultdict


def part1(heightmap: list[list[int]]):
    low_points = []

    for i in range(1, len(heightmap) - 1):
        for j in range(1, len(heightmap[0]) - 1):
            if (heightmap[i][j - 1] > heightmap[i][j] and
                    heightmap[i][j + 1] > heightmap[i][j] and
                    heightmap[i - 1][j] > heightmap[i][j] and
                    heightmap[i + 1][j] > heightmap[i][j]):
                low_points.append(heightmap[i][j])

    print('Part 1:', sum(low_points) + len(low_points))


def part2(heightmap: list[list[int]]):
    visited = defaultdict(lambda: False)

    sizes = []

    for x in range(0, len(heightmap[0])):
        for y in range(0, len(heightmap)):
            size, visited = group_size(x, y, visited, heightmap)
            if size != 0:
                sizes.append(size)

    sizes = sorted(sizes)
    print('Part 2:', sizes[-1] * sizes[-2] * sizes[-3])


def group_size(x, y, visited, heightmap):
    size = 0
    if x in range(len(heightmap[0])) and y in range(len(heightmap)) and not visited[(x, y)] and heightmap[y][x] != 9:
        visited[(x, y)] = True
        size = 1
        right = group_size(x + 1, y, visited, heightmap)
        size += right[0]
        visited = right[1]
        left = group_size(x - 1, y, visited, heightmap)
        size += left[0]
        visited = left[1]
        down = group_size(x, y + 1, visited, heightmap)
        size += down[0]
        visited = down[1]
        up = group_size(x, y - 1, visited, heightmap)
        size += up[0]
        visited = up[1]
    return size, visited


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = [[int(n) for n in list(line)] for line in file.read().splitlines()]

    width = len(lines[0])
    heightmap = []

    heightmap.append([9] * (width + 2))
    for line in lines:
        heightmap.append([9] + line + [9])
    heightmap.append([9] * (width + 2))

    part1(heightmap)
    part2(heightmap)
