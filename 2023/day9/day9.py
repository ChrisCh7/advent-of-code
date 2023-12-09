import math


def lagrange_interpolation(x_values: list[int], y_values: list[int], x: int) -> float:
    result = 0
    for i in range(len(y_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result


def extrapolate_next_value(history: list[int]) -> float:
    return lagrange_interpolation(list(range(len(history))), history, len(history))


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    history = [list(map(int, line.split())) for line in lines]

    print('Part 1:', math.ceil(sum(extrapolate_next_value(h) for h in history)))
    print('Part 2:', math.floor(sum(extrapolate_next_value(h[::-1]) for h in history)))
