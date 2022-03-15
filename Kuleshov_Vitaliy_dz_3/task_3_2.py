# 2. Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.

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
    if value.istitle() and dict_num.get(value.lower()):
        return dict_num.get(value.lower()).title()
    else:
        return dict_num.get(value)


print(f'"{num_translate("Eleven")}"')
