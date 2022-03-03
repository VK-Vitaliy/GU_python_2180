# 1.	Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
#       Если перевод сделать невозможно, вернуть None.


def num_translate(value):
    dict_num = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'zero': 'ноль'
    }
    return dict_num.get(value)


print(f'"{num_translate("two")}"')
