""" HT #5 task 1
Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла. """

def func(link: str) -> tuple:
    *way, file = link.split('/')
    res = ''
    for i in way:
        res += i + '/'
    nm, ad = file.split('.')
    return (res, nm, ad)


print(func('C:/Users/Regina/Documents/Learning/IT/2_1_Dive_into_Python/Seminar_5/task_1.py'))