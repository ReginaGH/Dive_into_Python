from datetime import date
from sys import argv

"""Function check_a_date
receive the date in str format such as 'DD.MM.YYYY', convert to date format: YYYY-MM-DD
return True if data exist in Gregorian calendar or False if not"""


def check_a_date(input_date: str):
    input_date = input_date.split('.')
    try:
        input_date = date(int(input_date[-1]), int(input_date[1]), int(input_date[0]))
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(check_a_date('2.2.9999'))

print(check_a_date(argv[1]))
