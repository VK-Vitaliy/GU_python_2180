"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""


class NotNumberError(Exception):
    pass


class HRDepartament:
    office_equip = {'Printers': [],
                    'Scanners': [],
                    'Photocopiers': [],
                    }
    count_photocopiers = 0
    count_printers = 0
    count_scanners = 0

    def get_statistic(self):
        return f'\nHRDepartament has office equipments:\n' \
               f'Printers:\t {self.count_printers}\n' \
               f'Scanners:\t {self.count_scanners}\n' \
               f'Photocopiers:\t {self.count_photocopiers}\n'


class Accounting:
    office_equip = {'Printers': [],
                    'Scanners': [],
                    'Photocopiers': [],
                    }
    count_photocopiers = 0
    count_scanners = 0
    count_printers = 0

    def get_statistic(self):
        return f'\nAccounting has office equipments:\n' \
               f'Printers:\t {self.count_printers}\n' \
               f'Scanners:\t {self.count_scanners}\n' \
               f'Photocopiers:\t {self.count_photocopiers}\n'


class Warehouse:
    office_equip = {'Printers': [],
                    'Scanners': [],
                    'Photocopiers': [],
                    }
    count_photocopiers = 0
    count_scanners = 0
    count_printers = 0

    def get_statistic(self):
        return f'\nWarehouse has office equipments:\n' \
               f'Printers:\t {self.count_printers}\n' \
               f'Scanners:\t {self.count_scanners}\n' \
               f'Photocopiers:\t {self.count_photocopiers}\n'

    @staticmethod
    def come_equipment(serial_number, departament_id):  # принимает офисную технику на склад
        """
        :param serial_number: str serial_number of office equipment
        :param departament_id: str ([1] HRDepartament, [2] Accounting)
        """
        try:
            if not departament_id.isdigit():
                raise NotNumberError('Enter correct number of departament!')

            if int(departament_id) == 1:
                for type_equip, list_equip in HRDepartament.office_equip.items():
                    if type_equip == 'Printers':
                        for equip in list_equip:
                            for ser_num in equip.keys():
                                if ser_num == serial_number:
                                    Warehouse.office_equip['Printers'].append(equip)
                                    list_equip.remove(equip)
                                    HRDepartament.count_printers -= 1
                                    Warehouse.count_printers += 1
                    elif type_equip == 'Scanners':
                        for equip in list_equip:
                            for ser_num in equip.keys():
                                if ser_num == serial_number:
                                    Warehouse.office_equip['Scanners'].append(equip)
                                    list_equip.remove(equip)
                                    HRDepartament.count_scanners -= 1
                                    Warehouse.count_scanners += 1
                    else:
                        for equip in list_equip:
                            for ser_num in equip.keys():
                                if ser_num == serial_number:
                                    Warehouse.office_equip['Photocopiers'].append(equip)
                                    list_equip.remove(equip)
                                    HRDepartament.count_photocopiers -= 1
                                    Warehouse.count_photocopiers += 1
            elif departament_id == 2:
                for type_equip, list_equip in Accounting.office_equip.items():
                    if type_equip == 'Printers':
                        for equip in list_equip:
                            for ser_num in equip.keys():
                                if ser_num == serial_number:
                                    Warehouse.office_equip['Printers'].append(equip)
                                    list_equip.remove(equip)
                                    Accounting.count_printers -= 1
                                    Warehouse.count_printers += 1
                    elif type_equip == 'Scanners':
                        for equip in list_equip:
                            for ser_num in equip.keys():
                                if ser_num == serial_number:
                                    Warehouse.office_equip['Scanners'].append(equip)
                                    list_equip.remove(equip)
                                    Accounting.count_scanners -= 1
                                    Warehouse.count_scanners += 1
                    else:
                        for equip in list_equip:
                            for ser_num in equip.keys():
                                if ser_num == serial_number:
                                    Warehouse.office_equip['Photocopiers'].append(equip)
                                    list_equip.remove(equip)
                                    Accounting.count_photocopiers -= 1
                                    Warehouse.count_photocopiers += 1
        except NotNumberError as err:
            print(err)

    @staticmethod
    def leave_equipment(serial_number, departament_id: int):  # передает офисную технику со склада в отдел
        """
        :param serial_number: str serial_number of office equipment
        :param departament_id: int([1] HRDepartament, [2] Accounting)
        """
        if departament_id == 1:
            for type_equip, list_equip in Warehouse.office_equip.items():
                if type_equip == 'Printers':
                    for equip in list_equip:
                        for ser_num in equip.keys():
                            if ser_num == serial_number:
                                HRDepartament.office_equip['Printers'].append(equip)
                                list_equip.remove(equip)
                                HRDepartament.count_printers += 1
                                Warehouse.count_printers -= 1
                elif type_equip == 'Scanners':
                    for equip in list_equip:
                        for ser_num in equip.keys():
                            if ser_num == serial_number:
                                HRDepartament.office_equip['Scanners'].append(equip)
                                list_equip.remove(equip)
                                HRDepartament.count_scanners += 1
                                Warehouse.count_scanners -= 1
                else:
                    for equip in list_equip:
                        for ser_num in equip.keys():
                            if ser_num == serial_number:
                                HRDepartament.office_equip['Photocopiers'].append(equip)
                                list_equip.remove(equip)
                                HRDepartament.count_photocopiers += 1
                                Warehouse.count_photocopiers -= 1
        elif departament_id == 2:
            for type_equip, list_equip in Warehouse.office_equip.items():
                if type_equip == 'Printers':
                    for equip in list_equip:
                        for ser_num in equip.keys():
                            if ser_num == serial_number:
                                Accounting.office_equip['Printers'].append(equip)
                                list_equip.remove(equip)
                                Accounting.count_printers += 1
                                Warehouse.count_printers -= 1
                elif type_equip == 'Scanners':
                    for equip in list_equip:
                        for ser_num in equip.keys():
                            if ser_num == serial_number:
                                Accounting.office_equip['Scanners'].append(equip)
                                list_equip.remove(equip)
                                Accounting.count_scanners += 1
                                Warehouse.count_scanners -= 1
                else:
                    for equip in list_equip:
                        for ser_num in equip.keys():
                            if ser_num == serial_number:
                                Accounting.office_equip['Photocopiers'].append(equip)
                                list_equip.remove(equip)
                                Accounting.count_photocopiers += 1
                                Warehouse.count_photocopiers -= 1


