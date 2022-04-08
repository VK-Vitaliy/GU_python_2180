class Stationery:
    title = 'канцелярские принадлежности'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск маркером')

stationery = Stationery()
pens = Pen()
pencils = Pencil()
handles = Handle()
print(stationery.draw())
print(pens.draw())
print(pencils.draw())
print(handles.draw())

