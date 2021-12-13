from collections import defaultdict

paths = []


def part1(connections: dict[str, list[str]]):
    traverse('start', connections, [])
    print('Part 1:', len(paths))


def part2(connections: dict[str, list[str]]):
    counter = traverse_p2('start', connections, [])
    print('Part 2:', counter)


def traverse(from_node: str, connections: dict[str, list[str]], path: list[str]):
    global paths
    if from_node == 'end':
        path.append(from_node)
        paths.append(path)
        return

    next_nodes = connections[from_node]

    for node in next_nodes:
        if node == 'start':
            continue
        if node.islower() and node in path:
            continue

        traverse(node, connections, path + [from_node])


def traverse_p2(from_node: str, connections: dict[str, list[str]], path: list[str], counter=0):
    if from_node == 'end':
        return 1

    next_nodes = connections[from_node]

    for node in next_nodes:
        if node == 'start':
            continue
        lower_nodes = [node for node in path if node.islower()]
        double_exists = len(lower_nodes) == len(set(lower_nodes)) + 1
        if node.islower() and node in path and double_exists:
            continue

        counter += traverse_p2(node, connections, path + [node])

    return counter


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    connections = defaultdict(list)

    for line in lines:
        from_node, to_node = line.split('-')
        connections[from_node].append(to_node)
        connections[to_node].append(from_node)

    part1(connections)
    part2(connections)
