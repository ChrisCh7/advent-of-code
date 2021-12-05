from collections import defaultdict


def part1(coords: list[list[list[int]]]):
    coords = list(filter(is_horizontal_or_vertical, coords))

    points = defaultdict(int)

    for coords_pair in coords:
        for point in get_points_between(coords_pair):
            points[tuple(point)] += 1

    print('Part 1:', sum([1 for (point, nr) in points.items() if nr > 1]))


def part2(coords: list[list[list[int]]]):
    points = defaultdict(int)

    for coords_pair in coords:
        for point in get_points_between_p2(coords_pair):
            points[tuple(point)] += 1

    print('Part 2:', sum([1 for (point, nr) in points.items() if nr > 1]))


def is_horizontal_or_vertical(coords: list[list[int]]):
    match coords:
        case [[x1, y1], [x2, y2]] if x1 == x2 or y1 == y2:
            return True
        case _:
            return False


def get_points_between(coords: list[list[int]]):
    points = []
    match coords:
        case [[x1, y1], [x2, y2]] if x1 == x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for y in range(min_y, max_y + 1):
                points.append([x1, y])
        case [[x1, y1], [x2, y2]] if y1 == y2:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            for x in range(min_x, max_x + 1):
                points.append([x, y1])
    return points


def get_points_between_p2(coords: list[list[int]]):
    points = []
    match coords:
        case [[x1, y1], [x2, y2]] if x1 == x2:
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            for y in range(min_y, max_y + 1):
                points.append([x1, y])
        case [[x1, y1], [x2, y2]] if y1 == y2:
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            for x in range(min_x, max_x + 1):
                points.append([x, y1])
        case _:
            leftmost_coord = min(coords[0], coords[1], key=lambda c: c[0])
            rightmost_coord = coords[1] if coords[0] == leftmost_coord else coords[0]

            current_coord = leftmost_coord
            points.append(current_coord.copy())

            if leftmost_coord[1] > rightmost_coord[1]:
                while current_coord != rightmost_coord:
                    current_coord[0] += 1
                    current_coord[1] -= 1
                    points.append(current_coord.copy())
            else:
                while current_coord != rightmost_coord:
                    current_coord[0] += 1
                    current_coord[1] += 1
                    points.append(current_coord.copy())
    return points


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    coords = []

    for line in lines:
        fst, snd = line.split(' -> ')
        coords.append([[int(n) for n in fst.split(',')], [int(n) for n in snd.split(',')]])

    part1(coords)
    part2(coords)
