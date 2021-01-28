# Кonstantin Filippov 22.01.2021
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

from math import floor
from random import randrange

class Complex:
    """
    Комплексное число вида z = a +bi,
     где:
       а - вещественная часть
       b - мнимая часть

     Проверено: https://www.kontrolnaya-rabota.ru/s/kopleksnyie-chisla/

    """
    a : int
    b : int

    def __init__(self, a , b):
        self.a  = a
        self.b  = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.b* other.a + self.a * other.b)

    def __str__(self):
        return (str(self.a)+" + ("+str(self.b)+")*i")

def d8u7():
    a1 = randrange(3, 25)
    b1 = randrange(10, 20)

    a2 = randrange(-10, 20)
    b2 = randrange(10, 20)

    c1 = Complex(a1, b1)
    c2 = Complex(a2, b2)
    c3 : Complex

    print("Комплексные числа созданы:")

    print("Комплексное число #1", c1)
    print("Комплексное число #2", c2)

    c3 = c1 + c2
    print("Комплексное число Сумма:", c3)

    c3 = c1 * c2
    print("Комплексное число Умножение", c3)

d8u7()

