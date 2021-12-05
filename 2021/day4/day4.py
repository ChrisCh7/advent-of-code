import copy


def part1(drawn_numbers, boards):
    boards = copy.deepcopy(boards)
    _, score = play_round(drawn_numbers, boards)
    print('Part 1:', score)


def part2(drawn_numbers, boards):
    boards = copy.deepcopy(boards)
    while len(boards) > 0:
        boards_round = copy.deepcopy(boards)
        winner_board, score = play_round(drawn_numbers, boards_round)
        boards.pop(winner_board)
        if len(boards) == 0:
            print('Part 2:', score)


def mark_number_on_boards(boards: list[list[list[list[int | bool]]]], number: int):
    boards_marked = boards

    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, nr in enumerate(row):
                if nr[0] == number:
                    boards_marked[i][j][k][1] = True

    return boards_marked


def check_winner(boards: list[list[list[list[int | bool]]]]):
    for i, board in enumerate(boards):
        winner_row = check_winner_rows(board)
        winner_col = check_winner_cols(board)

        if winner_row != -1:
            return i, winner_row, 'row'
        if winner_col != -1:
            return i, winner_col, 'col'

    return -1,


def check_winner_rows(board: list[list[list[int | bool]]]):
    for i, row in enumerate(board):
        if all(is_marked_number(nr) for nr in row):
            return i
    return -1


def check_winner_cols(board: list[list[list[int | bool]]]):
    for col in range(len(board[0])):
        marked_on_col = 0
        for row in range(len(board)):
            if is_marked_number(board[row][col]):
                marked_on_col += 1
        if marked_on_col == len(board):
            return col
    return -1


def sum_unmarked(board: list[list[list[int | bool]]]):
    sum_nr = 0
    for row in board:
        for nr in row:
            if not is_marked_number(nr):
                sum_nr += nr[0]
    return sum_nr


def is_marked_number(number: list[int | bool]):
    return number[1]


def play_round(drawn_numbers, boards):
    for nr in drawn_numbers:
        boards = mark_number_on_boards(boards, nr)
        winner = check_winner(boards)

        if winner[0] != -1:
            sum_unmarked_nrs = sum_unmarked(boards[winner[0]])
            return winner[0], sum_unmarked_nrs * nr


if __name__ == '__main__':
    with open('in.txt') as file:
        data = file.read()

    parts = data.split('\n\n')

    drawn_numbers = parts[0].split(',')
    drawn_numbers = list(map(int, drawn_numbers))

    boards = []

    for part in parts[1:]:
        board_rows = part.splitlines()
        board = [[[int(n), False] for n in row.split()] for row in board_rows]
        boards.append(board)

    part1(drawn_numbers, boards)
    part2(drawn_numbers, boards)
