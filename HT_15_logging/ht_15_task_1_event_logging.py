from datetime import datetime
import logging
import argparse

""" HT_15_task_1_итоговая 
Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок 
и полезной информации. 
HT_11_2
Создайте класс MyStr, который наследуется от встроенного класса str и добавлять дополнительную информацию 
о создателе строки и времени ее создания. Этот класс будет представлять строки с информацией о событиях.
Класс MyStr должен иметь следующие атрибуты и методы:
value (str): Строковое значение с описанием события. author (str): Имя автора, создавшего запись.
time: Время создания записи в формате '%Y-%m-%d %H:%M'."""


class MyStr(str):
    """Function has all properties of str method (parents class),
    adds the properties of instances: name, time"""
    def __new__(cls, event, author):
        instance = super().__new__(cls)
        if isinstance(author, str):
            instance.author = author
        else:
            logger.error(TypeError)
            raise TypeError(f'Author should be "str" format. Your value is {author}:')
        if isinstance(event, str):
            instance.value = event
        else:
            logger.error(TypeError)
            raise TypeError(f'Author should be "str" format. Your value is {event}:')
        instance.time = datetime.now().__format__("%Y-%m-%d %H:%M")
        logger.info(instance)
        return instance

    def __str__(self):
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        logger.info(self)
        return f"MyStr('{self.value}', '{self.author}')"


if __name__ == '__main__':
    FORMAT = '{levelname}:<7 - {asctime} - function: {funcName} - message: {msg} - filename: {name}'
    logging.basicConfig(format=FORMAT, style='{', filename='ht_15_1.log', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__file__)
    parser = argparse.ArgumentParser(description='Logging_event')
    parser.add_argument('values', metavar='event author', type=str, nargs=2,\
                        help='Enter your event and the author of the notes with a space between values')
    args = parser.parse_args()
    print(MyStr(*args.values))
