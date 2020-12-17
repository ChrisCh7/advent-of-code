def main(numbers, end):
    spoken = {nr: [idx] for idx, nr in enumerate(numbers[:-1])}

    while len(numbers) < end:
        last_nr_spoken = numbers[-1]

        info_nr = spoken.get(last_nr_spoken, list())

        if len(info_nr) == 0:
            next_nr = 0
        else:
            next_nr = len(numbers) - 1 - spoken[last_nr_spoken][0]

        spoken[last_nr_spoken] = [len(numbers) - 1]
        numbers.append(next_nr)

    print(numbers[-1])


if __name__ == '__main__':
    with open('in.txt') as file:
        numbers = [int(n) for n in file.readline().strip().split(',')]
    main(numbers, 2020)
    main(numbers, 30000000)
