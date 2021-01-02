# Кonstantin Filippov 02.01.2021
# 2. Для списка реализовать обмен значений соседних элементов,
# т.е.Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

def f_get_value_of(descr):
    while True:
        lv_len = input(f'Введите {descr}: ')
        try:
            lv_len=int(lv_len)
            if lv_len < 1:
                print('Введите число 1 или большее.')
                continue
            return lv_len
        except ValueError as err:
            print(f"Значение \"{lv_len}\" не удалось привести к целочисленному типу.\nОшибка: ", err)

def f_get_list(lv_len):
    lv_list = []
    for el in range(lv_len):
        lv_list.append(input(f"Введите [{el}]-й элемент списка:"))
    return  lv_list

def f_exchange(lv_list):
    lv_len = len(lv_list) // 2

    if lv_len >= 1:
        for e in range(lv_len):
            lv_list[e * 2], lv_list[e * 2 + 1] = lv_list[e * 2 + 1], lv_list[e * 2]
        return lv_list

def d2u2():
    my_list = f_get_list(f_get_value_of('длину списка'))
    print("\nВы ввели список:")
    print(my_list)

    new_list = f_exchange(my_list)
    print("\nРезультат - список, где заменены друг другом элементы с индексами 0 и 1, 2 и 3 и т.д.:")
    print(new_list)

###

d2u2()