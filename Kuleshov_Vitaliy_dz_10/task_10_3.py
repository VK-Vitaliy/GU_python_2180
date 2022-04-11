class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return self.quantity - other.quantity
        else:
            return 'Не могу сделать вычитание клеток'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __floordiv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, num_in_arrow):
        result = ''
        for i in range(self.quantity // num_in_arrow):
            result = result + ('*' * num_in_arrow) + '\\n'
        result += ('*' * (self.quantity % num_in_arrow))
        print(result)


cell_1 = Cell(3)
cell_2 = Cell(22)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_2 // cell_1)
cell_2.make_order(4)
