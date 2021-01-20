# Кonstantin Filippov 20.01.2021
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _length_m = 0
    _width_m  = 0


    def __init__(self, iv_length_m, iv_width_m):
        self._length_m = iv_length_m
        self._width_m  = iv_width_m

    def get_mass(self, height_cm, density_kg_m3):
        return self._width_m * self._length_m * height_cm/100 * density_kg_m3

def d6u2():
    try:
        r = Road(int(input("Введите длину дороги, м:")), int(input("Введите шиирну дороги, м:")))
        print(r.get_mass(int(input("Введите толщину покрытия, см:")), int(input("Введите плотность кг/м3: "))), " кг")
    except Exception as err:
        print("Ошибка: ", err)

d6u2()