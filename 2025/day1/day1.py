import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    current = 50
    left_at_zero_count = 0
    passed_by_zero_count = 0

    logger.debug(f"At position: {current}")

    for line in lines:
        logger.debug(f"Instruction: {line}")
        direction = line[0]
        distance = int(line[1:])
        start = current

        if direction == 'L':
            current -= distance
        else:
            current += distance

        logger.debug(f"After movement before modulo: {current}")
        new_current = current % 100

        if direction == 'R':
            first_hit = (100 - start) % 100
        else:
            first_hit = start % 100

        if first_hit == 0:
            first_hit = 100

        if first_hit < distance:
            passed_by_zero = 1 + (distance - 1 - first_hit) // 100
        else:
            passed_by_zero = 0

        logger.debug(f"Passed by zero {passed_by_zero} times")
        passed_by_zero_count += passed_by_zero

        current = new_current

        logger.debug(f"At position: {current}")

        if current == 0:
            left_at_zero_count += 1

    print('Part 1:', left_at_zero_count)
    print('Part 2:', left_at_zero_count + passed_by_zero_count)
