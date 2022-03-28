# Есть два списка. Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None)
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Дмитрий', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

person_new = ((tutors[i], klasses[i]) if len(klasses) > i else (tutors[i], None) for i in range(len(tutors)))
print(type(person_new))  # доказать что создали генератор

for i in range(len(tutors)):
    print(next(person_new))
