# Кonstantin Filippov 03.01.2021
# 3.	Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def max (x, y):
    try:
        if x >= y:
            return float(x)
        else:
            return float(y)
    except (ValueError, TypeError) as err:
        print('Ошибка: ', err)

def my_func(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a >= b and a >= c :
            return (a+max(b,c))
        elif b >= c and b >= a :
            return (b + max(a, c))
        elif c >= b and c >= a :
            return (c + max(b, a))
    except (ValueError, TypeError)  as err:
        print('Ошибка: ', err)


def d3u3():
    result = my_func(input("Введите 3 числа, a = "), input(" b= "), input(" c = "), )
    print("Сумма 2 наибольших чисел составила: ", result)

d3u3()

