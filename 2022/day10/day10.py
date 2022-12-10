def get_screen_pos(cycle: int):
    return (cycle // 40, cycle % 40 - 1)


if __name__ == '__main__':
    with open('in.txt') as file:
        program = [instr.split() for instr in file.read().splitlines()]

    X = 1

    cycle = 1
    signal_strengths = []

    task = None
    done = False
    instruction_index = -1
    screen = [['.'] * 40 for _ in range(6)]

    while not done:
        if cycle % 40 - 1 in [X, X - 1, X + 1]:
            screen_pos = get_screen_pos(cycle)
            screen[screen_pos[0]][screen_pos[1]] = '#'
        if cycle == 20 or (cycle - 20) % 40 == 0:
            signal_strengths.append(cycle * X)
        if task is None:
            instruction_index += 1
            if instruction_index >= len(program):
                done = True
                continue
            instruction = program[instruction_index]
            if instruction[0] != 'noop':
                task = int(instruction[1]), cycle + 1
        else:
            if cycle == task[1]:
                X += task[0]
                task = None
        cycle += 1

    print('Part 1:', sum(signal_strengths[:6]))

    print('Part 2:')
    for row in screen:
        print(''.join(row))
