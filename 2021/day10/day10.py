from collections import deque


def part1(lines: list[str], symbol_pairs: dict[str, str]):
    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for line in lines:
        result = classify_line(line, symbol_pairs)
        match result:
            case ['corrupt', char]:
                score += score_table[char]
            case _:
                pass

    print('Part 1:', score)


def part2(lines: list[str], symbol_pairs: dict[str, str]):
    score_table = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []

    for line in lines:
        result = classify_line(line, symbol_pairs)
        match result:
            case ['incomplete', completion_string]:
                score = 0
                for char in completion_string:
                    score *= 5
                    score += score_table[char]
                scores.append(score)
            case _:
                pass

    scores = sorted(scores)
    print('Part 2:', scores[len(scores) // 2])


def classify_line(line: str, symbol_pairs: dict[str, str]):
    symbols = deque()
    classification = []

    for char in line:
        if char in symbol_pairs:
            symbols.append(char)
        else:
            if len(symbols) == 0:
                classification = ['corrupt', char]
                break
            else:
                if symbol_pairs[symbols[-1]] == char:
                    symbols.pop()
                else:
                    classification = ['corrupt', char]
                    break

    if len(classification) == 0 and len(symbols) == 0:
        classification = ['ok']
    elif len(classification) == 0 and len(symbols) != 0:
        classification = ['incomplete', ''.join(reversed(''.join(symbols).translate(str.maketrans(symbol_pairs))))]

    return classification


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    symbol_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

    part1(lines, symbol_pairs)
    part2(lines, symbol_pairs)
