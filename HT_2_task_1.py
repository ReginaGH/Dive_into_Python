# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))
num_hex = hex(num)
res = ''
while num >0:
    res = str(num % 16) + res
    num //= 16
print(res, num_hex)