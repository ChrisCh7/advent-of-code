from typing import Callable, Iterable


def part1(pairs: list[list[list[int]]]):
    print('Part 1:', len(list(filter(lambda pair: ranges_overlap(pair, all), pairs))))


def ranges_overlap(pair: list[list[int]], how: Callable[[Iterable[object]], bool]) -> bool:
    range1 = range(pair[0][0], pair[0][1] + 1)
    range2 = range(pair[1][0], pair[1][1] + 1)
    return how(n in range2 for n in range1) or how(n in range1 for n in range2)


def part2(pairs: list[list[list[int]]]):
    print('Part 2:', len(list(filter(lambda pair: ranges_overlap(pair, any), pairs))))


if __name__ == '__main__':
    with open('in.txt') as file:
        pairs = [[[int(n) for n in rnge.split('-')] for rnge in pair.split(',')] for pair in file.read().splitlines()]

    part1(pairs)
    part2(pairs)
