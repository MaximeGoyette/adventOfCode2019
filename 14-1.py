import math
from copy import deepcopy

data = '''157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''.split('\n')
#data = open('14.txt').read().split('\n')

reverse_recipes = {}

for line in data:
    ingredients, product = line.split(' => ')
    ingredients = [(int(ing.split(' ')[0]), ing.split(' ')[1]) for ing in ingredients.split(', ')]
    product = (int(product.split(' ')[0]), product.split(' ')[1])

    reverse_recipes[product[1]] = ([x[1] for x in ingredients], {x[1]: x[0] for x in ingredients + [product]})

next_products = {'FUEL': 1}
convert_ores = False

while True:
    current_products = deepcopy(next_products)

    for product, required_amount in current_products.items():
        ingredients, amounts = reverse_recipes.get(product, ([], {}))

        if not convert_ores and 'ORE' in ingredients:
            next_products[product] = required_amount
            continue

        for ingredient in ingredients:
            n = math.ceil(required_amount/amounts[product])
            if ingredient not in next_products:
                next_products[ingredient] = 0
            next_products[ingredient] += n*amounts[ingredient]

        del next_products[product]

    if convert_ores:
        break

    if current_products == next_products:
        convert_ores = True

print(next_products)

# not 181628 (too low)
# not 192186 (too low)
