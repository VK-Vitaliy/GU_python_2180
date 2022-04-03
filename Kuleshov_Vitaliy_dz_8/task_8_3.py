# Написать декоратор для логирования типов позиционных аргументов функции, например
def type_logger(func):
    def wrapper(*args):
        result_func = func(*args)
        result_dict = {}
        for i in args:
            result_dict[i] = type(result_func)
        print(func.__name__ + str(result_dict))

    return wrapper


@type_logger
def calc_cube(*args):
    for i in args:
        return i ** 3


calc_cube(5)