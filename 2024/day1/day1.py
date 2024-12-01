from collections import Counter, defaultdict

if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    list1, list2 = map(sorted, zip(*(map(int, line.split()) for line in lines)))

    print('Part 1:', sum(abs(a - b) for a, b in zip(list1, list2)))

    counts_list2 = defaultdict(int, Counter(list2))

    print('Part 2:', sum(n * counts_list2[n] for n in list1))
