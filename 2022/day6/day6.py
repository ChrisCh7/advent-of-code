def part1(datastream: str):
    print('Part 1:', get_nr_chars_until_marker(datastream, 4))


def part2(datastream: str):
    print('Part 2:', get_nr_chars_until_marker(datastream, 14))


def get_nr_chars_until_marker(datastream: str, nr_distinct_chars: int):
    for i in range(nr_distinct_chars - 1, len(datastream)):
        chars = datastream[i - (nr_distinct_chars - 1):i + 1]
        if len(chars) == len(set(chars)):
            return i + 1


if __name__ == '__main__':
    with open('in.txt') as file:
        datastream = file.read()

    part1(datastream)
    part2(datastream)
