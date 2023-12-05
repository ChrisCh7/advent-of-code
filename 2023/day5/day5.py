from multiprocessing import Pool


def get_map_value(section: list[list[int]], query: int):
    value = query

    for destination, source, rnge in section:
        if source <= query < source + rnge:
            value = destination + query - source
            break

    return value


def get_location(seed: int, sections: list[list[list[int]]]):
    soil = get_map_value(sections[1], seed)
    fertilizer = get_map_value(sections[2], soil)
    water = get_map_value(sections[3], fertilizer)
    light = get_map_value(sections[4], water)
    temperature = get_map_value(sections[5], light)
    humidity = get_map_value(sections[6], temperature)
    location = get_map_value(sections[7], humidity)
    return location


def get_min_location_p2(value: int, sections: list[list[list[int]]]):
    min_location = 10 ** 100

    for i in range(sections[0][sections[0].index(value) + 1]):
        seed = value + i

        location = get_location(seed, sections)

        if location < min_location:
            min_location = location

    return min_location


if __name__ == '__main__':
    with open('in.txt') as file:
        sections = file.read().split('\n\n')

    sections[0] = list(map(int, sections[0].split(':')[1][1:].split()))

    for i in range(1, len(sections)):
        sections[i] = [list(map(int, line.split())) for line in sections[i].splitlines()[1:]]

    locations = []

    for seed in sections[0]:
        location = get_location(seed, sections)
        locations.append(location)

    print('Part 1:', min(locations))

    with Pool(10) as p:
        min_locations = p.starmap(get_min_location_p2, [[value, sections] for value in sections[0][::2]])

    print('Part 2:', min(min_locations))
