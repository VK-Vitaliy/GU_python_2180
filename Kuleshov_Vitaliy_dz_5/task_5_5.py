# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке.
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [num for num in src if src.count(num) == 1]

print(result)

# Вариант с урока
unique_nums = set()
tmp = set()
for i in src:
    if i not in tmp:
        unique_nums.add(i)
    else:
        unique_nums.discard(i)
    tmp.add(i)
result = [i for i in src if i in unique_nums]
print(result)
