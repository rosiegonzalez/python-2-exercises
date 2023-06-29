def calc_bmi(list_bmi):
    new_list = list(map(lambda p: round (['weight_kg'] / ['height_meters'] ** 2), people_list))
    return new_list




people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]


print(calc_bmi(people_list))