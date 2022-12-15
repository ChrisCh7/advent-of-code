import re


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    with open('in.txt') as file:
        info = file.read().splitlines()

    for i, line in enumerate(info):
        res = re.search(r'.*x=(.+), y=(.+):.*x=(.+), y=(.+)', line)
        info[i] = [int(res.group(j)) for j in range(1, 5)]
        info[i] += [manhattan_distance(info[i][0], info[i][1], info[i][2], info[i][3])]

    max_x = 0
    dist_for_max_x = 0
    for inf in info:
        if inf[0] > max_x:
            max_x = inf[0]
            dist_for_max_x = inf[4]
    limit = max_x + dist_for_max_x

    counter = 0
    searched_row = 2000000

    for i in range(-limit, limit + 1):
        sensor_covering_point = next((inf for inf in info
                                      if inf[4] >= manhattan_distance(i, searched_row, inf[0], inf[1])
                                      and (i, searched_row) != (inf[2], inf[3])), None)
        counter += 1 if sensor_covering_point else 0

    print('Part 1:', counter)

    limit = 4000000

    f = lambda x, y, d, p, q, r: ((p + q + r + x - y - d) // 2, (p + q + r - x + y + d) // 2 + 1)

    for X, Y in [f(a[0], a[1], a[4], b[0], b[1], b[4]) for a in info for b in info]:
        if 0 < X < limit and 0 < Y < limit and all(manhattan_distance(X, Y, x, y) > d for x, y, bx, by, d in info):
            print('Part 2:', limit * X + Y)
            break
