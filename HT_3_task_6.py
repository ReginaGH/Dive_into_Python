# HT #3 task_6
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends_staff = {
    'Jerry': ('flashlight', 'matches', 'powerbank', 'mobile', 'jacket', 'mobile', 'food'),
    'Tom': ('food', 'water', 'sleeping_bag', 'mat', 'mobile', 'matches', 'tent'),
    'Guffi': ('kitchen_utensil', 'hygiene_staff', 'mobile', 'mat', 'jacket', 'sleeping_bag', 'food')
}
# 1) Список всех вещей трёх друзей:
all_staff = set()
for key, value in friends_staff.items():
    for staff in value:
       all_staff.add(staff)
print(f'Список всех вещей трёх друзей: {all_staff}')
