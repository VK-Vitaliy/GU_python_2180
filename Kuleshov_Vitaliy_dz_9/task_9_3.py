class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        '''
        :param name: имя сотрудника
        :param surname: фамилия сотрудника
        :param position: должность
        :param wage: оклад по должности
        :param bonus: премия по должности
        '''
        self.name = str(name).lower()
        self.surname = str(surname).lower()
        self.position = str(position).lower()
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def get_full_name(self):
        return f'\tПолное имя сотрудника: {self.name.title()} {self.surname.title()}.'

    def get_total_income(self):
        total_income = sum(self._income.values())
        return f'\tДоход по должности "{self.position}", с учетом премии составляет - {total_income} руб.'


user_1 = Position('максим', 'дулимов', 'слесарь', 35000, 10000)
print(user_1.get_full_name())
print(user_1.get_total_income())
