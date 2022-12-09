def part1(motions: list[list[str | int]]):
    head = [0, 0]
    tail = [0, 0]

    visited = [(0, 0)]

    for motion in motions:
        match motion:
            case ['R', n]:
                for _ in range(n):
                    head[1] += 1
                    move_tail(head, tail)
                    visited.append(tuple(tail))
            case ['L', n]:
                for _ in range(n):
                    head[1] -= 1
                    move_tail(head, tail)
                    visited.append(tuple(tail))
            case ['U', n]:
                for _ in range(n):
                    head[0] -= 1
                    move_tail(head, tail)
                    visited.append(tuple(tail))
            case ['D', n]:
                for _ in range(n):
                    head[0] += 1
                    move_tail(head, tail)
                    visited.append(tuple(tail))

    print('Part 1:', len(set(visited)))


def part2(motions: list[list[str | int]]):
    head = [0, 0]
    tails = [[0, 0] for _ in range(9)]
    visited = [(0, 0)]

    for motion in motions:
        match motion:
            case ['R', n]:
                for _ in range(n):
                    head[1] += 1
                    current_head = head
                    for i in range(len(tails)):
                        move_tail(current_head, tails[i])
                        current_head = tails[i]
                    visited.append(tuple(tails[8]))
            case ['L', n]:
                for _ in range(n):
                    head[1] -= 1
                    current_head = head
                    for i in range(len(tails)):
                        move_tail(current_head, tails[i])
                        current_head = tails[i]
                    visited.append(tuple(tails[8]))
            case ['U', n]:
                for _ in range(n):
                    head[0] -= 1
                    current_head = head
                    for i in range(len(tails)):
                        move_tail(current_head, tails[i])
                        current_head = tails[i]
                    visited.append(tuple(tails[8]))
            case ['D', n]:
                for _ in range(n):
                    head[0] += 1
                    current_head = head
                    for i in range(len(tails)):
                        move_tail(current_head, tails[i])
                        current_head = tails[i]
                    visited.append(tuple(tails[8]))

    print('Part 2:', len(set(visited)))


def move_tail(head: list[int], tail: list[int]):
    y_diff = head[0] - tail[0]
    x_diff = head[1] - tail[1]
    if abs(x_diff) > 1 and abs(y_diff) > 1:
        if abs(x_diff) == abs(y_diff):
            tail[1] += x_diff
            tail[1] = tail[1] - 1 if x_diff > 0 else tail[1] + 1
            tail[0] += y_diff
            tail[0] = tail[0] - 1 if y_diff > 0 else tail[0] + 1
        elif abs(x_diff) > abs(y_diff):
            tail[1] += x_diff
            tail[1] = tail[1] - 1 if x_diff > 0 else tail[1] + 1
            tail[0] += y_diff
        else:
            tail[1] += x_diff
            tail[0] += y_diff
            tail[0] = tail[0] - 1 if y_diff > 0 else tail[0] + 1
    elif abs(x_diff) > 1 and abs(y_diff) == 1:
        tail[1] += x_diff
        tail[1] = tail[1] - 1 if x_diff > 0 else tail[1] + 1
        tail[0] += y_diff
    elif abs(y_diff) > 1 and abs(x_diff) == 1:
        tail[1] += x_diff
        tail[0] += y_diff
        tail[0] = tail[0] - 1 if y_diff > 0 else tail[0] + 1
    elif abs(x_diff) > 1:
        tail[1] += x_diff
        tail[1] = tail[1] - 1 if x_diff > 0 else tail[1] + 1
    elif abs(y_diff) > 1:
        tail[0] += y_diff
        tail[0] = tail[0] - 1 if y_diff > 0 else tail[0] + 1


if __name__ == '__main__':
    with open('in.txt') as file:
        motions = [[line.split()[0], int(line.split()[1])] for line in file.read().splitlines()]

    part1(motions)
    part2(motions)
