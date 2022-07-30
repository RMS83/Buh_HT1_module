from pprint import pprint
from datetime import date

from application import salary, people

if __name__ == '__main__':
    try:
        print(salary.calculate_salary('calculate_salary'))
        print(people.get_employees('get_employees'))
    except Exception as err:
        pprint(f'ERROR - {err}')
    else:
        print('Операция прошла успешно')
    finally:
        print(date.today())
