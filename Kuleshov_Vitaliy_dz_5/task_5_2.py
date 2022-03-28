# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield
odd_to_n = 15
odd_nums = (i for i in range(1, odd_to_n + 1, 2))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
