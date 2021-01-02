# Кonstantin Filippov 02.01.2021
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел   : 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
def f_get_value_of(descr, help):
    while True:
        x = input(f'Введите {descr}: ')
        try:
            x = int(x)
            if x < 1 :
                print(f'Введите {descr} {help}.')
                continue
            return x
        except ValueError as err:
            print(f"Значение \"{x}\" не удалось привести к целочисленному типу.\nОшибка: ", err)

def f_add(list, value):
    if value >= list[0]:
        list.insert(0, value)
    elif value <= list[len(list)-1]:
            list.insert(len(list), value)
    else:
        for el in range(len(list)):
            if list[el] <= value:
                list.insert(el, value)
                break
    return list


def d2u5():
    my_list = [7, 5, 3, 3, 2]
    print('Изначальный список ', my_list)
    no_of_inputs = f_get_value_of('число добавляемых элементов списка', 'оно должно быть натуральным 1, 2, 3, и т.д.')
    for el in range(no_of_inputs):
        f_add(my_list, f_get_value_of(f'целое число [{el+1}/{no_of_inputs}]:',
                                       'оно должно быть натуральным 1, 2, 3, и т.д.')
               )
        print('Расширенный список ', my_list)

d2u5()




