import math
import statistics


def part1(positions: list[int]):
    median_pos = statistics.median(positions)
    fuel = 0
    for pos in positions:
        fuel += abs(pos - median_pos)
    print('Part 1:', int(fuel))


def part2(positions: list[int]):
    mean_pos = math.floor(statistics.mean(positions))
    fuel = 0
    for pos in positions:
        cost = 1
        for _ in range(abs(pos - mean_pos)):
            fuel += cost
            cost += 1
    print('Part 2:', fuel)


if __name__ == '__main__':
    with open('in.txt') as file:
        positions = [int(n) for n in file.readline().split(',')]

    part1(positions)
    part2(positions)
