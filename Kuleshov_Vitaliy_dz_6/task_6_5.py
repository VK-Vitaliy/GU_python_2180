# Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным файлам и
# путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.
import json


def load_save_users_hobbies(load_users, load_hobbies, save_users_hobbies):
    with open(load_hobbies + '.csv', 'r', encoding='utf-8') as file_hobbies:
        with open(load_users + '.csv', 'r', encoding='utf-8') as file_users:
            with open(save_users_hobbies + '.json', 'w', encoding='utf-8') as file_users_hobbies:
                users_dict = {}
                count = 1
                for line in file_users:
                    user_dict = {'surname': line.split(',')[0], 'first_name': line.split(',')[1],
                                 'patronymic': line.replace('\n', '').split(',')[2],
                                 'hobbies': [hobby if hobby else None for hobby in
                                             file_hobbies.readline().replace('\n', '').split(',')]}
                    users_dict["user" + f"{str(count)}"] = user_dict
                    count += 1
                json.dump(users_dict, file_users_hobbies)


def main(argv):
    program, *argv = argv
    load_save_users_hobbies(load_users=argv[0], load_hobbies=argv[1], save_users_hobbies=argv[2])
    print(f"Файлы {argv[0]}.cvs и {argv[1]}.csv объединены в словарь и записаны в {argv[2]}.json")
    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
