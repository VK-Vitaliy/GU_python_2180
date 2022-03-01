# 4. Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.


def thesaurus_adv(*args):
    person_dict = {}
    for i in args:
        first_name, second_name = i.split()
        if not person_dict.get((second_name[0])):
            person_dict[second_name[0]] = {first_name[0]: [i]}
        elif not person_dict[second_name[0]].get(first_name[0]):
            person_dict[second_name[0]][first_name[0]] = [i]
        else:
            person_dict[second_name[0]][first_name[0]].append(i)
    return person_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))