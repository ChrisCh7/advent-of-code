from collections import defaultdict

if __name__ == '__main__':
    with open('in.txt') as file:
        rules, updates = file.read().split('\n\n')

    rules = [[int(n) for n in rule.split('|')] for rule in rules.splitlines()]
    updates = [[int(n) for n in update.split(',')] for update in updates.splitlines()]

    rules_dict = defaultdict(set)

    for rule in rules:
        rules_dict[rule[0]].add(rule[1])

    correct_updates = []
    incorrect_updates = []

    for update in updates:
        is_correct = True
        for i in range(len(update) - 1):
            if update[i + 1] not in rules_dict[update[i]]:
                is_correct = False
                break
        if is_correct:
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)

    print('Part 1:', sum(update[len(update) // 2] for update in correct_updates))

    for i, update in enumerate(incorrect_updates):
        is_correct = False
        while not is_correct:
            for j in range(len(update) - 1):
                if update[j + 1] not in rules_dict[update[j]]:
                    update[j], update[j + 1] = update[j + 1], update[j]
            if all(update[j + 1] in rules_dict[update[j]] for j in range(len(update) - 1)):
                is_correct = True

        incorrect_updates[i] = update

    print('Part 2:', sum(update[len(update) // 2] for update in incorrect_updates))
