import re
from itertools import cycle
from math import lcm


def part1(instructions: str, nodes: dict[str, tuple[str, str]]):
    nr_steps = 0
    current_node = 'AAA'

    for instruction in cycle(instructions):
        if current_node == 'ZZZ':
            break
        current_node = nodes[current_node][0 if instruction == 'L' else 1]
        nr_steps += 1

    print('Part 1:', nr_steps)


def part2(instructions: str, lines: list[list[str]], nodes: dict[str, tuple[str, str]]):
    starting_nodes = [line[0] for line in lines if line[0].endswith('A')]

    steps = []
    for node in starting_nodes:
        nr_steps = 0
        current_node = node

        for instruction in cycle(instructions):
            if current_node.endswith('Z'):
                break
            current_node = nodes[current_node][0 if instruction == 'L' else 1]
            nr_steps += 1

        steps.append(nr_steps)

    print('Part 2:', lcm(*steps))


if __name__ == '__main__':
    with open('in.txt') as file:
        sections = file.read().split('\n\n')

    sections = [[re.findall(r'\w+', line) for line in section.splitlines()] for section in sections]

    instructions = sections[0][0][0]

    lines = sections[1]

    nodes = {n: (l, r) for [n, l, r] in lines}

    part1(instructions, nodes)
    part2(instructions, lines, nodes)
