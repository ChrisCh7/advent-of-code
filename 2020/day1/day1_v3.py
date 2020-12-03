import numpy as np


def get_answer(*numbers):
    grid = np.array(np.meshgrid(*numbers))
    product = grid.T.reshape(-1, len(numbers))
    for nr in product:
        if np.sum(nr) == 2020:
            print('numbers: ' + str(nr))
            print('answer: ' + str(np.product(nr)))
            return


def main():
    with open('in.txt') as input:
        numbers = [int(line) for line in input.readlines()]
        get_answer(numbers, numbers)
        get_answer(numbers, numbers, numbers)


if __name__ == "__main__":
    main()
