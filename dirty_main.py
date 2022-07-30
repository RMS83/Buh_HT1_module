from pprint import pprint
from datetime import date

from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    try:
        print(date.today())
        print(calculate_salary('calculate_salary'))
        print(get_employees('get_employees'))
        print(garbage('calculate_salary'))  # Для примера - что исключение функции __all__ сработало
        print(garbage('get_employees'))  # Для примера - что исключение функции __all__ сработало
    except Exception as err:
        pprint(f'ERROR - {err}')
    else:
        print('Операция прошла успешно')
    finally:
        print(date.today())
