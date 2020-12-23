import copy

total_card_number = 0


def part1(players_og):
    players = copy.deepcopy(players_og)

    while len(players[0]) != 0 and len(players[1]) != 0:
        if players[0][0] > players[1][0]:
            move_cards(players[0], players[1])
        else:
            move_cards(players[1], players[0])

    winner = players[0] if len(players[0]) != 0 else players[1]

    score = 0
    for i in range(1, len(winner) + 1):
        score += i * winner[len(winner) - i]

    print('Part 1:', score)


def part2(players_og):
    players = copy.deepcopy(players_og)

    global total_card_number
    total_card_number = len(players[0]) + len(players[1])

    winner = game(players[0], players[1], 1)

    score = 0
    for i in range(1, len(winner) + 1):
        score += i * winner[len(winner) - i]

    print('Part 2:', score)


def game(player1: list[int], player2: list[int], game_nr):
    history = []
    round_nr = 1
    print(f'=== Game {game_nr} ===')
    while len(player1) != 0 and len(player2) != 0:
        round_winner, history = recursive_combat(player1, player2, history, game_nr, round_nr)
        if round_winner == 1:
            move_cards(player1, player2)
        else:
            move_cards(player2, player1)
        print(f'Player {round_winner} wins round {round_nr} of game {game_nr}!\n')
        round_nr += 1
    global total_card_number
    if len(player1) == total_card_number or len(player2) == total_card_number:
        print('== Post-game results ==')
        print('Player 1\'s deck:', player1)
        print('Player 2\'s deck:', player2)
        return player1 if round_winner == 1 else player2
    else:
        print(f'The winner of game {game_nr} is player {round_winner}!')
        return round_winner


def recursive_combat(player1: list[int], player2: list[int], history: list[tuple[list[int], list[int]]], game_nr,
                     round_nr):
    print(f'-- Round {round_nr} (Game {game_nr}) --')
    print('Player 1\'s deck:', player1)
    print('Player 2\'s deck:', player2)
    if (player1, player2) in history:
        return 1, history
    history.append((player1.copy(), player2.copy()))
    print('Player 1 plays:', player1[0])
    print('Player 2 plays:', player2[0])
    if player1[0] <= len(player1) - 1 and player2[0] <= len(player2) - 1:
        print('Playing a sub-game to determine the winner...\n')
        return game(player1[1:player1[0] + 1], player2[1:player2[0] + 1], game_nr + 1), history
    else:
        return (1, history) if player1[0] > player2[0] else (2, history)


def move_cards(winner: list[int], loser: list[int]):
    winner.append(winner[0])
    winner.append(loser[0])
    winner.remove(winner[0])
    loser.remove(loser[0])


if __name__ == '__main__':
    with open('in.txt') as file:
        players = file.read().split('\n\n')

    for i in range(len(players)):
        players[i] = [int(card) for card in players[i].splitlines()[1:]]

    part1(players)
    part2(players)  # works on example
