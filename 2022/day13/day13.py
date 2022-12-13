import operator
from functools import reduce


def part1(packet_pairs: list[list[list[list | int]]]):
    indices_sum = 0
    for i, pair in enumerate(packet_pairs):
        if check_pair(pair):
            indices_sum += i + 1

    print('Part 1:', indices_sum)


def part2(packet_pairs: list[list[list[list | int]]]):
    packets = reduce(operator.add, packet_pairs) + [[[2]]] + [[[6]]]

    done_sorting = False
    while not done_sorting:
        done_sorting = True
        for i in range(0, len(packets) - 1):
            if not check_pair([packets[i], packets[i + 1]]):
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                done_sorting = False

    print('Part 2:', (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


def check_pair(pair: list[list[list | int]]):
    right_order = None

    for i in range(max(len(pair[0]), len(pair[1]))):
        if len(pair[0][i:i + 1]) == 0:
            right_order = True
            break
        if len(pair[1][i:i + 1]) == 0:
            right_order = False
            break

        match [pair[0][i], pair[1][i]]:
            case [int(a), int(b)]:
                right_order = None if a == b else a < b
            case [list(a), list(b)]:
                right_order = check_pair([a, b])
            case [list(a), int(b)]:
                right_order = check_pair([a, [b]])
            case [int(a), list(b)]:
                right_order = check_pair([[a], b])

        if right_order is not None:
            break

    return right_order


if __name__ == '__main__':
    with open('in.txt') as file:
        packet_pairs = file.read().split('\n\n')

    packet_pairs = [[eval(packet) for packet in pair.splitlines()] for pair in packet_pairs]

    part1(packet_pairs)
    part2(packet_pairs)
