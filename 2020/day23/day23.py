def part1(cups_og: list[int]):
    cups = cups_og.copy()
    move(cups[0], cups, 1, 100, True, 1)


def part2(cups_og: list[int]):
    cups = cups_og.copy()
    cups.extend(range(10, 1_000_000 + 1))
    move(cups[0], cups, 1, 10_000_000, False, 2)


def move(current_cup: int, cups: list[int], move_nr, moves_to_do, print_moves: bool, part):
    if print_moves:
        print(f'-- move {move_nr} --')
        print('cups:', cups)
    pick_up = cups[1:4]
    if print_moves:
        print('pick up:', pick_up)
    remaining_cups = list(set(cups) - {current_cup} - set(pick_up))
    destination_cup = select_destination_cup(current_cup, remaining_cups)
    if print_moves:
        print('destination:', destination_cup, '\n')
    destination_cup_index = cups.index(destination_cup)
    new_cups = cups[:destination_cup_index][4:] + [destination_cup] + pick_up + cups[destination_cup_index + 1:] \
               + [current_cup]
    if move_nr < moves_to_do:
        move(new_cups[0], new_cups, move_nr + 1, moves_to_do, print_moves, part)
    else:
        if print_moves:
            print('-- final --')
            print('cups:', new_cups)
        one_index = new_cups.index(1)
        if part == 1:
            print(f'Part {part}:', ''.join([str(cup) for cup in new_cups[one_index + 1:] + new_cups[:one_index]]))
        else:
            print(f'Part {part}:', new_cups[new_cups.index(1) + 1] * new_cups[new_cups.index(1) + 2])


def select_destination_cup(current_cup: int, remaining_cups: list[int]):
    if current_cup - 1 in remaining_cups:
        return current_cup - 1
    min_cup = min(remaining_cups)
    for i in range(current_cup - 2, min_cup - 1, -1):
        if i in remaining_cups:
            return i
    return max(remaining_cups)


if __name__ == '__main__':
    with open('in.txt') as file:
        cups = [int(cup) for cup in file.readline().strip()]
    part1(cups)
    # part2(cups) doesn't work
