from collections import OrderedDict


def main():
    with open('in.txt') as file:
        foods = file.read().splitlines()

    ingredients = [food[:food.index('(')].split() for food in foods]
    allergens = [food[food.index('(') + 10:-1].split(', ') for food in foods]

    ingredients_distinct = set()
    for ingreds in ingredients:
        for ingr in ingreds:
            ingredients_distinct.add(ingr)

    allergens_distinct = set()
    for allergs in allergens:
        for allerg in allergs:
            allergens_distinct.add(allerg)

    all_suspects = dict()
    for allergen in allergens_distinct:
        suspects = []
        for i in range(len(ingredients)):
            if allergen in allergens[i]:
                if len(suspects) == 0:
                    suspects.extend(ingredients[i])
                else:
                    suspects = [susp for susp in suspects if susp in ingredients[i]]
        all_suspects[allergen] = suspects

    contain_allergens = set()
    while len(contain_allergens) < len(allergens_distinct):
        for susp in all_suspects:
            if len(all_suspects[susp]) == 1:
                contain_allergens.add(all_suspects[susp][0])
        for susp in all_suspects:
            if len(all_suspects[susp]) != 1:
                for allergen in contain_allergens:
                    if allergen in all_suspects[susp]:
                        all_suspects[susp].remove(allergen)

    not_contain_allergens = ingredients_distinct - contain_allergens

    count = 0
    for ingreds in ingredients:
        for not_allergen in not_contain_allergens:
            if not_allergen in ingreds:
                count += 1

    print('Part 1:', count)

    allergens_ordered = OrderedDict(sorted(all_suspects.items()))

    dangerous_ingredients = []
    for allergen, ingredient in allergens_ordered.items():
        dangerous_ingredients.extend(ingredient)

    canonical_dangerous_ingredient_list = ','.join(dangerous_ingredients)

    print('Part 2:', canonical_dangerous_ingredient_list)


if __name__ == '__main__':
    main()
