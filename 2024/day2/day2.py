def is_safe(report):
    return (levels_all_increasing_or_all_decreasing(report) and
            any_two_adjacent_levels_differ_by_at_least_one_and_at_most_three(report))


def levels_all_increasing_or_all_decreasing(report):
    return report == sorted(report) or report == sorted(report, reverse=True)


def any_two_adjacent_levels_differ_by_at_least_one_and_at_most_three(report):
    for i in range(len(report) - 1):
        if not 1 <= abs(report[i] - report[i + 1]) <= 3:
            return False
    return True


def is_safe_p2(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        report_with_a_level_removed = report[:i] + report[i + 1:]
        if is_safe(report_with_a_level_removed):
            return True

    return False


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    reports = [[int(n) for n in line.split()] for line in lines]

    print('Part 1:', sum(is_safe(report) for report in reports))
    print('Part 2:', sum(is_safe_p2(report) for report in reports))
