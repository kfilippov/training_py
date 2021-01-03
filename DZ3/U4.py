# Кonstantin Filippov 03.01.2021
# 4.	Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def f_pow_simple(x, y):
    try:
        z = float(x) ** float(y)
        return z
    except ValueError as err:
        print("Ошибка: ", err)


def f_pow_advanced(x, y):
    try:
        x = float(x)
        y = int(y)
        if y == 0:
            return 1
        else:
            z = 1
            for i in range(abs(y)):
                z = z * (1 / x)
            return z
    except ValueError as err:
        print("Ошибка: ", err)


def d3u4():
    try:
        x = input("Введите возводимое в степень действительное положительное число x:")
        if float(x) < 0:
            raise ValueError("число \"x\" должно быть положительным")
        else:
            y = input("Введите степень, целое отрицательное число y:")
            if int(y) >= 0:
                raise ValueError("число \"y\" должно быть отрицательным")
            else:
                z = f_pow_simple(x, y)
                print(f"Результат возведения в степень (оператором) x^y = {x}^{y} = {z}")
                z = f_pow_advanced(x, y)
                print(f"Результат возведения в степень (  циклом  ) x^y = {x}^{y} = {z}")
    except ValueError as err:
        print("Ошибка: ", err)


d3u4()
