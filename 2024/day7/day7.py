import itertools
import multiprocessing


def determine_equation_truth(test_value, nrs):
    operator_possibilities = list(itertools.product(['+', '*'], repeat=len(nrs) - 1))
    for operator_possibility in operator_possibilities:
        acc = nrs[0]
        for i, operator in enumerate(operator_possibility):
            match operator:
                case '+':
                    acc += nrs[i + 1]
                case '*':
                    acc *= nrs[i + 1]
        if test_value == acc:
            return True, test_value
    return False, None


def determine_equation_truth_p2(test_value, nrs):
    operator_possibilities = list(itertools.product(['+', '*', '||'], repeat=len(nrs) - 1))
    for operator_possibility in operator_possibilities:
        acc = nrs[0]
        for i, operator in enumerate(operator_possibility):
            match operator:
                case '+':
                    acc += nrs[i + 1]
                case '*':
                    acc *= nrs[i + 1]
                case '||':
                    acc = int(str(acc) + str(nrs[i + 1]))
        if test_value == acc:
            return True, test_value
    return False, None


def do_part(part, lines):
    f = determine_equation_truth if part == 1 else determine_equation_truth_p2

    with multiprocessing.Pool() as pool:
        results = pool.starmap(f, lines)

    true_equations_counter = 0
    total_calibration_result = 0

    for true_eq, test_value in results:
        if true_eq:
            true_equations_counter += 1
            total_calibration_result += test_value

    print(f'Part {part}: {total_calibration_result}, true equations: {true_equations_counter}')


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    lines = [line.split(':') for line in lines]

    for i, line in enumerate(lines):
        test_value = int(line[0])
        nrs = [int(n) for n in line[1].strip().split()]
        lines[i] = [test_value, nrs]

    do_part(1, lines)
    do_part(2, lines)
