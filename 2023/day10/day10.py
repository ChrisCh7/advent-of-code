if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    tiles = [list(line) for line in lines]

    for i, line in enumerate(tiles):
        if 'S' not in line:
            continue
        s_pos = i, line.index('S')
        break

    current_pos = (s_pos[0] + 1, s_pos[1])
    nr_steps = 1
    visited = {current_pos}
    valid_idx = lambda idx: 0 <= idx[0] < len(tiles) and 0 <= idx[1] < len(tiles[0])

    while current_pos != s_pos:
        match tiles[current_pos[0]][current_pos[1]]:
            case '|':
                option1 = (current_pos[0] + 1, current_pos[1])
                option2 = (current_pos[0] - 1, current_pos[1])
                current_pos = option1 if valid_idx(option1) and option1 not in visited else option2
            case '-':
                option1 = (current_pos[0], current_pos[1] + 1)
                option2 = (current_pos[0], current_pos[1] - 1)
                current_pos = option1 if valid_idx(option1) and option1 not in visited else option2
            case 'L':
                option1 = (current_pos[0], current_pos[1] + 1)
                option2 = (current_pos[0] - 1, current_pos[1])
                current_pos = option1 if valid_idx(option1) and option1 not in visited else option2
            case 'J':
                option1 = (current_pos[0] - 1, current_pos[1])
                option2 = (current_pos[0], current_pos[1] - 1)
                current_pos = option1 if valid_idx(option1) and option1 not in visited else option2
            case '7':
                option1 = (current_pos[0], current_pos[1] - 1)
                option2 = (current_pos[0] + 1, current_pos[1])
                current_pos = option1 if valid_idx(option1) and option1 not in visited else option2
            case 'F':
                option1 = (current_pos[0] + 1, current_pos[1])
                option2 = (current_pos[0], current_pos[1] + 1)
                current_pos = option1 if valid_idx(option1) and option1 not in visited else option2

        visited.add(current_pos)
        nr_steps += 1

    print('Part 1:', nr_steps // 2)

    nr_enclosed_tiles = 0

    for i in range(len(tiles)):
        enclosed_flag = False
        for j in range(len(tiles[0])):
            if tiles[i][j] in 'S|7F' and (i, j) in visited:
                enclosed_flag = not enclosed_flag
            if (i, j) not in visited and enclosed_flag:
                nr_enclosed_tiles += 1

    print('Part 2:', nr_enclosed_tiles)
