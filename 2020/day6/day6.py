def part1():
    with open('in.txt') as file:
        data = file.read()

    groups = data.split('\n\n')
    groups = [group.replace('\n', '') for group in groups]

    yes_answers = []
    for group in groups:
        questions_answered_yes = set()
        for question in group:
            questions_answered_yes.add(question)
        yes_answers.append(questions_answered_yes)

    yes_count = 0
    for answers in yes_answers:
        yes_count += len(answers)

    print(yes_count)


def part2():
    with open('in.txt') as file:
        data = file.read()

    groups = data.split('\n\n')
    groups = [group.split() for group in groups]

    yes_count = 0
    for group in groups:
        yes_answers = list(group[0])
        for person in group:
            for answer in yes_answers.copy():
                if answer not in person:
                    yes_answers.remove(answer)
        yes_count += len(yes_answers)

    print(yes_count)


if __name__ == '__main__':
    part1()
    part2()
