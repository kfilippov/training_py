# Кonstantin Filippov 20.01.2021
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    speed = 0.0
    color = ""
    name = ""
    is_police = False
    def __init__(self, speed, color, name, is_police):
        self.speed      = speed
        self.color      = color
        self.name       = name
        self.is_police  = is_police

    def show_speed(self):
        print("speed: ", self.speed)

    def go(self):
        print("go")

    def stop(self):
        print("stop")

    def turn(self, direction):
        print("turn ", direction)

class TownCar(Car):
    max_speed = 60
    def show_speed(self):
        if self.speed > self.max_speed:
            print("ATTENTION! speed: ", self.speed)
        else:
            print("speed: ", self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    max_speed = 40
    def show_speed(self):
        if self.speed > self.max_speed:
            print("ATTENTION! speed: ", self.speed)
        else:
            print("speed: ", self.speed)

class PoliceCar(Car):
    pass

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

def d5u4():

    while True:
        tmp = input("Введите цифру чтобы создать (1 - TownCar, 2 - SportCar, 3 - WorkCar, 4 - PoliceCar) выход-Enter: ")
        if tmp == "":
            break
        try:
            tmp = int(tmp)
            if tmp == 1:
                o = TownCar(
                    float(input("speed:")),
                    input("color:"),
                    input("name:"),
                    bool(("is_police:")) )
            elif tmp == 2:
                o = SportCar(
                    float(input("speed:")),
                    input("color:"),
                    input("name:"),
                    bool(("is_police:")))
            elif tmp == 3:
                o = WorkCar(
                    float(input("speed:")),
                    input("color:"),
                    input("name:"),
                    bool(("is_police:")))
            elif tmp == 4:
                o = PoliceCar(
                    float(input("speed:")),
                    input("color:"),
                    input("name:"),
                    bool(("is_police:")))

            o.show_speed()
            o.stop()
            o.go()
            o.turn(direction=input("Turn direction: "))
        except Exception as err:
            print("Ошибка: ", err)

d5u4()