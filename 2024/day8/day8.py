from collections import defaultdict


def find_antinode_positions(height, width, frequencies, part):
    antinode_positions = set()

    for freq, points in frequencies.items():
        if part == 2:
            # antenna is not antinode if only one of its frequency
            if len(points) == 1:
                continue

            # antennas are antinodes too
            antinode_positions.update(points)

        nr_points = len(points)
        for i in range(nr_points):
            for j in range(i + 1, nr_points):
                x1, y1 = points[i]
                x2, y2 = points[j]

                # distances between antenna coords
                dx, dy = x2 - x1, y2 - y1

                k = 1
                while (k == 1 and part == 1) or (k * dx < width and k * dy < height and part == 2):
                    # potential antinode positions, nearer one antenna and then the other
                    x3, y3 = x1 - k * dx, y1 - k * dy
                    x4, y4 = x2 + k * dx, y2 + k * dy

                    # consider position if within bounds
                    if 0 <= x3 < width and 0 <= y3 < height:
                        antinode_positions.add((x3, y3))
                    if 0 <= x4 < width and 0 <= y4 < height:
                        antinode_positions.add((x4, y4))

                    k += 1

    return antinode_positions


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    antennas = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                antennas.append((x, y, char))

    frequencies = defaultdict(list)
    for x, y, freq in antennas:
        frequencies[freq].append((x, y))

    print('Part 1:', len(find_antinode_positions(len(lines), len(lines[0]), frequencies, 1)))
    print('Part 2:', len(find_antinode_positions(len(lines), len(lines[0]), frequencies, 2)))
