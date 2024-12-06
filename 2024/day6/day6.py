import copy


def is_in_bounds(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    positions = [list(line) for line in lines]
    og_positions = copy.deepcopy(positions)

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }
    next_guard_symbol = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }

    current_direction = None
    current_position = None
    current_guard_symbol = None
    starting_direction = None
    starting_position = None
    starting_guard_symbol = None

    for i, row in enumerate(positions):
        for j, pos in enumerate(row):
            if pos not in ['.', '#']:
                current_direction = directions[pos]
                starting_direction = current_direction
                current_position = (i, j)
                starting_position = current_position
                current_guard_symbol = pos
                starting_guard_symbol = current_guard_symbol
                break
        if current_direction is not None:
            break

    visited_positions = set()
    visited_positions.add(current_position)

    while True:
        # uncomment to visualize the guard's movement
        # import os
        # import time
        # os.system('cls')
        # print(f'Visited positions: {len(visited_positions)}')
        # print(*[''.join(row) for row in positions], sep='\n')
        # time.sleep(0.2)

        next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])

        if not is_in_bounds(next_position[0], next_position[1], len(positions), len(positions[0])):
            break

        if positions[next_position[0]][next_position[1]] == '.':
            positions[current_position[0]][current_position[1]] = '.'
            current_position = next_position
            visited_positions.add(current_position)
            positions[current_position[0]][current_position[1]] = current_guard_symbol
        else:
            current_guard_symbol = next_guard_symbol[current_guard_symbol]
            current_direction = directions[current_guard_symbol]
            positions[current_position[0]][current_position[1]] = current_guard_symbol

    print('Part 1:', len(visited_positions))

    obstruction_positions = []

    for i in range(len(positions)):
        for j in range(len(positions[0])):
            if (i, j) == starting_position or positions[i][j] == '#':
                continue

            positions = copy.deepcopy(og_positions)
            positions[starting_position[0]][starting_position[1]] = '.'
            positions[i][j] = '#'

            current_direction = starting_direction
            current_position = starting_position
            current_guard_symbol = starting_guard_symbol

            visited_positions = set()
            visited_positions.add(current_position)

            looping = False
            already_visited_previous_and_current = [False, False]
            visited_positions_directions = {}

            while True:
                next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])

                if not is_in_bounds(next_position[0], next_position[1], len(positions), len(positions[0])):
                    break

                if positions[next_position[0]][next_position[1]] == '.':
                    current_position = next_position

                    if current_position in visited_positions and current_position != starting_position:
                        already_visited_previous_and_current.pop(0)
                        already_visited_previous_and_current.append(True)
                        if (all(already_visited_previous_and_current) and
                                current_direction == visited_positions_directions[current_position]):
                            looping = True
                            break
                    else:
                        already_visited_previous_and_current.pop(0)
                        already_visited_previous_and_current.append(False)

                    if current_position not in visited_positions:
                        visited_positions_directions[current_position] = current_direction

                    visited_positions.add(current_position)
                else:
                    current_guard_symbol = next_guard_symbol[current_guard_symbol]
                    current_direction = directions[current_guard_symbol]

            if looping:
                obstruction_positions.append((i, j))

    print('Part 2:', len(obstruction_positions))
