from math import prod

if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    games = [line.split(':')[1][1:] for line in lines]
    games = [game.split('; ') for game in games]
    games = [[reveal.split(', ') for reveal in game] for game in games]
    games = [[[cube_type.split() for cube_type in reveal] for reveal in game] for game in games]
    games = [[[[int(cube_type[0]), cube_type[1]] for cube_type in reveal] for reveal in game] for game in games]

    max_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    possible_ids = []
    powers = []

    for i, game in enumerate(games):
        possible_game = True

        max_cubes_game = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for reveal in game:
            for cube_count, cube_type in reveal:
                if cube_count > max_cubes[cube_type]:
                    possible_game = False
                if cube_count > max_cubes_game[cube_type]:
                    max_cubes_game[cube_type] = cube_count

        if possible_game:
            possible_ids.append(i + 1)

        power = prod(max_cubes_game.values())
        powers.append(power)

    print('Part 1:', sum(possible_ids))
    print('Part 2:', sum(powers))
