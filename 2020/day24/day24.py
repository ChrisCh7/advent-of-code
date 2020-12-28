# TODO: find out why the answer is wrong

class Tile:
    def __init__(self):
        self.east = None
        self.southeast = None
        self.southwest = None
        self.west = None
        self.northwest = None
        self.northeast = None
        self.color = 'White'

    def dfs(self, node, visited: set, collector: list[str]):
        if node is not None and node not in visited:
            collector.append(node.color)
            visited.add(node)
            self.dfs(node.east, visited, collector)
            self.dfs(node.southeast, visited, collector)
            self.dfs(node.southwest, visited, collector)
            self.dfs(node.west, visited, collector)
            self.dfs(node.northwest, visited, collector)
            self.dfs(node.northeast, visited, collector)


def main(instructions):
    reference_tile = Tile()

    for instruction in instructions:
        flip_tile(instruction, reference_tile)

    colors = []
    reference_tile.dfs(reference_tile, set(), colors)

    print('Part 1:', colors.count('Black'))


def flip_tile(instruction, tile: Tile):
    direction = instruction[0]
    if direction in ['s', 'n']:
        direction = instruction[0:2]
    instruction = instruction[len(direction):]
    next_tile = connect(tile, direction)
    if len(instruction) == 0:
        flip(next_tile)
    else:
        flip_tile(instruction, next_tile)


def flip(tile: Tile):
    tile.color = 'White' if tile.color == 'Black' else 'Black'


def connect(tile: Tile, direction):
    if direction == 'e':
        if tile.east is None:
            next_tile = Tile()
            tile.east = next_tile
            next_tile.west = tile
        else:
            next_tile = tile.east
    elif direction == 'se':
        if tile.southeast is None:
            next_tile = Tile()
            tile.southeast = next_tile
            next_tile.northwest = tile
        else:
            next_tile = tile.southeast
    elif direction == 'sw':
        if tile.southwest is None:
            next_tile = Tile()
            tile.southwest = next_tile
            next_tile.northeast = tile
        else:
            next_tile = tile.southwest
    elif direction == 'w':
        if tile.west is None:
            next_tile = Tile()
            tile.west = next_tile
            next_tile.east = tile
        else:
            next_tile = tile.west
    elif direction == 'nw':
        if tile.northwest is None:
            next_tile = Tile()
            tile.northwest = next_tile
            next_tile.southeast = tile
        else:
            next_tile = tile.northwest
    elif direction == 'ne':
        if tile.northeast is None:
            next_tile = Tile()
            tile.northeast = next_tile
            next_tile.southwest = tile
        else:
            next_tile = tile.northeast
    connect_surrounding(next_tile)
    return next_tile


def connect_surrounding(tile: Tile):
    if tile.east is None:
        east = Tile()
        tile.east = east
        east.west = tile
    if tile.southeast is None:
        southeast = Tile()
        tile.southeast = southeast
        southeast.northwest = tile
    if tile.southwest is None:
        southwest = Tile()
        tile.southwest = southwest
        southwest.northeast = tile
    if tile.west is None:
        west = Tile()
        tile.west = west
        west.east = tile
    if tile.northwest is None:
        northwest = Tile()
        tile.northwest = northwest
        northwest.southeast = tile
    if tile.northeast is None:
        northeast = Tile()
        tile.northeast = northeast
        northeast.southwest = tile
    tile.east.northwest = tile.northeast
    tile.northeast.southeast = tile.east
    tile.northeast.west = tile.northwest
    tile.northwest.east = tile.northeast
    tile.northwest.southwest = tile.west
    tile.west.northeast = tile.northwest
    tile.west.southeast = tile.southwest
    tile.southwest.northwest = tile.west
    tile.southwest.east = tile.southeast
    tile.southeast.west = tile.southwest
    tile.southeast.northeast = tile.east
    tile.east.southwest = tile.southeast


if __name__ == '__main__':
    with open('in.txt') as file:
        instructions = file.read().splitlines()

    main(instructions)
