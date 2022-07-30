__all__ = ['get_employees']


def get_employees(x):
    return f'Отработка функции: {x}'


def garbage(x):
    return f'Мусорная функция: {x}'


# Тест
if __name__ == '__main__':
    print(get_employees(get_employees.__name__))
    print(garbage(get_employees.__name__))
