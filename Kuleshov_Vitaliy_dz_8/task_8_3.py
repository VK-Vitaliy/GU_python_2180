# Написать декоратор для логирования типов позиционных аргументов функции.
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_dict = {}
        # работа с позиционными аргументами
        for i in args:
            result_dict[i] = type(i)
        # работа с именованными аргументами
        for v in kwargs.values():
            result_dict[v] = type(v)
        return func.__name__ + str(result_dict)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5, 7, x=6))
