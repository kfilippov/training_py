# Кonstantin Filippov 20.01.2021
# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
#
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
#
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
#
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

from math import floor
from random import randrange

class Cell:
    number_of_cells = 0.0

    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return  Cell(self.number_of_cells - other.number_of_cells)

    def __mul__(self, other):
        return  Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return  Cell(self.number_of_cells // other.number_of_cells)

    def _make_order(self, n, is_print: bool):
        r = int(floor(self.number_of_cells))
        rs = ''
        i = 1
        if i > n or i > r:
            return rs

        if is_print: print()
        rs = '\n'

        while i <= r:
            if is_print: print("*", end='')
            rs = rs + "*"
            if ( i  % n ) == 0:
                if is_print: print()
                rs = rs + "\n"
            i += 1

        return rs

    def make_order(self, n):
        self._make_order(n, True)

    def __str__(self):
        return self._make_order(10, False)


def d7u3():
    n1 = randrange(15, 25)
    n2 = randrange(10, 20)

    cell1 = Cell(n1)
    cell2 = Cell(n2)
    print(n1, "и ", n2, "- ячеечные клетки созданы:")

    print("\n--\nКлетка #1", cell1)
    print("\n--\nКлетка #2", cell2)

    cell3 = cell1 + cell2
    print("\n--\nКлетка Сумма:", cell3)

    cell3 = cell1 - cell2
    print("\n--\nКлетка Разница", cell3)

    cell3 = cell1 * cell2
    print("\n--\nКлетка Умножение", cell3)

    cell3 = cell1 / cell2
    print("\n--\nКлетка деление", cell3)

    x = randrange(5, 9)
    print("\n--\nКлетка 1 печать в %s колонок" % x)
    cell1.make_order(x)

d7u3()



