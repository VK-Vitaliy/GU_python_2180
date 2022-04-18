# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
import re


class ComplexNumber:
    def __init__(self, complex_number):
        self.real_coefficient = re.compile(f'\(([-+]?\d+)\s[+]').findall(complex_number)
        self.imaginary_coefficient = re.compile(f'\s([-+]?\d+)\w').findall(complex_number)
        self.imaginary_unit = re.compile(f'[-+]?\d+(\w)').findall(complex_number)

    def __add__(self, other):
        result = f'({int(self.real_coefficient[0]) + int(other.real_coefficient[0])} + ' \
                 f'{int(self.imaginary_coefficient[0]) + int(other.imaginary_coefficient[0])}{self.imaginary_unit[0]})'
        return result

    def __mul__(self, other):
        result = f'({int(self.real_coefficient[0]) * int(other.real_coefficient[0])} + ' \
                 f'{int(self.imaginary_coefficient[0]) * int(other.imaginary_coefficient[0])}{self.imaginary_unit[0]})'
        return result


complex_num1 = '(5 + -4i)'
complex_num2 = '(12 + 6i)'

c1 = ComplexNumber(complex_num1)
c2 = ComplexNumber(complex_num2)

print(c1 + c2)
print(c1 * c2)
