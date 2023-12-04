import copy
import re


def part1(cards: list[list[list[int]]]):
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


def part2(cards: list[list[list[int]]]):
    cards_og = copy.deepcopy(cards)

    nr_cards = 0

    for card in cards:
        nr_cards += 1
        winning_nrs, owned_nrs = card
        matching_nrs = 0

        for nr in owned_nrs:
            if nr in winning_nrs:
                matching_nrs += 1

        for i in range(matching_nrs):
            cards.append(cards_og[cards_og.index(card) + i + 1])

    print('Part 2:', nr_cards)


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    cards = [line.split(':')[1].split('|') for line in lines]
    cards = [[list(map(int, re.findall(r'\d+', nrs))) for nrs in line] for line in cards]

    part1(cards)
    part2(cards)
