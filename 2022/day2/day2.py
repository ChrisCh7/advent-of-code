if __name__ == '__main__':
    with open('in.txt') as file:
        strategy_guide = [entry.split() for entry in file.read().splitlines()]

    is_defeated_by = {'rock': 'scissors',
                      'scissors': 'paper',
                      'paper': 'rock'}

    defeats = dict((value, key) for key, value in is_defeated_by.items())

    selected_score = {'rock': 1,
                      'paper': 2,
                      'scissors': 3}

    round_outcome = {'lost': 0,
                     'draw': 3,
                     'won': 6}

    opponent_plays = {'A': 'rock',
                      'B': 'paper',
                      'C': 'scissors'}

    me_plays = {'X': 'rock',
                'Y': 'paper',
                'Z': 'scissors'}


    def get_round_score(shape, outcome):
        return selected_score[shape] + round_outcome[outcome]


    total_score = 0
    for round in strategy_guide:
        if is_defeated_by[opponent_plays[round[0]]] == me_plays[round[1]]:
            total_score += get_round_score(me_plays[round[1]], 'lost')
        elif is_defeated_by[me_plays[round[1]]] == opponent_plays[round[0]]:
            total_score += get_round_score(me_plays[round[1]], 'won')
        else:
            total_score += get_round_score(me_plays[round[1]], 'draw')

    print('Part 1:', total_score)

    required_ending = {'X': 'lose',
                       'Y': 'draw',
                       'Z': 'win'}

    total_score = 0
    for round in strategy_guide:
        if required_ending[round[1]] == 'draw':
            total_score += get_round_score(opponent_plays[round[0]], 'draw')
        elif required_ending[round[1]] == 'lose':
            total_score += get_round_score(is_defeated_by[opponent_plays[round[0]]], 'lost')
        else:
            total_score += get_round_score(defeats[opponent_plays[round[0]]], 'won')

    print('Part 2:', total_score)
