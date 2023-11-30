def mix(numbers: list[tuple[int, int]], numbers_og: list[tuple[int, int]]):
    for nr in numbers_og:
        from_idx = numbers.index(nr)
        to_idx = (from_idx + nr[0]) % len(numbers_og)
        if from_idx + nr[0] < 0:
            to_idx -= abs((from_idx + nr[0]) // len(numbers_og))
        elif from_idx + nr[0] >= len(numbers_og) - 1:
            to_idx += abs((from_idx + nr[0]) // len(numbers_og))
        numbers.pop(from_idx)
        if to_idx == 0:
            numbers.append(nr)
        else:
            numbers.insert(to_idx, nr)


if __name__ == '__main__':
    with open('in.txt') as file:
        numbers = list(map(int, file.read().splitlines()))

    # numbers can repeat, keep track of indexes in the original list in addition to the number itself
    numbers = [(nr, i) for i, nr in enumerate(numbers)]
    numbers_og = numbers.copy()

    mix(numbers, numbers_og)

    zero_nr = next(nr for nr in numbers if nr[0] == 0)
    print('Part 1:', sum(numbers[(numbers.index(zero_nr) + pos) % len(numbers)][0] for pos in [1000, 2000, 3000]))

    # part 2 produces an incorrect result, something is wrong
    numbers = numbers_og.copy()
    numbers = [(nr[0] * 811589153, nr[1]) for nr in numbers]
    numbers_og_part2 = numbers.copy()

    for _ in range(10):
        mix(numbers, numbers_og_part2)

    zero_nr = next(nr for nr in numbers if nr[0] == 0)
    print('Part 2:', sum(numbers[(numbers.index(zero_nr) + pos) % len(numbers)][0] for pos in [1000, 2000, 3000]))
