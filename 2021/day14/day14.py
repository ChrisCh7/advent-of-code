from collections import Counter, defaultdict


def part1(template: str, rules: dict[str, str]):
    for _ in range(10):
        template = step(template, rules)

    counts_letters = Counter(template)
    max_count = max(counts_letters.items(), key=lambda i: i[1])[1]
    min_count = min(counts_letters.items(), key=lambda i: i[1])[1]

    print('Part 1:', max_count - min_count)


def part2(template: str, rules: dict[str, str]):
    counts_rules = {rule: 0 for rule in rules}

    for i in range(len(template) - 1):
        counts_rules[template[i:i + 2]] += 1

    counts_letters = defaultdict(int)

    for letter in template:
        counts_letters[letter] += 1

    for _ in range(40):
        counts_rules, counts_letters = step_p2(rules, counts_rules, counts_letters)

    max_count = max(counts_letters.items(), key=lambda i: i[1])[1]
    min_count = min(counts_letters.items(), key=lambda i: i[1])[1]

    print('Part 2:', max_count - min_count)


def step(template: str, rules: dict[str, str]):
    new_template = template
    index_diff = 0

    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        new_template = new_template[:i + 1 + index_diff] + rules[pair] + new_template[i + 1 + index_diff:]
        index_diff += 1

    return new_template


def step_p2(rules: dict[str, str], counts_rules: dict[str, int], counts_letters: dict[str, int]):
    new_counts_rules = counts_rules.copy()
    new_counts_letters = counts_letters.copy()

    for rule, count in counts_rules.items():
        inserted = rules[rule]
        new_counts_rules[rule[0] + inserted] += count
        new_counts_rules[inserted + rule[1]] += count
        new_counts_rules[rule] -= count
        new_counts_letters[inserted] += count

    return new_counts_rules, new_counts_letters


if __name__ == '__main__':
    with open('in.txt') as file:
        content = file.read()

    template, rules = content.split('\n\n')

    rules = [rule.split(' -> ') for rule in rules.splitlines()]
    rules = {rule[0]: rule[1] for rule in rules}

    part1(template, rules)
    part2(template, rules)
