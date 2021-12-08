def part1(outputs: list[list[str]]):
    count_digits = 0

    for output in outputs:
        for digit in output:
            if len(digit) in [2, 4, 3, 7]:
                count_digits += 1

    print('Part 1:', count_digits)


def part2(patterns: list[list[str]], outputs: list[list[str]]):
    sum_outputs = 0

    for i, entry_patterns in enumerate(patterns):
        numbers = determine_numbers(entry_patterns)

        output_digits = ''

        for digit in outputs[i]:
            sorted_digit = ''.join(sorted(digit))
            output_digits += str(numbers[sorted_digit])

        sum_outputs += int(output_digits)

    print('Part 2:', sum_outputs)


def determine_numbers(patterns: list[str]):
    numbers = {}

    for i, pattern in enumerate(patterns):
        patterns[i] = ''.join(sorted(pattern))

    one_pattern = list(filter(lambda p: len(p) == 2, patterns))[0]
    seven_pattern = list(filter(lambda p: len(p) == 3, patterns))[0]
    four_pattern = list(filter(lambda p: len(p) == 4, patterns))[0]
    eight_pattern = list(filter(lambda p: len(p) == 7, patterns))[0]

    numbers[one_pattern] = 1
    numbers[seven_pattern] = 7
    numbers[four_pattern] = 4
    numbers[eight_pattern] = 8

    five_segments = list(filter(lambda p: len(p) == 5, patterns))
    six_segments = list(filter(lambda p: len(p) == 6, patterns))

    two_pattern, three_pattern, five_pattern = determine_numbers_5_segments(five_segments, seven_pattern, four_pattern)
    zero_pattern, six_pattern, nine_pattern = determine_numbers_6_segments(six_segments, seven_pattern, four_pattern)

    numbers[zero_pattern] = 0
    numbers[two_pattern] = 2
    numbers[three_pattern] = 3
    numbers[five_pattern] = 5
    numbers[six_pattern] = 6
    numbers[nine_pattern] = 9

    return numbers


def determine_numbers_5_segments(five_segments: list[str], seven_pattern: str, four_pattern: str):
    two_pattern = ''
    three_pattern = ''

    for pattern in five_segments:
        if len(set(pattern).intersection(set(seven_pattern))) == 3:
            three_pattern = pattern
            break

    five_segments.remove(three_pattern)

    for pattern in five_segments:
        if len(set(pattern).intersection(set(four_pattern))) == 2:
            two_pattern = pattern
            break

    five_segments.remove(two_pattern)
    five_pattern = five_segments[0]

    return two_pattern, three_pattern, five_pattern


def determine_numbers_6_segments(six_segments: list[str], seven_pattern: str, four_pattern: str):
    zero_pattern = ''
    six_pattern = ''

    for pattern in six_segments:
        if len(set(pattern).intersection(set(seven_pattern))) == 2:
            six_pattern = pattern
            break

    six_segments.remove(six_pattern)

    for pattern in six_segments:
        if len(set(pattern).intersection(set(four_pattern))) == 3:
            zero_pattern = pattern
            break

    six_segments.remove(zero_pattern)
    nine_pattern = six_segments[0]

    return zero_pattern, six_pattern, nine_pattern


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    patterns = []
    outputs = []

    for entry in lines:
        parts = entry.split('|')
        patterns.append(parts[0].split())
        outputs.append(parts[1].split())

    part1(outputs)
    part2(patterns, outputs)
