def part1(depths: list[int]):
    nr_increases = 0

    for n in range(1, len(depths)):
        if depths[n] > depths[n - 1]:
            nr_increases += 1

    print('Part 1:', nr_increases)


def part2(depths: list[int]):
    nr_increases = 0
    prev_sum = 0

    for n in range(len(depths) - 2):
        if prev_sum == 0:
            prev_sum = depths[n] + depths[n + 1] + depths[n + 2]
            continue

        current_sum = depths[n] + depths[n + 1] + depths[n + 2]

        if current_sum > prev_sum:
            nr_increases += 1

        prev_sum = current_sum

    print('Part 2:', nr_increases)


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    depths = [int(line) for line in lines]

    part1(depths)
    part2(depths)
