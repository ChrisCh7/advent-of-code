from collections import deque


def bfs(start_pos: tuple[int, int], heightmap: list[list[str]]):
    paths = deque([[start_pos]])
    seen = {start_pos}
    while paths:
        path = paths.popleft()
        i, j = path[-1]
        if heightmap[i][j] == "E":
            return path
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if (0 <= x < len(heightmap) and 0 <= y < len(heightmap[0]) and
                    get_height(heightmap[x][y]) - get_height(heightmap[i][j]) < 2 and (x, y) not in seen):
                paths.append(path + [(x, y)])
                seen.add((x, y))


def get_height(letter: str):
    if letter == 'S':
        return ord('a')
    elif letter == 'E':
        return ord('z')
    else:
        return ord(letter)


if __name__ == '__main__':
    with open('in.txt') as file:
        heightmap = [list(line) for line in file.read().splitlines()]

    for part, start_letters in enumerate(['S', 'Sa']):
        start_pos = [(i, j) for j in range(len(heightmap[0])) for i in range(len(heightmap))
                     if heightmap[i][j] in start_letters]
        print(f'Part {part + 1}:', min(len(path) - 1 for pos in start_pos if (path := bfs(pos, heightmap)) is not None))
