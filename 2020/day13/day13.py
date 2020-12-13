from sympy.ntheory.modular import crt


def part1(lines):
    estimate = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']

    minutes_to_wait = [estimate - (bus * round(estimate / bus)) for bus in buses]
    min_minutes_to_wait = list(filter(lambda m: m[1] <= 0, list(enumerate(minutes_to_wait))))
    min_minutes_to_wait = min(min_minutes_to_wait, key=lambda m: abs(m[1]))
    min_bus_minutes = buses[min_minutes_to_wait[0]], abs(min_minutes_to_wait[1])

    print('Part 1:', min_bus_minutes[0] * min_bus_minutes[1])


def part2(lines):
    buses = [1 if bus == 'x' else int(bus) for bus in lines[1].split(',')]

    remainders = [bus - buses.index(bus) for bus in buses]

    t = crt(buses, remainders)[0]

    print('Part 2:', t)


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    part1(lines)
    part2(lines)
