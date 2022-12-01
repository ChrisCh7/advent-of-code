if __name__ == '__main__':
    with open('in.txt') as file:
        elves = [list(map(int, elf.split('\n'))) for elf in file.read().split('\n\n')]

    top_elves = sorted(map(sum, elves), reverse=True)[:3]

    print('Part 1:', top_elves[0])
    print('Part 2:', sum(top_elves))
