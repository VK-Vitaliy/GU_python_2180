# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class DivZeroError(Exception):
    pass


while True:
    try:
        print('\nPlease, enter dividend and divider.')
        print('Enter "quit" if you want to stop.')
        dividend = input('Enter dividend: ')
        if not dividend.isdigit():
            print('Please, enter int.')
            continue
        elif dividend == 'quit':
            break
        divider = input('Enter divider: ')
        if not divider.isdigit():
            print('Please, enter int.')
            continue
        elif divider == 'quit':
            break
        elif int(divider) == 0:
            raise DivZeroError("Error: Division by zero!")
        result = int(dividend) / int(divider)
    except DivZeroError as err:
        print(err)
    else:
        print(f'Result is {round(result, 2)}')
