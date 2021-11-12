from collections import defaultdict


def part1(wire1_moves, wire2_moves):
    board = defaultdict(list)
    board[(0, 0)] = [1, 2]

    make_moves(1, wire1_moves, board)
    make_moves(2, wire2_moves, board)

    intersections = [position for position in board if
                     1 in board[position] and 2 in board[position] and position != (0, 0)]
    distances = [manhattan_distance(x, y) for (x, y) in intersections]
    print('Part 1:', min(distances))


def part2(wire1_moves, wire2_moves):
    board = defaultdict(lambda: [0, 0])

    make_moves_part2(1, wire1_moves, board)
    make_moves_part2(2, wire2_moves, board)

    intersections = [position for position in board if
                     0 not in board[position] and 0 not in board[position]]

    sums = [sum(board[position]) for position in intersections]
    print('Part 2:', min(sums))


def make_moves(wire: int, moves: list[list[str]], board: dict[tuple[int, int], list[int]]):
    current_position = (0, 0)
    for move in moves:
        match move:
            case ['R', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0] + 1, current_position[1])
                    board[current_position].append(wire)
            case ['L', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0] - 1, current_position[1])
                    board[current_position].append(wire)
            case ['U', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0], current_position[1] + 1)
                    board[current_position].append(wire)
            case ['D', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0], current_position[1] - 1)
                    board[current_position].append(wire)


def make_moves_part2(wire: int, moves: list[list[str]], board: dict[tuple[int, int], list[int]]):
    current_position = (0, 0)
    current_move_counter = 0

    for move in moves:
        match move:
            case ['R', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0] + 1, current_position[1])
                    current_move_counter += 1
                    if board[current_position][wire - 1] == 0:
                        board[current_position][wire - 1] = current_move_counter
            case ['L', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0] - 1, current_position[1])
                    current_move_counter += 1
                    if board[current_position][wire - 1] == 0:
                        board[current_position][wire - 1] = current_move_counter
            case ['U', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0], current_position[1] + 1)
                    current_move_counter += 1
                    if board[current_position][wire - 1] == 0:
                        board[current_position][wire - 1] = current_move_counter
            case ['D', amount]:
                for i in range(int(amount)):
                    current_position = (current_position[0], current_position[1] - 1)
                    current_move_counter += 1
                    if board[current_position][wire - 1] == 0:
                        board[current_position][wire - 1] = current_move_counter


def manhattan_distance(x, y):
    """Manhattan distance from origin to a point(x, y)"""
    return abs(0 - x) + abs(0 + y)


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    wire1 = lines[0]
    wire2 = lines[1]

    wire1_moves = [[move[0], move[1:]] for move in wire1.split(',')]
    wire2_moves = [[move[0], move[1:]] for move in wire2.split(',')]

    part1(wire1_moves, wire2_moves)
    part2(wire1_moves, wire2_moves)
