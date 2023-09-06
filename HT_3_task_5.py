# HT #3 task_5
# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

text = 'Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним'
text = text.lower()

letter_count_for = dict()
for i in text:
    count = 0
    if i.isalpha() and i not in letter_count_for.keys():
        letter_count_for.setdefault(i, 1)
    elif i.isalpha():
        count = letter_count_for[i] + 1
        letter_count_for[i] = count
print(letter_count_for)

letter_count = {}
for i in text:
    if i.isalpha():
        letter_count.setdefault(i, text.count(i))
print(letter_count)
