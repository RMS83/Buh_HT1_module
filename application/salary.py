__all__ = ['calculate_salary']


def calculate_salary(x):
    return f'Отработка функции: {x}'


def garbage(x):
    return f'Мусорная функция: {x}'


# Тест
if __name__ == '__main__':
    print(calculate_salary(calculate_salary.__name__))
    print(garbage(calculate_salary.__name__))
