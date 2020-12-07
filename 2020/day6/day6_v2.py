import functools


def part1(data: str):
    groups = [group.replace('\n', '') for group in data.split('\n\n')]
    yes_answers = [set(group) for group in groups]
    yes_count = functools.reduce(lambda count, set_yes_group: count + len(set_yes_group), yes_answers, 0)
    print(yes_count)


def part2(data: str):
    groups = [group.split() for group in data.split('\n\n')]

    yes_count = 0
    for group in groups:
        yes_answers = functools.reduce(
            lambda yes_group, person: ''.join([question for question in yes_group if question in person]), group)
        yes_count += len(yes_answers)

    print(yes_count)


if __name__ == '__main__':
    with open('in.txt') as file:
        data = file.read()
    part1(data)
    part2(data)
