# HT #3 task_3
"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните
все возможные варианты комплектации рюкзака."""

backpack = {'matches': 0.001, 'flashlight': 0.1, 'socks': 0.2, 'repellent': 0.25, 'mobile': 0.3, 'powerbank': 0.5,
            'kitchen_utensil': 0.7, 'mat': 0.9, 'jacket': 1, 'hygiene_staff': 1.2, 'sleeping_bag': 2.5, 'food': 3,
            'water': 5}
LOAD_CAPACITY = 10


def packing(backpack_variant: dict, list_capacity_variant: list, count_kg=0):
    list_capacity_variant = []
    for key, value in backpack_variant.items():
        if (LOAD_CAPACITY - count_kg) > value:
            list_capacity_variant.append(key)
            count_kg += value

    return list_capacity_variant, count_kg


list_capacity = []
# 1) Упаковка рюкзака без условий
print(packing(backpack, list_capacity))
""" (['matches', 'flashlight', 'socks', 'repellent', 'mobile', 'powerbank', 'kitchen_utensil', 'mat', 'jacket', 
'hygiene_staff', 'sleeping_bag'], 7.651)"""

# 2) Упаковка наименьшего кол-ва вещей:
heavy_staff = sorted(backpack.items(), key=lambda x: x[1], reverse=True)
print(packing(dict(heavy_staff), list_capacity))
# (['water', 'food', 'hygiene_staff', 'kitchen_utensil', 'flashlight'], 9.999999999999998)
