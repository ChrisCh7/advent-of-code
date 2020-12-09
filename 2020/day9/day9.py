from itertools import combinations


def part1(numbers):
    for i in range(25, len(numbers)):
        previous_25 = numbers[i - 25:i]
        sums = [sum(combination) for combination in list(combinations(previous_25, 2))]
        if numbers[i] not in sums:
            print('Part 1:', numbers[i])
            return numbers[i]


def part2(numbers, invalid_number):
    range_length = 2
    while range_length < len(numbers):
        for i in range(0, len(numbers) + 1 - range_length):
            nr = numbers[i: i + range_length]
            if invalid_number == sum(nr):
                nr.sort()
                print('Part 2:', nr[0] + nr[-1])
                return
        range_length += 1


if __name__ == '__main__':
    with open('in.txt') as file:
        numbers = [int(line) for line in file.read().splitlines()]
    invalid_number = part1(numbers)
    part2(numbers, invalid_number)
