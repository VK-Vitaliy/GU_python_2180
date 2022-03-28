# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
def odd_nums(num):
    for i in range(1, num + 1, 2):
        yield i


odd_to_15 = odd_nums(15)
for _ in range(1, 10):
    try:
        print(next(odd_to_15))
    except StopIteration:
        print('...StopIteration...')
