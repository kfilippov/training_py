# Кonstantin Filippov 20.01.2021
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = ""
    surname = ""
    position = ""
    _income = dict()


class Position(Worker):

    def __init__(self, iv_name, iv_surname, iv_position, iv_wage, iv_bonus):
        self.name = iv_name
        self.surname = iv_surname
        self.position = iv_position
        self._income = {"wage": iv_wage, "bonus": iv_bonus}

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return int(self._income.get("wage")) + int(self._income.get("bonus"))

def d6u3():
    # demo

    demo = [["Имя........:",
            "Фамилия....:",
            "Должность..:",
            "Основная ЗП:",
            "Бонус......:" ],
            ["Иван", "Иванов", "Генеральный директор", 20_195, 2019]]

    print("Введите данные сотрудника, Enter - оставить как есть.")
    i = 0
    for descr in demo[0]:
        tmp = input(f"{descr} [{demo[1][i]}]: ")
        if tmp != "":
            demo[1][i] = tmp
        i += 1
    try:
        pos = Position(demo[1][0],demo[1][1],demo[1][2], int(demo[1][3]), int(demo[1][4]))

        print("\nСоздан объект Position:\n-----------------")
        print(demo[0][0], pos.name)
        print(demo[0][1], pos.surname)
        print(demo[0][2], pos.position)
        print("Полное имя:", pos.get_full_name())
        print("Полная ЗП.:", pos.get_total_income())

    except Exception as err:
        print("Ошибка: ", err)



d6u3()