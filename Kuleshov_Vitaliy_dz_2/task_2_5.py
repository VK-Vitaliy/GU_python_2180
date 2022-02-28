# Создать вручную список, содержащий цены на товары (10–20 товаров)
price = [57.8, 46.51, 97, 154.2, 336, 38.08, 12, 224.5, 150.1, 89.09, 111.11, 313, 218.18]
# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (
# например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп)
price_float = list(map(float, price))
price_str = [str(i) for i in price_float]
for i in price_str:
    R, K = i.split('.')
    R, K = int(R), int(K)
    print(f'{R} руб {K:02d} коп', end=', ')
print()

# B.	Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
# сортировки остался тот же).
price = [57.8, 46.51, 97, 154.2, 336, 38.08, 12, 224.5, 150.1, 89.09, 111.11, 313, 218.18]
print(price)
print(id(price))  # текущий id
price.sort()
print(price)
print(id(price))  # тот же id отсортированного списка по возрастанию
price_float = list(map(float, price))
price_str = [str(i) for i in price_float]
for i in price_str:
    R, K = i.split('.')
    R, K = int(R), int(K)
    print(f'{R} руб {K:02d} коп', end=', ')
print()

# C.	Создать новый список, содержащий те же цены, но отсортированные по убыванию.
price = [57.8, 46.51, 97, 154.2, 336, 38.08, 12, 224.5, 150.1, 89.09, 111.11, 313, 218.18]
print(id(price))
price_rev = sorted(price, reverse=True)
print(price_rev)
print(id(price_rev))  # видим, что ссылка идет на новый объект, значит список новый

# D.	Вывести цены пяти самых дорогих товаров.
price = [57.8, 46.51, 97, 154.2, 336, 38.08, 12, 224.5, 150.1, 89.09, 111.11, 313, 218.18]
price.sort(reverse=True)
price_float = list(map(float, price))
price_str = [str(i) for i in price_float]
for i in price_str[:6]:
    R, K = i.split('.')
    R, K = int(R), int(K)
    print(f'{R} руб {K:02d} коп', end=', ')
print()
