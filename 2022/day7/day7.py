from collections import deque


class File:
    def __init__(self, name, parent, is_folder, size=0):
        self.name = name
        self.parent = parent
        self.is_folder = is_folder
        self.children = {}
        self.size = int(size)


if __name__ == '__main__':
    with open('in.txt') as file:
        terminal_output = file.read().splitlines()

    navigation = deque(['/'])
    folders = {'/': File('/', None, True)}

    path = lambda foldername: ''.join(navigation) + foldername

    for line in terminal_output:
        parts = line.split()
        if parts[0] == '$':
            if parts[1] == 'cd':
                if parts[2] == '/':
                    navigation.clear()
                    navigation.append('/')
                elif parts[2] == '..':
                    navigation.pop()
                    if not navigation:
                        navigation.append('/')
                else:
                    if path(parts[2]) not in folders:
                        folders[path(parts[2])] = File(parts[2], path(''), True)
                    if parts[2] not in folders[path('')].children:
                        folders[path('')].children[parts[2]] = folders[path(parts[2])]
                    navigation.append(parts[2])
        else:
            if parts[0] == 'dir':
                if path(parts[1]) not in folders:
                    folders[path(parts[1])] = File(parts[1], path(''), True)
                if path(parts[1]) not in folders[path('')].children:
                    folders[path('')].children[parts[1]] = folders[path(parts[1])]
            else:
                size, name = parts
                if name not in folders[path('')].children:
                    folders[path('')].children[name] = File(name, path(''), False, size)
                    folders[path('')].size += int(size)

                    parent = folders[path('')].parent
                    while parent is not None:
                        folders[parent].size += int(size)
                        parent = folders[parent].parent

    size_sum = 0
    for folder in folders:
        if (dir_size := folders[folder].size) <= 100000:
            size_sum += dir_size

    print('Part 1:', size_sum)

    unused = 70000000 - folders['/'].size
    free_up = 30000000 - unused

    min_size = folders['/'].size
    for folder in folders:
        if free_up <= folders[folder].size < min_size:
            min_size = folders[folder].size

    print('Part 2:', min_size)
