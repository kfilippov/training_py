# Кonstantin Filippov 20.01.2021
# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from random import  randrange

class Odezhda(ABC):
    @abstractmethod
    def __init__(self, size):
        pass



    @abstractmethod
    def calc_tkan(self):
        pass

class Palbto(Odezhda):
    V = 0

    def __init__(self, size):
        self.V = size

    @property
    def calc_tkan(self):
        return (self.V/6.5 +0.5)


class Kostyum(Odezhda):
    H = 0

    def __init__(self, size):
        self.H = size

    @property
    def calc_tkan(self):
        return (2*self.H + 0.3)

def d7u2():
    p = Palbto(randrange(50,70))
    k = Kostyum(randrange(150,195))

    print(f"Потребуется ткани на пальто  {p.V} размера:", p.calc_tkan)
    print(f"Потребуется ткани на костюм {k.H} роста..:", k.calc_tkan)

d7u2()

