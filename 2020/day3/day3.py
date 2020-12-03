from termcolor import colored


def insert_marker_and_get(line, is_tree, current_x):
    marker = colored('X', 'red') if is_tree else colored('O', 'green')
    line = line[:current_x] + marker + line[current_x + 1:]
    return line


def main(right, down, print_slope):
    with open('in.txt') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        line_length = len(lines[0])
        open_square = '.'
        tree = '#'
        current_x = right
        current_y = down
        open_square_count = 0
        tree_count = 0
        if print_slope:
            print('1/' + str(len(lines)) + ' - ' + lines[0])
        while current_y < len(lines):
            if lines[current_y][current_x] == open_square:
                open_square_count += 1
            elif lines[current_y][current_x] == tree:
                tree_count += 1
            if print_slope:
                print(str(current_y + 1) + '/' + str(len(lines)) + ' - '
                      + insert_marker_and_get(lines[current_y], lines[current_y][current_x] == tree, current_x))
            current_x = (current_x + right) % line_length
            current_y += down
        print('Open squares: ' + str(open_square_count))
        print('Trees: ' + str(tree_count))


if __name__ == '__main__':
    main(1, 1, False)
    main(3, 1, False)
    main(5, 1, False)
    main(7, 1, False)
    main(1, 2, False)
