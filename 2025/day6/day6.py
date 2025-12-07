import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    lines = [[el.strip() for el in line.split()] for line in lines]
    logger.debug(lines)

    results = []
    for i in range(len(lines[0])):
        vertical_line = [line[i] for line in lines]
        logger.debug(vertical_line)
        numbers = list(map(int, vertical_line[:-1]))
        sign = vertical_line[-1]
        match sign:
            case '+':
                result = sum(numbers)
            case '*':
                result = 1
                for n in numbers:
                    result *= n
        results.append(result)
        logger.debug(f' {sign} '.join(map(str, numbers)) + f" = {result}")

    print('Part 1:', sum(results))

    logger.debug('-' * 50)
    with open('in.txt') as file:
        lines = file.read().splitlines()
    logger.debug(lines)

    lines = [list(line) for line in lines]
    logger.debug(lines)

    results = []
    numbers = []
    for i in range(len(lines[0]) - 1, -1, -1):
        column = ''.join(line[i] for line in lines).strip()
        logger.debug(column)
        if column == '':
            numbers = []
            continue
        if column[-1] in '+*':
            sign = column[-1]
            column = column[:-1].strip()
            numbers.append(int(column))
            match sign:
                case '+':
                    result = sum(numbers)
                case '*':
                    result = 1
                    for n in numbers:
                        result *= n
            results.append(result)
            logger.debug(f' {sign} '.join(map(str, numbers)) + f" = {result}")
        else:
            numbers.append(int(column))

    print('Part 2:', sum(results))
