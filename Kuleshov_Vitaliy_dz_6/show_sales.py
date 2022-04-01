# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    show = list(map(int, sys.argv[1:]))
    line = f.readlines()
    if len(show) == 2:
        for el in line[show[0] - 1: show[1]]:
            print(el.strip())
    elif len(show) == 1:
        for el in line[show[0] - 1:]:
            print(el.strip())
    else:
        for el in line:
            print(el.strip())
    exit(0)
