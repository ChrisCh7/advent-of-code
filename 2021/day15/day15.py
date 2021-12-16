import numpy as np


def part1(cave: list[list[int]]):
    risk = get_min_risk(cave, len(cave), len(cave[0])) - cave[0][0]
    print('Part 1:', risk)


def part2(cave: list[list[int]]):
    arr = np.array(cave)
    arr_extra = []

    for i in range(1, 5):
        arr_extra.append(arr + i)

    for i in range(4):
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr_extra[i][row][col] > 9:
                    arr_extra[i][row][col] = arr_extra[i][row][col] % 9

    row_big = np.hstack((arr, *arr_extra))
    row_big_extra = []

    for i in range(1, 5):
        row_big_extra.append(row_big + i)

    for i in range(4):
        for row in range(len(row_big)):
            for col in range(len(row_big[0])):
                if row_big_extra[i][row][col] > 9:
                    row_big_extra[i][row][col] = row_big_extra[i][row][col] % 9

    final_big_arr = np.vstack((row_big, *row_big_extra))

    risk = get_min_risk(final_big_arr, len(final_big_arr), len(final_big_arr[0])) - final_big_arr[0][0]
    print('Part 2:', risk)


class Position:
    def __init__(self, x=0, y=0, distance=0):
        self.x = x
        self.y = y
        self.distance = distance

    def __repr__(self):
        return f'Position(x={self.x}, y={self.y}, distance={self.distance})'


def is_valid_pos(cave: list[list[int]], row: int, col: int):
    return row in range(len(cave)) and col in range(len(cave[0]))


def get_min_risk(cave: list[list[int]] | np.ndarray, row: int, col: int):
    dis = [[10 ** 9] * row for _ in range(col)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    st = [Position()]

    dis[0][0] = cave[0][0]

    while len(st) != 0:
        k = st.pop(0)

        for i in range(4):
            x = k.x + dx[i]
            y = k.y + dy[i]

            if not is_valid_pos(cave, x, y):
                continue

            if dis[x][y] > dis[k.x][k.y] + cave[x][y]:
                dis[x][y] = dis[k.x][k.y] + cave[x][y]
                st.append(Position(x, y, dis[x][y]))

        st.sort(key=lambda pos: (pos.distance, pos.x, pos.y))

    return dis[row - 1][col - 1]


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = [[int(n) for n in list(line)] for line in file.read().splitlines()]

    part1(lines)
    part2(lines)
