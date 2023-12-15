import re
from collections import defaultdict


def get_hash(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def get_focusing_power(box: int, slot: int, focal_length: int) -> int:
    return (1 + box) * slot * focal_length


if __name__ == '__main__':
    with open('in.txt') as file:
        sequence = file.read().replace('\n', '').split(',')

    result = 0
    for step in sequence:
        current_value = get_hash(step)
        result += current_value

    print('Part 1:', result)

    boxes = defaultdict(list)

    for step in sequence:
        label, focal_length = re.split(r'[=-]', step)
        box = get_hash(label)
        operation = '=' if focal_length else '-'
        lens = f'{label} {focal_length}'

        if operation == '-':
            for l in boxes[box]:
                if l.split()[0] == label:
                    boxes[box].remove(l)
                    break
        else:
            i = -1
            for l in boxes[box]:
                if l.split()[0] == label:
                    i = boxes[box].index(l)
                    boxes[box][i] = lens
                    break
            if i == -1:
                boxes[box].append(lens)

    total_focusing_power = 0

    for box in boxes:
        for i, lens in enumerate(boxes[box]):
            focusing_power = get_focusing_power(box, i + 1, int(lens.split()[1]))
            total_focusing_power += focusing_power

    print('Part 2:', total_focusing_power)
