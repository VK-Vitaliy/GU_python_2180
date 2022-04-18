# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
# список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NotNumberError(Exception):
    pass


result = []
print("Enter numerical data or enter 'stop' if you want to finish a program.")
while True:
    value = input('Enter numerical data: ')

    if value == 'stop':
        print(f'Entered list of data: {result}')
        break
    try:
        if not value.isdigit():
            raise NotNumberError("It isn't numerical data.\n")
        result.append(int(value))
    except NotNumberError as err:
        print(err)
