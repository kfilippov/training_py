# Кonstantin Filippov 06.01.2021
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

import itertools as it
from random import random, randint, randrange

def f_positive_number(txt):
    while True:
        try:
            iv = input(txt)
            iv = int(iv)
            if iv > 0:
                return iv
        except Exception as err:
            print(f"{txt}. Введено: {iv}. Ошибка: {err}")


def f_gen_int(fr, to):
   if to >= fr:
       cur = fr - 1
       while cur < to:
           cur += 1
           yield cur

def f_gen_list(lst, repeats):
    cur = 0
    l = len(lst)
    while cur < repeats:
        cur += 1
        yield lst[(cur-1) % l]


def d4u6():
     # 1
     print("\n===>  Часть 1. Целые числа с .. по.. ")
     to = 0
     fr = f_positive_number("Введите с ( больше нуля ): ")
     while to <= fr:
         to = f_positive_number(f"Введите по ( больше {fr} ): ")
         if to <= fr:
             print(f"Неверный ввод. Введённое {to} меньше или равно {fr}!")

     go = f_gen_int(fr, to)
     print(f"Сгенерированы целые числа: ", end='')
     for el in go:
         print(el, end=', ')


     list = [randrange(fr, to) for el in range(randrange(fr, to))]
     print(f"\n\n\n===>  Часть 2. Имеем список (длиной {len(list)}): {list}")

     repeats = to*randrange(fr+1,to+1)
     go2 = f_gen_list(list, repeats)
     print(f"\nГенератор сгенерировал {repeats} значние(й) в списке: ", end='')
     for el in go2:
         print(el, end=', ')



d4u6()