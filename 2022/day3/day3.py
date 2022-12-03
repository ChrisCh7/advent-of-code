def part1(backpacks: list[list[str]]):
    priority_sum = 0
    for backpack in backpacks:
        common_item = set(backpack[0]).intersection(set(backpack[1])).pop()
        priority_sum += get_item_priority(common_item)

    print('Part 1:', priority_sum)


def get_item_priority(item: str):
    return ord(item) - 96 if item.islower() else ord(item) - 38


def part2(backpacks: list[list[str]]):
    priority_sum = 0
    for i in range(0, len(backpacks), 3):
        common_item = (set(backpacks[i][0] + backpacks[i][1])
                       .intersection(set(backpacks[i + 1][0] + backpacks[i + 1][1]))
                       .intersection(set(backpacks[i + 2][0] + backpacks[i + 2][1])).pop())
        priority_sum += get_item_priority(common_item)

    print('Part 2:', priority_sum)


if __name__ == '__main__':
    with open('in.txt') as file:
        backpacks = [[backpack[:len(backpack) // 2], backpack[len(backpack) // 2:]]
                     for backpack in file.read().splitlines()]

    part1(backpacks)
    part2(backpacks)
