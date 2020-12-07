def count_bags(bag_type, lines):
    bag_line = [line for line in lines if line.find(bag_type) != -1 and line.index(bag_type) == 0]
    bag_line = bag_line[0][:-1]

    if bag_line.count('no other') == 1:
        return 0

    bags = [line.strip() for line in bag_line.split(',')]
    bags[0] = bags[0][bags[0].index('contain') + 8:]

    for i in range(len(bags)):
        bags[i] = bags[i][:bags[i].index('bag') - 1]

    bags = [[int(bag.split()[0]), bag[bag.index(bag.split()[1]):]] for bag in bags]

    count = 0
    for bag in bags:
        count += bag[0] + bag[0] * count_bags(bag[1], lines)

    return count


def main():
    with open('in.txt') as file:
        lines = [line.strip() for line in file.readlines()]
    count = count_bags('shiny gold', lines)
    print(count)


if __name__ == '__main__':
    main()
