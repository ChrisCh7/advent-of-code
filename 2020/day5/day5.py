import math

front = 'F'
back = 'B'
left = 'L'
right = 'R'


def find_row_number(row: str, range_min: int, range_max: int):
    if range_min == range_max:
        return range_max
    if row[0] == front:
        return find_row_number(row[1:], range_min, (range_max - range_min) // 2 + range_min)
    if row[0] == back:
        return find_row_number(row[1:], math.ceil((range_max - range_min) / 2) + range_min, range_max)


def find_column_number(column: str, range_min: int, range_max: int):
    if range_min == range_max:
        return range_max
    if column[0] == left:
        return find_column_number(column[1:], range_min, (range_max - range_min) // 2 + range_min)
    if column[0] == right:
        return find_column_number(column[1:], math.ceil((range_max - range_min) / 2) + range_min, range_max)


def main():
    with open('in.txt') as file:
        lines = [line.strip() for line in file.readlines()]
    max_id = 0
    ids = []
    for seat in lines:
        row = seat[:7]
        column = seat[7:]
        row_number = find_row_number(row, 0, 127)
        column_number = find_column_number(column, 0, 7)
        id = row_number * 8 + column_number
        ids.append(id)
        if id > max_id:
            max_id = id
        print(row, column, 'Row number:', row_number, 'Column number:', column_number, 'ID:', id)
    print('Max ID:', max_id)
    ids.sort()
    print('All IDs:', ids)
    for id in range(ids[0], ids[-1]):
        if id not in ids:
            print('Missing ID:', id)


if __name__ == '__main__':
    main()
