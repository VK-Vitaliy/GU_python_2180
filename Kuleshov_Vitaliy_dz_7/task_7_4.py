# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0)
import os

folder = os.getcwd()
dict_size = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}

for root, dirs, files in os.walk(folder):
    for file in files:
        if os.stat(os.path.join(root, file)).st_size < 100:
            dict_size[100] += 1
        elif os.stat(os.path.join(root, file)).st_size < 1000:
            dict_size[1000] += 1
        elif os.stat(os.path.join(root, file)).st_size < 10000:
            dict_size[10000] += 1
        elif os.stat(os.path.join(root, file)).st_size < 100000:
            dict_size[100000] += 1
print(dict_size)
