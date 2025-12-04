def main():
    with open('in.txt') as file:
        lines = file.read().splitlines()

    banks = [[int(battery) for battery in line] for line in lines]

    total_output_joltage = 0

    for bank in banks:
        best = 0
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                val = bank[i] * 10 + bank[j]
                if val > best:
                    best = val
        total_output_joltage += best

    print("Part 1:", total_output_joltage)
    total_output_joltage = sum(best_subsequence_of_12(bank) for bank in banks)
    print("Part 2:", total_output_joltage)


def best_subsequence_of_12(bank):
    chosen_digits = []
    search_start = 0
    total_needed = 12
    bank_length = len(bank)

    for digits_left_to_pick in range(total_needed, 0, -1):
        search_end = bank_length - digits_left_to_pick + 1
        best_digit = max(bank[search_start:search_end])
        best_digit_index = bank.index(best_digit, search_start, search_end)
        chosen_digits.append(best_digit)
        search_start = best_digit_index + 1

    return int("".join(map(str, chosen_digits)))


if __name__ == '__main__':
    main()
