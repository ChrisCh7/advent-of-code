from enum import Enum


def part1(lines: list[str], rows: int):
    zeros = [0] * rows
    ones = [0] * rows

    for line in lines:
        for i, digit in enumerate(line):
            if int(digit) == 0:
                zeros[i] += 1
            else:
                ones[i] += 1

    gamma_rate = ''

    for pos in range(rows):
        if zeros[pos] > ones[pos]:
            gamma_rate += '0'
        else:
            gamma_rate += '1'

    gamma_rate_decimal = int(gamma_rate, 2)

    epsilon_rate = gamma_rate.translate(str.maketrans({'1': '0', '0': '1'}))

    epsilon_rate_decimal = int(epsilon_rate, 2)

    print('Part 1:', gamma_rate_decimal * epsilon_rate_decimal)


def part2(lines: list[str], rows: int):
    nrs = lines

    for pos in range(rows):
        nrs = filter_nrs(nrs, pos, BitCriteria.MOST)
        if len(nrs) == 1:
            break

    oxygen_generator_rating_decimal = int(nrs[0], 2)

    nrs = lines

    for pos in range(rows):
        nrs = filter_nrs(nrs, pos, BitCriteria.LEAST)
        if len(nrs) == 1:
            break

    co2_scrubber_rating_decimal = int(nrs[0], 2)

    print('Part 2:', oxygen_generator_rating_decimal * co2_scrubber_rating_decimal)


class BitCriteria(Enum):
    MOST = 1
    LEAST = 2


def get_common_bit(nrs: list[str], pos: int, bit_criteria: BitCriteria):
    zeros = 0
    ones = 0

    for nr in nrs:
        if int(nr[pos]) == 0:
            zeros += 1
        else:
            ones += 1

    if zeros == ones:
        return 1 if bit_criteria is BitCriteria.MOST else 0
    elif zeros > ones:
        return 0 if bit_criteria is BitCriteria.MOST else 1
    else:
        return 1 if bit_criteria is BitCriteria.MOST else 0


def filter_nrs(nrs: list[str], pos, bit_criteria):
    bit = get_common_bit(nrs, pos, bit_criteria)

    if bit == 1:
        nrs = [nr for nr in nrs if nr[pos] == '1']
    else:
        nrs = [nr for nr in nrs if nr[pos] == '0']

    return nrs


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    rows = len(lines[0])

    part1(lines, rows)
    part2(lines, rows)
