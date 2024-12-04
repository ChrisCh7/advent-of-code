import itertools


def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)

    count = 0

    # for every position in the grid, check if the word can be found in any of the 8 directions
    for i in range(rows):
        for j in range(cols):
            for dx, dy in [direction for direction in itertools.product([1, -1, 0], repeat=2) if direction != (0, 0)]:
                if all(is_valid(i + k * dx, j + k * dy, rows, cols) and
                       grid[i + k * dx][j + k * dy] == word[k]
                       for k in range(word_len)):
                    count += 1

    return count


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def count_xmas_shapes(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def is_xmas_center(x, y):
        if not is_valid(x, y, rows, cols) or grid[x][y] != 'A':
            return False

        # diagonal positions relative to the center, top-left and bottom-right + top-right and bottom-left
        corners = [(x - 1, y - 1), (x + 1, y + 1),
                   (x - 1, y + 1), (x + 1, y - 1)]

        corner_letters = [grid[dx][dy] if is_valid(dx, dy, rows, cols) else None for dx, dy in corners]

        # pattern can be MAS or SAM
        valid_patterns = [
            ['M', 'S', 'S', 'M'],
            ['M', 'S', 'M', 'S'],
            ['S', 'M', 'M', 'S'],
            ['S', 'M', 'S', 'M'],
        ]

        return corner_letters in valid_patterns

    for i in range(rows):
        for j in range(cols):
            if is_xmas_center(i, j):
                count += 1

    return count


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    print('Part 1:', count_word_occurrences(lines, 'XMAS'))
    print('Part 2:', count_xmas_shapes(lines))