class OfficeEquipment(Warehouse):
    def __init__(self, model, serial_number):
        self.name = model
        self.serial_number = serial_number


class Printer(OfficeEquipment):

    def __init__(self, model, serial_number, max_size_of_paper):
        super().__init__(model, serial_number)
        self.max_size_of_paper = max_size_of_paper
        Warehouse.office_equip['Printers'].append({serial_number: model})
        Warehouse.count_printers += 1


class Scanner(OfficeEquipment):

    def __init__(self, model, serial_number, color_depth):
        super().__init__(model, serial_number)
        self.color_depth = color_depth
        Warehouse.office_equip['Scanners'].append({serial_number: model})
        Warehouse.count_scanners += 1


class Photocopier(OfficeEquipment):

    def __init__(self, model, serial_number, speeding_copy):
        super().__init__(model, serial_number)
        self.speeding_copy = speeding_copy
        Warehouse.office_equip['Photocopiers'].append({serial_number: model})
        Warehouse.count_photocopiers += 1


ph_copier1 = Photocopier('Xerox N91', '32168', '30 p/min')
printer1 = Printer('Canon G130', '214Sf', 'A4')
printer2 = Printer('Canon 7130', '2897f', 'A4')
scanner1 = Scanner('Fujitsu', 'i940', '24 bit')

print(f'Список техники на складе:\n'
      f'Принтеры: {Warehouse.office_equip["Printers"]}\n'
      f'Сканеры: {Warehouse.office_equip["Scanners"]}\n'
      f'Копиры: {Warehouse.office_equip["Photocopiers"]}\n')
w1 = Warehouse
print(w1.get_statistic(w1))
w1.leave_equipment('214Sf', 1)
hr1 = HRDepartament
print(w1.get_statistic(w1))
print(hr1.get_statistic(hr1))
w1.come_equipment('214Sf', '1ff')
w1.come_equipment('214Sf', '1')
print(w1.get_statistic(w1))
