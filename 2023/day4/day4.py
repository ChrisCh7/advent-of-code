import re


def part1(cards: list[tuple[tuple[int, ...], ...]]):
    points_total = 0

    for winning_nrs, owned_nrs in cards:
        points_card = 0

        for nr in owned_nrs:
            if nr in winning_nrs:
                if points_card == 0:
                    points_card += 1
                else:
                    points_card *= 2

        points_total += points_card

    print('Part 1:', points_total)


def part2(cards: list[tuple[tuple[int, ...], ...]]):
    cards_og = cards.copy()

    card_idxs = {card: i for i, card in enumerate(cards)}

    nr_cards = 0

    for card in cards:
        nr_cards += 1
        winning_nrs, owned_nrs = map(set, card)

        matching_nrs = len(winning_nrs & owned_nrs)

        for i in range(matching_nrs):
            cards.append(cards_og[card_idxs[card] + i + 1])

    print('Part 2:', nr_cards)


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    cards = [line.split(':')[1].split('|') for line in lines]
    cards = [tuple(tuple(map(int, re.findall(r'\d+', nrs))) for nrs in line) for line in cards]

    part1(cards)
    part2(cards)
