# Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ.
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и
# название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга
import json

with open('hobby.csv', 'r', encoding='utf-8') as file_hobbies:
    with open('users.csv', 'r', encoding='utf-8') as file_users:
        with open('users_hobbies.json', 'w', encoding='utf-8') as file_users_hobbies:
            # данные о каждом пользователе сохраним в словарь для создания эффективной структуры данных
            users_dict = {}
            count = 1
            for line in file_users:
                # для каждого пользователя user создаем словарь с ключами surname, first_name, patronymic, hobbies
                # значения ключа hobbies делаем списком, что бы сохранять несколько значений хобби
                user_dict = {'surname': line.split(',')[0], 'first_name': line.split(',')[1],
                             'patronymic': line.replace('\n', '').split(',')[2],
                             'hobbies': [hobby if hobby else None for hobby in
                                         file_hobbies.readline().replace('\n', '').split(',')]}
                users_dict["user" + f"{str(count)}"] = user_dict
                count += 1
            print(users_dict)
            json.dump(users_dict, file_users_hobbies)
