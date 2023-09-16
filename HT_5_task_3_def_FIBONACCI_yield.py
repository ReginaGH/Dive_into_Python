""" HT #5 task_3
Создайте функцию генератор чисел Фибоначчи """


def fibonacci(n):
    """Return the number of fibonacci of input number, n """
    f = [1, 1]
    yield f[0]
    yield f[1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
        yield f[i]


n = 8
for i in fibonacci(n):
    print(i)
