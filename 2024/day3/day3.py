import re

if __name__ == '__main__':
    with open('in.txt') as file:
        program = file.read()

    matches = re.findall(r'mul\((\d+),(\d+)\)', program)
    pairs = [list(map(int, pair)) for pair in matches]

    print('Part 1:', sum(pair[0] * pair[1] for pair in pairs))

    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", program)

    result = 0
    do = True

    for m in matches:
        match m:
            case (a, b, '', ''):
                if do:
                    result += int(a) * int(b)
            case ('', '', 'do()', ''):
                do = True
            case ('', '', '', "don't()"):
                do = False

    print('Part 2:', result)
