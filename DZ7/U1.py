# Кonstantin Filippov 20.01.2021
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

from copy import deepcopy
class Matrix:


    def __init__(self, matrix ):
        """ конструктор """
        self.matrix = matrix

    def __str__(self):
        """ переопределение str() """
        string = str()
        for line in self.matrix:
            string = string +"("
            for cell in line:
                string = string + str(cell)+ "\t"
            string = string + ")\n"
        return(str(string))

    def __add__(self, other):
        """ переопределение суммирования. Суммируем матрицы, необязательно полные и разных размеров """

        # определяем размеры результата
        max_i = max(len(self.matrix), len(other.matrix))
        max_j = max(Matrix.__get_max_j(self.matrix), Matrix.__get_max_j(other.matrix))

        # создаём пустую матрицу
        matrix = Matrix.__create_empty_matrix(max_i, max_j)

        # добавляем к пустой матрице матрицы производльных размеров, включая неполные
        matrix = Matrix.__add_simple(matrix, self.matrix)
        matrix = Matrix.__add_simple(matrix, other.matrix)

        return Matrix(matrix)

    @staticmethod
    def __get_max_j(matrix):
        """ получаем наибольший размер 2-го измерения для случая неполной матрицы"""
        max_j = 0
        for line in matrix:
            if len(line) > max_j:
                max_j = len(line)
        return max_j

    @staticmethod
    def __create_empty_matrix(max_i, max_j):
        """ создаём пустую полную матрицу """
        matrix = []
        for i in range(max_i):
            column = []
            for j in range(max_j):
                column.append(0)
            matrix.append(column)
        return matrix

    @staticmethod
    def __add_simple(matrix, other):
        """ Добавляем к матрице другую, меньшего или равного размера в т.ч. неполную"""
        rv_matrix = deepcopy(matrix)
        i = 0
        j = 0
        for line in other:
            for cell in line:
                rv_matrix[i][j] += int(cell)
                j += 1
            i += 1
            j = 0

        i = 0
        j = 0
        return rv_matrix

def demo_print(text, list1, list2):
    m1 = Matrix(list1)
    m2 = Matrix(list2)

    print(text, "\n-----------------")

    print("Слагаемое 1")
    print(m1)

    print("Слагаемое 2")
    print(m2)

    print("Сумма матриц")
    m3 = m1 + m2
    print(m3)

def d7u1():
    demo_print("пример №1", [[1,2,3],[4,5,6],[7,8,9]] ,
                            [[9,8,7],[6,5,4],[3,2,1]] )

    demo_print("пример №2", [[1,2,3],[4,5,6],[7,8,9]],
                            [[9,8  ],[6,5,4],[3,2,1,99]] )

    demo_print("пример №3",[[9, 8], [6, 5, 4], [3, 2, 1, 99]],
                           [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  )
d7u1()