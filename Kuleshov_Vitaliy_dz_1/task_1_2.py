# 2.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
user_list = [i**3 for i in range(1, 1000, 2)]

#   a.	Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
new_list = []
for i in user_list:
    n = i
    summ = 0
    while n != 0:
        digit = n % 10
        summ += digit
        n = n // 10
    if summ % 7 == 0:
        new_list.append(i)
result = 0
for i in new_list:
    result += i
print(result)

#   b.	К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
user_list = [i ** 3 + 17 for i in range(1, 1000, 2)]
new_list = []
for i in user_list:
    n = i
    summ = 0
    while n != 0:
        digit = n % 10
        summ += digit
        n = n // 10
    if summ % 7 == 0:
        new_list.append(i)
result = 0
for i in new_list:
    result += i
print(result)

#   c.	* Решить задачу под пунктом b, не создавая новый список.
user_list = [i ** 3 + 17 for i in range(1, 1000, 2)]
for i in user_list[:]:
    n = i
    summ = 0
    while n != 0:
        digit = n % 10
        summ += digit
        n = n // 10
    if summ % 7 != 0:
        user_list.remove(i)
result = 0
for i in user_list:
    result += i
print(result)
