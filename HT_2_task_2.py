# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей.
# Для проверки своего кода используйте модуль fractions.

import math
from fractions import Fraction

def convert_to_tuple(num: str):
# функция принимает дробное число в виде строки, возвращает кортеж из чисел (знаменатель, числитель):
    numerator = int(num.split('/')[0])
    denominator = int(num.split('/')[1])
    return numerator, denominator

def reduction(fraction:str) -> str:  # функция сокращения дроби (6/10 => 3/4)
    fraction = convert_to_tuple(fraction)
    gcd = math.gcd(fraction[0], fraction[1])
    fraction = str(round((fraction[0]/gcd),)) + '/' + str(round((fraction[1]/gcd),))
    return fraction

def func(a: str, b: str):  # функция для вычисление суммы и произведения дробей
    a, b = convert_to_tuple(a), convert_to_tuple(b)
    lcm = math.lcm(a[1], b[1])
    mult = str(a[0] * b[0]) + '/' + str(a[1] * b[1])
    summary = str(round(((lcm / a[1] * a[0]) + (lcm / b[1] * b[0])),)) + '/' + str(lcm)
    mult = reduction(mult)
    summary = reduction(summary)
    return mult, summary
input_1 = input('Введите одно дробное число: ')
input_2 = input('Введите другое дробное число: ')
print('Произведение и сумма чисел: ', *func(input_1, input_2))

# Проверка модулем "fractions"
n1 = Fraction(input_1)
n2 = Fraction(input_2)
if str(n1 * n2) == func(input_1, input_2)[0] and str(n1 + n2) == func(input_1, input_2)[1]:
    print('Вычисления верные')
else:
    print('Вычисления не верные')