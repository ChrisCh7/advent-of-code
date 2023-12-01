import regex as re

if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    sum_p1 = 0
    sum_p2 = 0

    for line in lines:
        matches = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)

        matches_p1 = list(filter(lambda d: d.isdigit(), matches))
        sum_p1 += int(matches_p1[0] + matches_p1[-1])

        matches_p2 = list(map(lambda m: m.replace('one', '1')
                              .replace('two', '2')
                              .replace('three', '3')
                              .replace('four', '4')
                              .replace('five', '5')
                              .replace('six', '6')
                              .replace('seven', '7')
                              .replace('eight', '8')
                              .replace('nine', '9'), matches))
        sum_p2 += int(matches_p2[0] + matches_p2[-1])

    print('Part 1:', sum_p1)
    print('Part 2:', sum_p2)
