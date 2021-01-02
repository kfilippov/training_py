# Кonstantin Filippov 02.01.2021
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

def d2u1():
    lv_list = ['Курс Python начат в', 2020, "году.", True, 1.0, 0b111, 0o77, 0x0FF3]

    lv_list[0] = lv_list[0].split()

    lv_list.append((1, 2, 3))

    lv_list.append({0, 1, 'A'})

    lv_list.append({'A':1, 'B':2})

    lv_list.append ( (i for i in range(3)) )

    lv_list.append( lambda z: z**2 + 1 )

    lv_list.append(lv_list[12](11))

    lv_tab = "\t:\t"
    for lv_element in range(len(lv_list)):
        print(lv_element, lv_tab, type(lv_list[lv_element]), lv_tab,  lv_list[lv_element])

###

d2u1()