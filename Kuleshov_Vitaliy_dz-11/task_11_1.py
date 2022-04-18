# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date):
        if self.valid_date(date):
            self.date = date
        else:
            raise ValueError('Введите дату в формате строки "день-месяц-год"')

    @classmethod
    def get_date_int(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def valid_date(date):
        date_num = Date.get_date_int(date)
        valid_num = True
        if len(date_num) != 3:
            valid_num = False
        elif not 1 <= date_num[0] <= 31:
            valid_num = False
        elif not 1 <= date_num[1] <= 12:
            valid_num = False
        elif date_num[2] < 0:
            valid_num = False
        return valid_num


d1 = Date('31-12-2011')
print(d1.get_date_int(d1.date))
print(d1.valid_date(d1.date))
