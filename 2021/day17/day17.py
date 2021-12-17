def step(pos: list[int], velocity: list[int]):
    pos[0] += velocity[0]
    pos[1] += velocity[1]

    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1

    velocity[1] -= 1

    return pos, velocity


def test_velocity(pos: list[int], velocity: list[int], target: list[list[int]]):
    pos = pos.copy()
    velocity = velocity.copy()

    was_in_target = False
    max_height = pos[1]

    while pos[0] <= target[0][1] and pos[1] >= target[1][0]:
        pos, velocity = step(pos, velocity)
        if pos[0] in range(target[0][0], target[0][1] + 1) and pos[1] in range(target[1][0], target[1][1] + 1):
            was_in_target = True
        max_height = max(max_height, pos[1])

    return was_in_target, max_height


if __name__ == '__main__':
    with open('in.txt') as file:
        content = file.readline()

    target = content.split('target area: ')[1].split(', ')
    target = [[int(n) for n in c[2:].split('..')] for c in target]

    pos = [0, 0]

    max_observed_height = 0
    optimal_velocity = []
    velocity_counter = 0

    for x in range(0, 501):
        for y in range(-500, 501):
            was_in_target, max_height = test_velocity(pos, [x, y], target)
            if was_in_target:
                velocity_counter += 1
                if max_height > max_observed_height:
                    max_observed_height = max_height
                    optimal_velocity = [x, y]

    print('Part 1:', max_observed_height)
    print('Part 2:', velocity_counter)
