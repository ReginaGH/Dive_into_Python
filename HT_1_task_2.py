# Home Task 1

# Task 2
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

min_limit = 1
max_limit = 100_000
number = None
while True:
    print('Введите число между ', min_limit, "и", max_limit, ': ')
    number = int(input())
    if number < min_limit or number > max_limit:
        print('Введите корректное число')
    else:
        break

count = None
for i in range(2, number):
    if number % i == 0:
        count = 1
print('Составное число' if count == 1 else 'Простое число')
