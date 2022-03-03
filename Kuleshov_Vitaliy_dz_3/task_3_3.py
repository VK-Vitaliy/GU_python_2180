# 3.	Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def thesaurus(*args):
    dict_names = dict()
    for i in args:
        dict_names[i[0]] = dict_names.setdefault(i[0], []) + [i]
    return dict_names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
