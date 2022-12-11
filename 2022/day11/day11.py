import copy
import operator
from collections import deque
from functools import reduce
from typing import Self, Callable


class Monkey:
    def __init__(self, starting_items: deque[int], operation: Callable[[int], int], test: Callable[[int], bool],
                 true_monkey: int, false_monkey: int, divisible_by: int):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0
        self.divisible_by = divisible_by

    def take_turn_item(self, monkeys: list[Self], part: int = 1):
        worry = self.items.pop()
        worry = self.operation(worry)

        monkeys_divisible_by_product = reduce(operator.mul, map(lambda m: m.divisible_by, monkeys))
        worry = (worry // 3) if part == 1 else worry % monkeys_divisible_by_product

        if self.test(worry):
            monkeys[self.true_monkey].items.appendleft(worry)
        else:
            monkeys[self.false_monkey].items.appendleft(worry)

    def take_turn(self, monkeys: list[Self], part: int = 1):
        self.inspections += len(self.items)
        while self.items:
            self.take_turn_item(monkeys, part)


def parse_monkeys(monkeys: list[list[str]]):
    new_monkeys = []

    for monkey in monkeys:
        starting_items = deque(reversed([int(item.strip(',')) for item in monkey[1].split()[2:]]))
        operation = eval('lambda old: ' + monkey[2].split('=')[1])
        divisible_by = int(monkey[3].split('by')[1])
        test = eval(f'lambda l: l % {divisible_by} == 0')
        true_monkey = int(monkey[4].split()[-1])
        false_monkey = int(monkey[5].split()[-1])
        new_monkeys.append(Monkey(starting_items, operation, test, true_monkey, false_monkey, divisible_by))

    return new_monkeys


def part1(monkeys: list[Monkey]):
    monkeys = copy.deepcopy(monkeys)

    for _ in range(20):
        for monkey in monkeys:
            monkey.take_turn(monkeys)

    print('Part 1:', reduce(operator.mul, sorted(map(lambda m: m.inspections, monkeys), reverse=True)[:2]))


def part2(monkeys: list[Monkey]):
    monkeys = copy.deepcopy(monkeys)

    for _ in range(10000):
        for monkey in monkeys:
            monkey.take_turn(monkeys, 2)

    print('Part 2:', reduce(operator.mul, sorted(map(lambda m: m.inspections, monkeys), reverse=True)[:2]))


if __name__ == '__main__':
    with open('in.txt') as file:
        monkeys = [m.splitlines() for m in file.read().split('\n\n')]

    monkeys = parse_monkeys(monkeys)

    part1(monkeys)
    part2(monkeys)
