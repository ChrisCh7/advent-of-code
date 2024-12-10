from collections import defaultdict

trailhead_scores = defaultdict(set)
trailhead_ratings = defaultdict(set)


def is_valid_pos(map, i, j):
    return 0 <= i < len(map) and 0 <= j < len(map[0])


def get_surrounding_coords(map, i, j):
    return [(i2, j2) for (i2, j2) in [
        (i, j + 1),
        (i + 1, j),
        (i, j - 1),
        (i - 1, j)
    ] if is_valid_pos(map, i2, j2)]


def explore_trail(map, i, j, start_i, start_j, last_height, current_trail):
    if map[i][j] != last_height + 1:
        return

    new_trail = current_trail + [(i, j)]

    if map[i][j] == 9:
        trailhead_scores[(start_i, start_j)].add((i, j))
        trailhead_ratings[(start_i, start_j)].add(tuple(new_trail))
        return

    for new_pos in get_surrounding_coords(map, i, j):
        explore_trail(map, new_pos[0], new_pos[1], start_i, start_j, map[i][j], new_trail)


def get_trailhead_score_and_rating(map, i, j):
    for pos in get_surrounding_coords(map, i, j):
        explore_trail(map, pos[0], pos[1], i, j, 0, [])
    return len(trailhead_scores[(i, j)]), len(trailhead_ratings[(i, j)])


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    map = [[int(n) for n in line] for line in lines]

    score_sum = 0
    rating_sum = 0

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != 0:
                continue

            trailhead_score, trailhead_rating = get_trailhead_score_and_rating(map, i, j)

            score_sum += trailhead_score
            rating_sum += trailhead_rating

    print('Part 1:', score_sum)
    print('Part 2:', rating_sum)
