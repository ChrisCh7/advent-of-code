def part1(numbers):
    device = numbers[-1] + 3
    diff_1_jolt = 0
    diff_2_jolt = 0
    diff_3_jolt = 0
    current_joltage = 0
    index = 0

    while current_joltage < device:
        for i in range(index, len(numbers)):
            diff = numbers[i] - current_joltage
            if diff == 1:
                current_joltage += diff
                diff_1_jolt += 1
                index = i + 1
                break
            elif diff == 2:
                current_joltage += diff
                diff_2_jolt += 1
                index = i + 1
                break
            elif diff == 3:
                current_joltage += diff
                diff_3_jolt += 1
                index = i + 1
                break

        diff = device - current_joltage
        if diff == 1:
            current_joltage += diff
            diff_1_jolt += 1
        elif diff == 2:
            current_joltage += diff
            diff_2_jolt += 1
        elif diff == 3:
            current_joltage += diff
            diff_3_jolt += 1

    print('Part 1:', diff_1_jolt * diff_3_jolt)


def part2(numbers):
    numbers.insert(0, 0)
    next_possibilities = {number: [] for number in numbers}

    for i in range(len(numbers)):
        if i + 1 < len(numbers) and numbers[i + 1] - numbers[i] < 4:
            next_possibilities[numbers[i]].append(numbers[i + 1])
        if i + 2 < len(numbers) and numbers[i + 2] - numbers[i] < 4:
            next_possibilities[numbers[i]].append(numbers[i + 2])
        if i + 3 < len(numbers) and numbers[i + 3] - numbers[i] < 4:
            next_possibilities[numbers[i]].append(numbers[i + 3])

    ways = count_ways(next_possibilities, 0, numbers, dict())
    print('Part 2:', ways)


def count_ways(next_possibilities: dict[int, list[int]], index, numbers, storage):
    next = next_possibilities[numbers[index]]

    if len(next) == 0:
        return 1

    ways = 0
    for nr in next:
        if nr in storage:
            ways += storage[nr]
        else:
            ways_nr = count_ways(next_possibilities, numbers.index(nr), numbers, storage)
            ways += ways_nr
            storage[nr] = ways_nr

    return ways


if __name__ == '__main__':
    with open('in.txt') as file:
        numbers = [int(line) for line in file.read().splitlines()]
    numbers.sort()
    part1(numbers)
    part2(numbers)
