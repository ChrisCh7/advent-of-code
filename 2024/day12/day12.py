from collections import deque


def get_neighbors(x, y, rows, cols):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            yield nx, ny


def calculate_area_and_perimeter(grid, start_x, start_y, plant_type, visited):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    area = 0
    perimeter = 0

    while queue:
        x, y = queue.popleft()
        area += 1

        for nx, ny in get_neighbors(x, y, rows, cols):
            if grid[nx][ny] == plant_type:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
            else:
                perimeter += 1

        # check edges of the grid for perimeter
        if x == 0 or x == rows - 1:
            perimeter += 1
        if y == 0 or y == cols - 1:
            perimeter += 1

    return area, perimeter


def calculate_total_price(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:
                plant_type = grid[x][y]
                area, perimeter = calculate_area_and_perimeter(grid, x, y, plant_type, visited)
                total_price += area * perimeter

    return total_price


if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    grid = [list(line) for line in lines]

    print('Part 1:', calculate_total_price(grid))
    print('Part 2:', 'TODO')
