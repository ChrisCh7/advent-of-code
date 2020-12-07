def count_bags(bag_type, lines, passed_bags):
    bag_type_bag_lines = [line for line in lines if line.find(bag_type) != -1 and line.index(bag_type) != 0]

    if len(bag_type_bag_lines) == 0:
        return 0

    contain_bag_type = [line[0:line.index(' bags')] for line in bag_type_bag_lines if
                        line[0:line.index(' bags')] not in passed_bags]

    for bag in contain_bag_type:
        passed_bags.add(bag)

    count = len(contain_bag_type)
    for bag_type in contain_bag_type:
        count += count_bags(bag_type, lines, passed_bags)

    return count


def main():
    with open('in.txt') as file:
        lines = [line.strip() for line in file.readlines()]
    count = count_bags('shiny gold', lines, set())
    print(count)


if __name__ == '__main__':
    main()
