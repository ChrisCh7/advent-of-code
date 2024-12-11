from collections import Counter


def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        return [int(stone[:len(stone) // 2]), int(stone[len(stone) // 2:])]
    else:
        return [stone * 2024]


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    stones = [int(n) for n in lines[0].split()]
    stones_og = stones.copy()

    for _ in range(25):
        new_stones = []
        for stone in stones:
            new_stones.extend(blink(stone))
        stones = new_stones

    print('Part 1:', len(stones))

    freq = Counter(stones_og)

    for _ in range(75):
        new_freq = Counter()
        for stone, count in freq.items():
            for new_stone in blink(stone):
                # the count of each new stone reflects how many times it would have been generated
                # by all the occurrences of the original stone
                new_freq[new_stone] += count
        freq = new_freq

    print('Part 2:', sum(freq.values()))
