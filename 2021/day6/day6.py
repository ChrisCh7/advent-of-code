def part1(days: list[int]):
    for _ in range(80):
        days = simulate_a_day(days)
    print('Part 1:', sum(days))


def part2(days: list[int]):
    for _ in range(256):
        days = simulate_a_day(days)
    print('Part 2:', sum(days))


def simulate_a_day(days: list[int]):
    new_days = [0] * 9

    new_days[0] = days[1]
    new_days[1] = days[2]
    new_days[2] = days[3]
    new_days[3] = days[4]
    new_days[4] = days[5]
    new_days[5] = days[6]
    new_days[6] = days[7] + days[0]
    new_days[7] = days[8]
    new_days[8] = days[0]

    return new_days


if __name__ == '__main__':
    with open('in.txt') as file:
        timers = [int(n) for n in file.readline().split(',')]

    days = [0] * 9

    for timer in timers:
        days[timer] += 1

    part1(days)
    part2(days)
