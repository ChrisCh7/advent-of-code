import itertools

import numpy as np


def main(number_of_numbers):
    with open('in.txt') as input:
        numbers = [int(line) for line in input.readlines()]
        product = list(itertools.product(numbers, repeat=number_of_numbers))
        for nr in product:
            if sum(nr) == 2020:
                print('numbers: ' + str(nr))
                print('answer: ' + str(np.prod(nr)))
                return


if __name__ == "__main__":
    print('Part 1')
    main(2)
    print('Part 2')
    main(3)
