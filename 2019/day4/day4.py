def part1(range_min, range_max):
    valid_passwords = 0

    for i in range(range_min, range_max + 1):
        if is_valid_password(i):
            valid_passwords += 1

    print('Part 1:', valid_passwords)


def part2(range_min, range_max):
    valid_passwords = 0

    for i in range(range_min, range_max + 1):
        if is_valid_password_part2(i):
            valid_passwords += 1

    print('Part 2:', valid_passwords)


def contains_adjacent_matching_digits(number):
    return len(str(number)) != len(set(str(number)))


def digits_never_decrease(number):
    return str(number) == ''.join(sorted(str(number)))


def is_valid_password(number):
    return contains_adjacent_matching_digits(number) and digits_never_decrease(number)


def is_valid_password_part2(number):
    return (contains_adjacent_matching_digits(number) and digits_never_decrease(number)
            and contains_group_of_exactly_2_adjacent_matching_digits(number))


def contains_group_of_exactly_2_adjacent_matching_digits(number):
    number = str(number)
    uniq_digits = list(set(number))

    for digit in uniq_digits:
        if number.count(digit) == 2:
            return True

    return False


if __name__ == '__main__':
    with open('in.txt') as file:
        line = file.readline()

    range_min, range_max = line.split('-')
    range_min = int(range_min)
    range_max = int(range_max)

    part1(range_min, range_max)
    part2(range_min, range_max)
