""" HT #4 task_3
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.

__Задача из семинара 2.__ Напишите программу банкомат. Условия:
1) Начальная сумма равна нулю
2) Допустимые действия: пополнить, снять, выйти
3) Сумма пополнения и снятия кратны 50 у.е.
4) Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
5) После каждой третей операции пополнения или снятия начисляются проценты - 3%
6) Нельзя снять больше, чем на счёте
7) При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
8) Любое действие выводит сумму денег"""

# Задаём константы (ставки и условия банка)
SUM_REDNESS = 50  # Условие № 3
WITHDRAWAL_PERCENT, WITHDRAWAL_MIN, WITHDRAWAL_MAX = 0.015, 30, 600  # Условие № 4
PERCENT_FOR_WDR_OR_REFILL = 0.03  # Условие № 5
WEALTH_LIMIT, WEALTH_TAX = 5_000_000, 0.1  # Условие № 7

# Переменные:
balance = 0  # Баланс
num_operation = 0  # Номер - соответствует типу операции
sum_operation = 0  # Сумма операции (сумма снятия или попоплнения)
count_operation = 0  # Подсчёт кол-ва операций для выполнения условия № 5

# Функция для проверки корректного ввода операции банкомата (возвращает номер операции):
def operating_type() -> int:
    while True:
        print('Выберите номер операции: 1 - Пополнить, 2 - Снять, 3 - Выйти: ')
        num_action = int(input())
        if num_action not in (1, 2, 3):
            print('Введите корректный номер операции: ')
        elif num_action == 1 or num_action == 2:
            return num_action
        else:
            break

# Функция для проверки корректного ввода суммы операции, учитывая типа операции, баланс и кратность суммы операции.
# Принимает: сумму и номер/тип операции.  Возвращает: сумму, процент банка на снятие.
def check_sum(sum: int, num_action: int) -> tuple:
    while True:
        print('Введите сумму операции, кратную ', SUM_REDNESS, ' y.e.: ')
        sum = int(input())
        if sum % 50 != 0:
            print('Неверная сумма операции. Ваш баланс: ', balance, ' y.e.')
        elif num_action == 2:
            percent = min(WITHDRAWAL_MAX, max(int(WITHDRAWAL_PERCENT * sum), WITHDRAWAL_MIN))
            if sum > (balance - percent):
                print('Данная сумма не доступна для снятие с учётом процента банка. Ваш баланс: ', balance, ' y.e.')
            else:
                break
        else:
            percent = 0
            break
    return sum, percent

while num_operation != 3:
    num_operation = operating_type()
    if num_operation == 1 or num_operation == 2:
        tuple_ = check_sum(sum_operation, num_operation)
        sum_operation, percent_to_bank = tuple_[0], tuple_[1]
        if num_operation == 2:
            balance = balance - sum_operation - percent_to_bank  # (-) баланс за вычетом суммы операции и процента банка
        else:
            balance += sum_operation
            if balance > WEALTH_LIMIT:
                balance -= WEALTH_TAX
        count_operation += 1
        if count_operation % 3 == 0 and count_operation != 0:
            balance = balance + sum_operation * PERCENT_FOR_WDR_OR_REFILL  # (+) баланс с прибавлением 3% за 3-ью операцию
        print('Ваш баланс: ', balance, ' y.e.')
    else:
        print('Ваш баланс: ', balance, ' y.e. До встречи!')