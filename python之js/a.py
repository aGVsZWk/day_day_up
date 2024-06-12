data = [
    {"id": 1, "name": 10},
    {"id": 2, "name": 20},
    {"id": 3, "name": 30},
    {"id": 4, "name": 40},
]


ids = [2, 3, 1, 4]

data.sort(key=lambda x: ids.index(x['id']))
