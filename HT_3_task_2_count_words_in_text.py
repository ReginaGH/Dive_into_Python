import string

# HT #3 task_2
"""В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки 
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку."""

data = ('Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a '
        'simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, '
        'together with its interpreted nature, make it an ideal language for scripting and rapid application '
        'development in many areas on most platforms. The Python interpreter and the extensive standard library are '
        'freely available in source or binary form for all major platforms from the Python web site, '
        'https://www.python.org/, and may be freely distributed. The same site also contains distributions of and '
        'pointers to many free third party Python modules, programs and tools, and additional documentation. The '
        'Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other '
        'languages callable from C). Python is also suitable as an extension language for customizable applications. '
        'This tutorial introduces the reader informally to the basic concepts and features of the Python language and '
        'system. It helps to have a Python interpreter handy for hands-on experience, but all examples are '
        'self-contained, so the tutorial can be read off-line as well. For a description of standard objects and '
        'modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of '
        'the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and '
        'Python/C API Reference Manual. There are also several books covering Python in depth. This tutorial does not '
        'attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, '
        'it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s '
        'flavor and style. After reading it, you will be able to read and write Python modules and programs, '
        'and you will be ready to learn more about the various Python library modules described in The Python '
        'Standard Library.')

# 1) Удаляем всю пунктуацию:
punctuation = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
text = ''
for i in data:
    if i not in punctuation:
        text += i

# 2) Создаем список только из слов в нижнем регистре
words_list = []
for word in text.split():
    temp = ''
    for letter in word:
        if letter.isalpha():
            temp += letter.lower()
    words_list.append(temp)

# 3) Создаём словарь (ключ: кол-во в тексте)
words_count = {}
for word in words_list:
    if word not in words_count.keys():
        words_count.setdefault(word, 1)
    else:
        value = words_count[word] + 1
        words_count[word] = value

# 4) Сортируем значения словаря и выводим 10 ключей: 10 наиб.встречающихся слов
count_list = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
print(*dict(count_list[1:11]).keys(), sep=', ')
