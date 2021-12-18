import copy
import math
import re
from functools import reduce


def part1(nrs: list):
    first_sum = add_nrs(nrs[0], nrs[1])
    res = reduce(add_nrs, nrs[2:], first_sum)

    print('Part 1:', get_magnitude(res))


def part2(nrs: list):
    sums = []

    for i in range(len(nrs)):
        for j in range(len(nrs)):
            if i != j:
                res = add_nrs(nrs[i], nrs[j])
                magn = get_magnitude(res)
                sums.append({'sum': res, 'nrs': [nrs[i], nrs[j]], 'magnitude': magn})

    print('Part 2:', max(sums, key=lambda s: s['magnitude'])['magnitude'])


def add_nrs(nr1: int | list, nr2: int | list):
    addition = [nr1, nr2]

    res = addition
    res_prev = None

    while res_prev is None or res != res_prev:
        res_prev = copy.deepcopy(res)
        if can_explode(res):
            res = explode(res)
        elif sorted(map(int, get_numbers(str(res))))[-1] > 9:
            res = split(res)

    return res


def explode(nr: list):
    result = copy.deepcopy(nr)

    revert_steps = []

    nr_removed_layers = 0
    while not all([isinstance(n, int) for n in result]):
        result, ops = remove_layer(result)
        revert_steps.append(ops)
        nr_removed_layers += 1

    result = add_layer(result, revert_steps.pop())
    nr_removed_layers -= 1

    for i, el in enumerate(result):
        if isinstance(el, list):
            if i - 1 >= 0:
                result[i - 1] += result[i][0]
            if i + 1 < len(result):
                if isinstance(result[i + 1], int):
                    result[i + 1] += result[i][1]
                else:
                    result[i + 1][0] += result[i][1]
            result[i] = 0
            break

    for _ in range(nr_removed_layers):
        result = add_layer(result, revert_steps.pop())

    return result


def split(nr: list):
    to_replace = map(int, get_numbers(str(nr)))
    for n in to_replace:
        if n > 9:
            to_replace = n
            break
    replacement = [to_replace // 2, math.ceil(to_replace / 2)]
    return eval(str(nr).replace(str(to_replace), str(replacement), 1))


def remove_layer(nr: list[list | int]):
    result = []
    ops = {}

    for i, n in enumerate(nr):
        if isinstance(n, list):
            ops[i] = [index + len(result) for index in list(range(len(n)))]
            result.extend(n)
        else:
            ops[i] = len(result)
            result.append(n)

    return result, ops


def add_layer(nr: list[list | int], ops: dict[int, int | list[int]]):
    result = [0] * len(ops)

    for i_pre, i_post in ops.items():
        if isinstance(i_post, list):
            result[i_pre] = nr[i_post[0]:i_post[-1] + 1]
        else:
            result[i_pre] = nr[i_post]

    return result


def get_numbers(string: str):
    return [n for n in re.split(r'[\[\], ]', string) if n != '']


def can_explode(nr: list):
    levels = 0

    for c in str(nr):
        if c == '[':
            if levels == 4:
                return True
            levels += 1
        elif c == ']':
            levels -= 1

    return False


def get_magnitude(nr: list):
    match nr:
        case [int(first), int(second)]:
            return 3 * first + 2 * second
        case [int(first), list(second)]:
            return 3 * first + 2 * get_magnitude(second)
        case [list(first), int(second)]:
            return 3 * get_magnitude(first) + 2 * second
        case [list(first), list(second)]:
            return 3 * get_magnitude(first) + 2 * get_magnitude(second)


if __name__ == '__main__':
    with open('in.txt') as file:
        nrs = [eval(line) for line in file.read().splitlines()]

    part1(nrs)
    part2(nrs)
