import numpy as np


def cartesian(arrays, out=None):
    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = int(n / arrays[0].size)
    out[:, 0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m, 1:])
        for j in range(1, arrays[0].size):
            out[j * m:(j + 1) * m, 1:] = out[0:m, 1:]
    return out


def get_answer(*numbers):
    product = cartesian(numbers)
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
