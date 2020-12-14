from itertools import product

bits = 36


def part1(lines):
    memory = dict()
    mask = ''

    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
            continue
        parts = line.split(' = ')
        memory_location = int(parts[0].split('[')[1][:-1])
        value = int(parts[1])
        new_value = apply_mask_p1(mask, get_bits(value))
        memory[memory_location] = new_value

    sum = 0
    for value in memory.values():
        sum += int(value, 2)

    print('Part 1:', sum)


def get_bits(number):
    return "{0:#b}".format(number).replace('b', '').rjust(36, '0')


def apply_mask_p1(mask, value):
    new_value_list = list(value)
    for i in range(bits):
        if mask[i] == 'X':
            continue
        if mask[i] in ['0', '1']:
            new_value_list[i] = mask[i]
    return ''.join(new_value_list)


def apply_mask_p2(mask, value):
    new_value_list = list(value)
    for i in range(bits):
        if mask[i] == 'X':
            new_value_list[i] = mask[i]
        if mask[i] == '0':
            continue
        if mask[i] == '1':
            new_value_list[i] = mask[i]
    return ''.join(new_value_list)


def handle_floating_bits(memory_location_with_floats):
    memory_locations = []
    count_x = memory_location_with_floats.count('X')
    combinations = [list(combination) for combination in list(product(range(2), repeat=count_x))]
    for combination in combinations:
        location = list(memory_location_with_floats)
        for i in range(len(combination)):
            location[location.index('X')] = str(combination[i])
        memory_locations.append(int(''.join(location), 2))
    return memory_locations


def part2(lines):
    memory = dict()
    mask = ''

    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
            continue
        parts = line.split(' = ')
        memory_location = int(parts[0].split('[')[1][:-1])
        value = int(parts[1])
        new_memory_location = apply_mask_p2(mask, get_bits(memory_location))
        memory_locations = handle_floating_bits(new_memory_location)
        for memory_location in memory_locations:
            memory[memory_location] = value

    sum = 0
    for value in memory.values():
        sum += value

    print('Part 2:', sum)


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    part1(lines)
    part2(lines)
