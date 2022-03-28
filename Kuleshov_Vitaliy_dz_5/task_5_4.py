# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result.append(src[i])
print(result)

result_comprehensions = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(result_comprehensions)

result_generator = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
for i in range(len(result_comprehensions)):
    print(next(result_generator))
