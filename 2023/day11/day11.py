import copy
from itertools import combinations

import numpy as np
from scipy.spatial.distance import cityblock

if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    image = [list(line) for line in lines]
    image_og = copy.deepcopy(image)

    galaxy_coords_preexpansion = []
    for i, line in enumerate(image):
        for j, character in enumerate(line):
            if character == '#':
                galaxy_coords_preexpansion.append((j, len(image) - i - 1))

    # vertical expansion
    new_image = []
    for row in image:
        if '#' in row:
            new_image.append(row)
        else:
            new_image.append(row)
            new_image.append(row)
    image = new_image
    # horizontal expansion
    new_image = []
    for column in zip(*image):
        if '#' in column:
            new_image.append(column)
        else:
            new_image.append(column)
            new_image.append(column)
    image = list(zip(*new_image))

    galaxy_coords = []
    for i, line in enumerate(image):
        for j, character in enumerate(line):
            if character == '#':
                galaxy_coords.append((j, len(image) - i - 1))

    distances = []
    for p1, p2 in combinations(galaxy_coords, 2):
        distances.append(cityblock(p1, p2))

    print('Part 1:', sum(distances))

    image = copy.deepcopy(image_og)
    width = len(image[0])
    height = len(image)
    current_x = 0
    current_y = 0
    galaxy_coords = galaxy_coords_preexpansion.copy()
    expand_by = 1000000 - 1
    # horizontal expansion
    while current_x < width:
        if not any(g[0] == current_x for g in galaxy_coords):
            width += expand_by
            for i, galaxy in enumerate(galaxy_coords):
                if galaxy[0] > current_x:
                    galaxy_coords[i] = (galaxy[0] + expand_by, galaxy[1])
            current_x += expand_by
        current_x += 1
    # vertical expansion
    while current_y < height:
        if not any(g[1] == current_y for g in galaxy_coords):
            height += expand_by
            for i, galaxy in enumerate(galaxy_coords):
                if galaxy[1] > current_y:
                    galaxy_coords[i] = (galaxy[0], galaxy[1] + expand_by)
            current_y += expand_by
        current_y += 1

    distances = []
    for p1, p2 in combinations(galaxy_coords, 2):
        distances.append(cityblock(p1, p2))

    print('Part 2:', sum(np.array(distances, dtype=np.int64)))
