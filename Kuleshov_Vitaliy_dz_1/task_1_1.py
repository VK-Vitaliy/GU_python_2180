# 1.	Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#   a.	до минуты: <s> сек;
#   b.	до часа: <m> мин <s> сек;
#   c.	до суток: <h> час <m> мин <s> сек;
#   d.	* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# hour 3600 seconds
# 1 day	86400 seconds

# вариант с 1 значением
duration = 86400
if 0 <= duration <= 59:
    print(f'{duration} сек')
elif 60 <= duration <= 3599:
    print(f'{duration // 60} мин {duration % 60} сек')
elif 3600 <= duration <= 86399:
    print(f'{duration // 3600} час {duration % 3600 // 60} мин {duration % 60} сек')
else:
    print(f'{duration // 86400} дн {duration % 86400 // 3600} час {duration % 86400 % 3600 // 60} мин {duration % 60} сек')

# вариант с несколькими значениями в списке
durations = [85, 80003, 5000, 0, 59, 86399]
idx = 0
while idx < len(durations):
    if 0 <= durations[idx] <= 59:
        print(f'{durations[idx]} сек')
    elif 60 <= durations[idx] <= 3599:
        print(f'{durations[idx] // 60} мин {durations[idx] % 60} сек')
    elif 3600 <= durations[idx] <= 86399:
        print(f'{durations[idx] // 3600} час {durations[idx] % 3600 // 60} мин {durations[idx] % 60} сек')
    else:
        print(
            f'{durations[idx] // 86400} дн {durations[idx] % 86400 // 3600} час {durations[idx] % 86400 % 3600 // 60} мин {durations[idx] % 60} сек')
    idx += 1
