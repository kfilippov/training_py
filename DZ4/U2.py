# Кonstantin Filippov 06.01.2021
# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import random, randint, randrange


def get_list_simple(lst_in):
    lst_out = []
    in_len = len(lst_in)
    if in_len == 1:
        lst_out = [el for el in lst_in]
    else:
        for i in range(in_len):
            if i == 0:
                continue
            else:
                curr = lst_in[i]
                prev = lst_in[i - 1]

                if curr > prev:
                    lst_out.append(lst_in[i])
    return lst_out


def get_list_advanced(lst_in):
    lst_out = []
    in_len = len(lst_in)
    if in_len == 1:
        lst_out = [el for el in lst_in]
    else:
        g = (x for x in lst_in)
        try:
            for i in range(in_len):
                if i == 0:
                    prev = next(g)
                    continue
                curr = next(g)
                if curr > prev:
                    lst_out.append(curr)
                prev = curr
        except StopIteration as err:
            print(err)

    return lst_out


def d4u3():
    lst = [randrange(1, 10) for el in range(10)]

    print("Исходный список....: ", lst)
    print("Результат (простой): ", get_list_simple(lst))
    print("Исходный список....: ", lst)
    print("Результат (сложный): ", get_list_advanced(lst))
    print("Сохранены только лементы исходного списка,значения которых больше предыдущего элемента.")

d4u3()
