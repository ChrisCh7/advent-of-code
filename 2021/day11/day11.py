import copy
from itertools import chain


def part1(octopi: list[list[int]]):
    octopi = copy.deepcopy(octopi)
    flashes = []

    for _ in range(100):
        octopi, flashes_step = sim_step(octopi, [])
        flashes.extend(flashes_step)

    print('Part 1:', len(flashes))


def part2(octopi: list[list[int]]):
    octopi = copy.deepcopy(octopi)
    flashes_step = []

    step = 0

    while not len(flashes_step) == len(octopi) * len(octopi[0]):
        step += 1
        octopi, flashes_step = sim_step(octopi, [])

    print('Part 2:', step)


def sim_step(octopi: list[list[int]], flashes: list[tuple[int, int]]):
    for i in range(len(octopi)):
        for j in range(len(octopi[0])):
            octopi[i][j] += 1

    post_flash_octopi = copy.deepcopy(octopi)

    while 10 in list(chain.from_iterable(octopi)):
        post_flash_octopi = copy.deepcopy(octopi)

        for i in range(len(octopi)):
            for j in range(len(octopi[0])):
                if octopi[i][j] == 10:
                    post_flash_octopi, flashes = flash(post_flash_octopi, flashes, i, j)

        octopi = post_flash_octopi

    return post_flash_octopi, flashes


def flash(octopi: list[list[int]], flashes: list[tuple[int, int]], row: int, col: int):
    flashes.append((row, col))
    octopi[row][col] = 0

    rows = len(octopi)
    cols = len(octopi[0])

    if col + 1 in range(cols):
        octopi, flashes = flash_wave(octopi, flashes, row, col + 1)
    if col - 1 in range(cols):
        octopi, flashes = flash_wave(octopi, flashes, row, col - 1)
    if row - 1 in range(rows):
        octopi, flashes = flash_wave(octopi, flashes, row - 1, col)
    if row + 1 in range(rows):
        octopi, flashes = flash_wave(octopi, flashes, row + 1, col)
    if row - 1 in range(rows) and col - 1 in range(cols):
        octopi, flashes = flash_wave(octopi, flashes, row - 1, col - 1)
    if row - 1 in range(rows) and col + 1 in range(cols):
        octopi, flashes = flash_wave(octopi, flashes, row - 1, col + 1)
    if row + 1 in range(rows) and col - 1 in range(cols):
        octopi, flashes = flash_wave(octopi, flashes, row + 1, col - 1)
    if row + 1 in range(rows) and col + 1 in range(cols):
        octopi, flashes = flash_wave(octopi, flashes, row + 1, col + 1)

    return octopi, flashes


def flash_wave(octopi: list[list[int]], flashes: list[tuple[int, int]], row: int, col: int):
    if octopi[row][col] < 10 and (row, col) not in flashes:
        octopi[row][col] += 1

    return octopi, flashes


if __name__ == '__main__':
    with open('in.txt') as file:
        octopi = [[int(n) for n in list(line)] for line in file.read().splitlines()]

    part1(octopi)
    part2(octopi)
