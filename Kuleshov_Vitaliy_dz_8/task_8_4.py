def val_checker(callback_func):
    def _checker(func):
        def wrapped(*args, **kwargs):
            if callback_func(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError(f'wrong val {args, kwargs}')

        return wrapped

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
