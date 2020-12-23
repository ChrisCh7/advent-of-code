def main():
    with open('in.txt') as file:
        tiles = file.read().split('\n\n')

    tiles = {int(tile[tile.find('e ') + 2:tile.find(':')]): tile[tile.find(':') + 2:].splitlines() for tile in tiles}

    variations = dict()
    for tile in tiles:
        variations[tile] = [tiles[tile][0], tiles[tile][0][::-1], tiles[tile][-1], tiles[tile][-1][::-1],
                            ''.join([tiles[tile][i][0] for i in range(len(tiles[tile]))]),
                            ''.join([tiles[tile][i][0] for i in range(len(tiles[tile]))])[::-1],
                            ''.join([tiles[tile][i][-1] for i in range(len(tiles[tile]))]),
                            ''.join([tiles[tile][i][-1] for i in range(len(tiles[tile]))])[::-1]]

    product = 1
    for tile in variations:
        count = 0
        for til in [t for t in variations if t != tile]:
            for i in range(8):
                if variations[tile][i] in variations[til]:
                    count += 1
                    # print(tile, 'touches', til)
                    break
        if count == 2:
            # print(tile, count)
            product *= tile

    print('Part 1:', product)


if __name__ == '__main__':
    main()
