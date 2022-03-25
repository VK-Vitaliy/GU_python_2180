tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Дмитрий', 'Станислав'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

if len(tutors) >= len(klasses):
    klasses.append(None)

person_new = ((tutors[i], klasses[i]) for i in range(len(tutors)))
print(type(person_new))  # доказать что создали генератор

for i in range(len(tutors)):
    print(next(person_new))
