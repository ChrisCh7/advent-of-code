if __name__ == '__main__':
    with open('in.txt') as file:
        lines = file.read().splitlines()

    separator_idx = lines.index('')
    ingredient_id_ranges = lines[:separator_idx]
    ingredient_ids = lines[separator_idx + 1:]
    ingredient_id_ranges = [tuple(map(int, rnge.split('-'))) for rnge in ingredient_id_ranges]
    ingredient_ids = list(map(int, ingredient_ids))

    nr_fresh_ingredients = 0
    for ingredient_id in ingredient_ids:
        for rnge in ingredient_id_ranges:
            if rnge[0] <= ingredient_id <= rnge[1]:
                nr_fresh_ingredients += 1
                break

    ingredient_id_ranges.sort(key=lambda r: r[0])
    merged_ranges = [ingredient_id_ranges[0]]
    for rnge in ingredient_id_ranges[1:]:
        start, end = merged_ranges[-1]
        next_start, next_end = rnge
        if start <= next_start <= end + 1:
            merged_ranges[-1] = (start, max(end, next_end))
        else:
            merged_ranges.append(rnge)

    nr_fresh_ingredient_ids = 0
    for rnge in merged_ranges:
        nr_fresh_ingredient_ids += rnge[1] - rnge[0] + 1

    print('Part 1:', nr_fresh_ingredients)
    print('Part 2:', nr_fresh_ingredient_ids)
