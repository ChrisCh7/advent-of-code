import math


def part1():
    with open('in.txt') as file:
        lines = [int(line) for line in file.readlines()]
        total_fuel = 0
        for nr in lines:
            fuel = math.floor(nr / 3) - 2
            total_fuel += fuel
        print('total_fuel:', total_fuel)


def part2():
    with open('in.txt') as file:
        lines = [int(line) for line in file.readlines()]
        total_fuel = 0
        for nr in lines:
            fuel = math.floor(nr / 3) - 2
            new_fuel = fuel
            while new_fuel > 0:
                new_fuel = math.floor(new_fuel / 3) - 2
                if new_fuel > 0:
                    fuel += new_fuel
            total_fuel += fuel
        print('total_fuel, with fuel for fuel:', total_fuel)


if __name__ == '__main__':
    part1()
    part2()
