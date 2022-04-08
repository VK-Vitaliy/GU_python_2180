class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала!'

    def stop(self):
        return f'Машина {self.name} оставилась'

    def turn(self, direction):
        if direction == 'L':
            direction = 'налево'
        elif direction == 'R':
            direction = 'направо'
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость машины {self.name}: {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Машина {self.name} превышает скорость! {self.speed} км/ч'
        else:
            return f'Текущая скорость машины {self.name}: {self.speed} км/ч'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Машина {self.name} превышает скорость! {self.speed} км/ч'
        else:
            return f'Текущая скорость машины {self.name}: {self.speed} км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - машина полиции'
        else:
            return f'{self.name} - не является машиной полиции'


# Задаём атрибуты: speed, color, name, is_police
porsche = SportCar(110, 'чёрный', 'Porsche', False)
lada = TownCar(70, 'синий', 'Lada Granta', False)
mercedes = WorkCar(50, 'белый', 'Mercedes-Benz', False)
skoda = PoliceCar(120, 'белый', 'Scoda', True)
kia = TownCar(90, 'белый', 'KIA', False)

print(f'\nВыполняем доступ к атрибутам:')
print(f'\t{porsche.speed}')
print(f'\t{lada.color}')
print(f'\t{mercedes.name}')
print(f'\t{skoda.name} машина полиции: {skoda.is_police}')
print(f'\tЦвет машины {skoda.name}: {skoda.color}')

print(f'\nВызываем методы:')
print(f'\t{porsche.turn("L")}')
print(f'\t{lada.turn("R")}')
print(f'\t{mercedes.go()}\n\t{mercedes.show_speed()}')
print(f'\t{porsche.show_speed()}')
print(f'\t{kia.show_speed()}')
print(f'\t{skoda.show_speed()}')
