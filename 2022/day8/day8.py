import numpy as np


def part1(trees):
    visible = 0
    for i, line in enumerate(trees):
        for j, tree in enumerate(line):
            if (all(t < tree for t in trees[i, 0:j]) or
                    all(t < tree for t in trees[i, j + 1:trees.shape[1]]) or
                    all(t < tree for t in trees[0:i, j]) or
                    all(t < tree for t in trees[i + 1:trees.shape[0], j])):
                visible += 1

    print('Part 1:', visible)


def part2(trees):
    scenic_scores = []

    for i, line in enumerate(trees):
        for j, tree in enumerate(line):
            scenic_scores.append(visible_trees(tree, trees[i, 0:j][::-1]) *
                                 visible_trees(tree, trees[i, j + 1:trees.shape[1]]) *
                                 visible_trees(tree, trees[0:i, j][::-1]) *
                                 visible_trees(tree, trees[i + 1:trees.shape[0], j]))

    print('Part 2:', max(scenic_scores))


def visible_trees(tree, trees):
    counter = 0
    for t in trees:
        counter += 1
        if t >= tree:
            break
    return counter


if __name__ == '__main__':
    with open('in.txt') as file:
        trees = [list(map(int, line)) for line in file.read().splitlines()]

    trees = np.array(trees)

    part1(trees)
    part2(trees)
