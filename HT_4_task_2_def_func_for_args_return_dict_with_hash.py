""" HT #4 task_2
Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление."""


def func(*args) -> dict:
    hash_dict = {}
    for elem in args:
        if args.__hash__ :
            hash_dict.setdefault(elem, hash(elem))
        else:
            hash_dict.setdefault(elem, str(args.__name__))
    return hash_dict


print(func(*['s','wc',10]))
