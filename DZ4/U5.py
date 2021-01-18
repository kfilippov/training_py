# Кonstantin Filippov 06.01.2021
# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import functools
import datetime

def f_classic(list):
    mult = 1
    for el in list:
        mult = mult * el
    return mult

def f_reduce(list):
    mult = functools.reduce(lambda a, b: a*b, list)
    return mult

def f_generator(generator_obj):
    mult = 1
    while True:
        try:
            mult = mult *  next(generator_obj)
        except Exception as err:
            break
    return mult

def f_gen_reduce(generator_obj):
    mult = functools.reduce(lambda a,b: a*b, generator_obj )
    return mult

def d4u5():
    lst = [el for el in range(100, 1000 + 1) if el % 2 == 0]

    go1 = (el for el in range(100, 1000 + 1) if el % 2 == 0)
    go2 = (el for el in range(100, 1000 + 1) if el % 2 == 0)

    print(f"Список....................: {lst}")
    print(f"Произведение (классически): {f_classic(lst)}")
    print(f"Произведение (reduce).....: {f_reduce(lst)}")
    print(f"Произведение (generator)..: {f_generator(go1)}")
    print(f"Произведение (gen,reduce).: {f_gen_reduce(go2)}")


d4u5()