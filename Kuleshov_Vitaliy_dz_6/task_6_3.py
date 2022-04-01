# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ
import sys
import json

with open('hobby.csv', 'r', encoding='utf-8') as file_hobbies:
    with open('users.csv', 'r', encoding='utf-8') as file_users:
        users = file_users.read().replace(',', ' ').splitlines()
        hobbies = file_hobbies.read().replace(',', ', ').splitlines()
        if len(users) < len(hobbies):
            sys.exit(1)
        users_hobbies_dict = {users[i]: hobbies[i] if len(hobbies) > i else None for i in range(len(users))}
        print(users_hobbies_dict)

with open('users_hobbies.json', 'w', encoding='utf-8') as file_users_hobbies:
    json.dump(users_hobbies_dict, file_users_hobbies)

with open('users_hobbies.json', 'r', encoding='utf-8') as file_users_hobbies:
    users_hobbies_dict = json.load(file_users_hobbies)
    print(users_hobbies_dict)
