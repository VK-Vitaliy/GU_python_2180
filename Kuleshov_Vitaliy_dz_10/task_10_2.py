from abc import ABC, abstractmethod


class Clothes(ABC):
    total_consumption = 0  # счетчик затрат ткани

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def consumption(self):
        result = round(self.size / 6.5 + 0.5, 2)
        Clothes.total_consumption += result
        return result

    def __str__(self):
        return f'{self.name}, размер {self.size} - расход {self.consumption}м ткани'


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def consumption(self):
        result = round(2 * self.height + 0.3, 2)
        Clothes.total_consumption += result
        return result

    def __str__(self):
        return f'{self.name}, рост {self.height} - расход {self.consumption}м ткани'


my_coat = Coat('Красивое пальто', 48)
my_coat2 = Coat('Некрасивое пальто', 40)
my_suit = Suit('Деловой костюм', 176)
print(my_coat)
print(my_coat2)
print(my_suit)

print(Clothes.total_consumption)
