from collections import Counter


def replace_joker(hand: str) -> str:
    max_count = max(Counter(hand).values())
    max_count_card = [el for el in Counter(hand).items() if el[1] == max_count][0][0]
    sorted_hand = ''.join(sorted(hand))
    hand_no_j = hand.replace('J', '')

    if max_count == 4:
        if max_count_card == 'J':
            max_count_card = [el for el in Counter(hand_no_j).items() if el[1] == 1][0][0]
    elif max_count == 3:
        if max_count_card == 'J':
            max_count_card = [el for el in Counter(hand_no_j).items() if el[1] in [1, 2]][0][0]
    elif max_count == 2:
        if 'JJ' in sorted_hand:
            if max(Counter(hand_no_j).values()) == 2:
                max_count_card = [el for el in Counter(hand_no_j).items() if el[1] == 2][0][0]
            else:
                max_count_card = [el for el in Counter(hand_no_j).items() if el[1] == 1][0][0]
        else:
            max_count_card = [el for el in Counter(hand_no_j).items() if el[1] == 2][0][0]
    elif max_count == 1:
        max_count_card = [el for el in Counter(hand_no_j).items() if el[1] == 1][0][0]

    return hand.replace('J', max_count_card)


def get_hand_strength(hand: str, part: int = 1) -> int:
    if part == 2 and 'J' in hand:
        hand = replace_joker(hand)

    if len(set(hand)) == 1:
        hand_strength = 7
    elif len(set(hand)) == 2 and 4 in Counter(hand).values():
        hand_strength = 6
    elif len(set(hand)) == 2 and [2, 3] == sorted(Counter(hand).values()):
        hand_strength = 5
    elif len(set(hand)) == 3 and [1, 1, 3] == sorted(Counter(hand).values()):
        hand_strength = 4
    elif len(set(hand)) == 3 and [1, 2, 2] == sorted(Counter(hand).values()):
        hand_strength = 3
    elif len(set(hand)) == 4 and [1, 1, 1, 2] == sorted(Counter(hand).values()):
        hand_strength = 2
    else:
        hand_strength = 1
    return hand_strength


def get_card_strengths(hand: str, part: int = 1) -> str:
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    if part == 2:
        order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    card_strengths = {c: s for s, c in enumerate(order)}

    strengths = ''

    # card strengths expressed as characters, b > a
    for card in hand:
        strengths += chr(97 + card_strengths[card])

    return strengths


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    hands = [[line.split()[0], int(line.split()[1])] for line in lines]

    sorted_hands = sorted(hands, key=lambda h: (get_hand_strength(h[0]), get_card_strengths(h[0])))

    print('Part 1:', sum(bid * rank for rank, [_, bid] in enumerate(sorted_hands, 1)))

    sorted_hands_p2 = sorted(hands, key=lambda h: (get_hand_strength(h[0], 2), get_card_strengths(h[0], 2)))

    print('Part 2:', sum(bid * rank for rank, [_, bid] in enumerate(sorted_hands_p2, 1)))
