import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def is_repeated_pattern(s: str) -> bool:
    return s in (s + s)[1:-1]


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    ranges = lines[0].split(',')
    for i, rnge in enumerate(ranges):
        a, b = rnge.split('-')
        ranges[i] = (int(a), int(b))

    invalid_id_sum = 0
    invalid_id_sum_p2 = 0
    for rnge in ranges:
        for nr in range(rnge[0], rnge[1] + 1):
            nr = str(nr)
            logger.debug(f"Checking id: {nr}")
            logger.debug(f"{nr[:len(nr) // 2]} == {nr[len(nr) // 2:]}?")
            if nr[:len(nr) // 2] == nr[len(nr) // 2:]:
                logger.debug(f"Invalid id: {nr}")
                invalid_id_sum += int(nr)
            if is_repeated_pattern(nr):
                logger.debug(f"Invalid id (p2): {nr}")
                invalid_id_sum_p2 += int(nr)

    print('Part 1:', invalid_id_sum)
    print('Part 2:', invalid_id_sum_p2)
