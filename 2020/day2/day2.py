def part1():
    with open('in.txt') as inp:
        valid_pass_count = 0
        for line in inp.readlines():
            line = line.strip()
            parts = line.split(' ')
            nr_of_repetitions_min = int(parts[0].split('-')[0])
            nr_of_repetitions_max = int(parts[0].split('-')[1])
            letter = parts[1][0]
            password = parts[2]
            if nr_of_repetitions_min <= password.count(letter) <= nr_of_repetitions_max:
                valid_pass_count += 1
        print(valid_pass_count)


def part2():
    with open('in.txt') as inp:
        valid_pass_count = 0
        for line in inp.readlines():
            line = line.strip()
            parts = line.split(' ')
            index1 = int(parts[0].split('-')[0]) - 1
            index2 = int(parts[0].split('-')[1]) - 1
            letter = parts[1][0]
            password = parts[2]
            letter_is_present_at_index1 = password[index1] == letter
            letter_is_present_at_index2 = password[index2] == letter
            if letter_is_present_at_index1 != letter_is_present_at_index2:
                valid_pass_count += 1
        print(valid_pass_count)


if __name__ == '__main__':
    part1()
    part2()
