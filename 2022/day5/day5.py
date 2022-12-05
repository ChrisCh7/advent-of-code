import copy
from collections import deque


def part1(instructions: list[list[int]], stacks: list[deque[str]]):
    stacks = copy.deepcopy(stacks)

    for instruction in instructions:
        move_crates(instruction, stacks)

    print('Part 1:', end=' ')
    for stack in stacks:
        print(stack.pop(), end='')
    print()


def part2(instructions: list[list[int]], stacks: list[deque[str]]):
    stacks = copy.deepcopy(stacks)

    for instruction in instructions:
        move_crates_p2(instruction, stacks)

    print('Part 2:', end=' ')
    for stack in stacks:
        print(stack.pop(), end='')
    print()


def move_crates(instruction: list[int], stacks: list[deque[str]]):
    for _ in range(instruction[0]):
        stacks[instruction[2] - 1].append(stacks[instruction[1] - 1].pop())


def move_crates_p2(instruction: list[int], stacks: list[deque[str]]):
    temp_stack = deque()

    for _ in range(instruction[0]):
        temp_stack.append(stacks[instruction[1] - 1].pop())

    for _ in range(instruction[0]):
        stacks[instruction[2] - 1].append(temp_stack.pop())


if __name__ == '__main__':
    with open('in.txt') as file:
        drawing, instructions = file.read().split('\n\n')

    drawing = drawing.splitlines()
    nr_stacks = int(drawing[-1].split()[-1])
    drawing = drawing[:-1]

    stacks = [deque() for _ in range(nr_stacks)]

    for line in drawing:
        for i in range(nr_stacks):
            letter_index = 1 + i * 4
            if line[letter_index] != ' ':
                stacks[i].appendleft(line[letter_index])

    instructions = [[int(token) for token in line.split() if token.isnumeric()] for line in instructions.splitlines()]

    part1(instructions, stacks)
    part2(instructions, stacks)
