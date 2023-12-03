import re
from math import prod


def is_valid_idx(engine_schematic: list[str], y: int, x: int):
    return (0 <= y < len(engine_schematic) and
            0 <= x < len(engine_schematic[0]))


def is_adjacent_to_sign(engine_schematic: list[str], y: int, x: int):
    for pos in [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                (y, x - 1), (y, x + 1),
                (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]:
        if (is_valid_idx(engine_schematic, *pos) and
                not engine_schematic[pos[0]][pos[1]].isdigit() and
                engine_schematic[pos[0]][pos[1]] != '.'):
            return True
    return False


def detect_adjacent_stars(engine_schematic: list[str], y: int, x: int):
    star_pos = set()
    for pos in [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                (y, x - 1), (y, x + 1),
                (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]:
        if (is_valid_idx(engine_schematic, *pos) and
                engine_schematic[pos[0]][pos[1]] == '*'):
            star_pos.add(pos)
    return star_pos


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    part_numbers = []

    stars = {}

    for i, line in enumerate(lines):
        for idx_char, char in enumerate(line):
            if char == '*':
                stars[(i, idx_char)] = []

    for i, line in enumerate(lines):
        nrs = re.findall(r'\d+', line)

        if not nrs:
            continue

        start_idx = 0

        for nr in nrs:
            is_part_number = False
            nr_idx = line.index(nr, start_idx)
            start_idx = nr_idx + len(nr)

            star_pos = set()

            for idx_digit_in_number, digit in enumerate(nr):
                adjacent_to_sign = is_adjacent_to_sign(lines, i, nr_idx + idx_digit_in_number)

                if adjacent_to_sign:
                    is_part_number = True
                    star_pos |= detect_adjacent_stars(lines, i, nr_idx + idx_digit_in_number)

                if is_part_number and idx_digit_in_number == len(nr) - 1:
                    part_numbers.append(int(nr))

            for pos in star_pos:
                stars[pos].append(int(nr))

    print('Part 1:', sum(part_numbers))
    print('Part 2:', sum([prod(star) for star in stars.values() if len(star) > 1]))
