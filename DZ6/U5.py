# Кonstantin Filippov 20.01.2021
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ""

    def draw(self):
        pass

    def test(self):
        print("", self.title)

class Pen(Stationery):
    def draw(self):
        self.title = "Pen"
        return self

class Pencil(Stationery):
    def draw(self):
        self.title = "Pencil"
        return self

class Handle(Stationery):
    def draw(self):
        self.title = "Handle"
        return self

def d6u5():
    Pen().draw().test()
    Pencil().draw().test()
    Handle().draw().test()

d6u5()
