import math
import re

import sympy as sp


def find_times_to_hold(total_time: int, distance: int) -> list[int]:
    holding_time = sp.Symbol('holding_time')

    f = holding_time * (total_time - holding_time) > distance

    roots = sp.solve_univariate_inequality(f, holding_time, relational=False)

    root_args = [float(roots.args[0]), float(roots.args[1])]
    if root_args[0].is_integer():
        root_args[0] += 0.1
    if root_args[1].is_integer():
        root_args[1] -= 0.1

    holding_time_start = math.ceil(root_args[0])
    holding_time_end = math.floor(root_args[1])

    return [t for t in range(holding_time_start, holding_time_end + 1)]


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    lines = [list(map(int, re.findall(r'\d+', line))) for line in lines]

    ways_to_win = []
    for race_nr in range(len(lines[0])):
        ways = len(find_times_to_hold(lines[0][race_nr], lines[1][race_nr]))
        ways_to_win.append(ways)

    print('Part 1:', math.prod(ways_to_win))

    lines = [int(''.join(map(str, line))) for line in lines]

    ways_to_win = len(find_times_to_hold(lines[0], lines[1]))

    print('Part 2:', ways_to_win)
