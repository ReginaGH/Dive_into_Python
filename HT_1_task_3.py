# Home Task 1

# Task 3
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

max_try = 10
count_tries = max_try
print('Угадайте число между', LOWER_LIMIT, "и", UPPER_LIMIT, ' :')

while True:
    print('Количество попыток:', count_tries, 'Число: ')
    number = int(input())
    if count_tries > 1:
        count_tries -= 1
        if number > num:
            print('Меньше!')
        elif number < num:
            print('Больше!')
        else:
            count_tries = 0
            print('Угадал!')
    else:
        break



