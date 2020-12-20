import re


def main(rules_og, messages):
    rules = rules_og.copy()

    # after 5 replacement passes, the answer doesn't change
    # because all the replacements after that are done after the message max length
    for _ in range(5):
        for rule in rules:
            for rul in [r for r in rules if r != rule]:
                rules[rul] = re.sub(rf'\b{rule}\b', rf'({rules[rule]})', rules[rul])

    for rule in rules:
        rules[rule] = rules[rule].replace(' ', '').replace('"', '').replace('(a)', 'a').replace('(b)', 'b')

    count = 0
    for message in messages:
        if re.fullmatch(rules[0], message) is not None:
            count += 1

    return count


if __name__ == '__main__':
    with open('in.txt') as file:
        rules, messages = file.read().split('\n\n')

    rules = [rule.strip() for rule in rules.splitlines()]
    messages = [message.strip() for message in messages.splitlines()]

    rules = {int(rule[:rule.index(':')]): rule[rule.index(':') + 2:] for rule in rules}

    part1 = main(rules, messages)
    print('Part 1:', part1)

    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'

    part2 = main(rules, messages)
    print('Part 2:', part2)
