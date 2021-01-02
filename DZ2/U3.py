# Кonstantin Filippov 02.01.2021
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
def f_get_value_of(descr, help):
    while True:
        x = input(f'Введите {descr}: ')
        try:
            x = int(x)
            if x < 1 or x > 12:
                print(f'Введите {descr} {help}.')
                continue
            return x
        except ValueError as err:
            print(f"Значение \"{x}\" не удалось привести к целочисленному типу.\nОшибка: ", err)


def f_get_season_list_simple(month):
    lv_winter = [1, 2, 12]
    lv_spring = [3, 4, 5]
    lv_summer = [6, 7, 8]
    lv_autumn = [9, 10, 11]

    if (month in lv_autumn):
        return 'Осень'
    elif (month in lv_spring):
        return 'Весна'
    elif (month in lv_summer):
        return 'Лето'
    elif (month in lv_winter):
        return 'Зима'


def f_get_season_list_advanced(month):
    lv_seasons = [
          ['Весна', [3, 4, 5]]
        , ['Лето', [6, 7, 8]]
        , ['Осень', [9, 10, 11]]
        , ['Зима', [1, 2, 12]]
    ]

    for el in range(len(lv_seasons)):
        if month in lv_seasons[el][1]:
            return lv_seasons[el][0]


def f_get_season_from_dict(month):
    lv_dict = {1: 'Зима',
               2: 'Зима',
               3: 'Весна',
               4: 'Весна',
               5: 'Весна',
               6: 'Лето',
               7: 'Лето',
               8: 'Лето',
               9: 'Осень',
               10: 'Осень',
               11: 'Осень',
               12: 'Зима'}
    return lv_dict.get(month)


def f_get_season_from_dict_advanced(month):
    # Альтернативно - заполнение словаря из списка:
    lv_dict = {month + 1: f_get_season_list_advanced(month + 1) for month in range(12)}
    return lv_dict.get(month)


def d2u3():
    lv_tab = "\t:\t"
    my_month = f_get_value_of('номер месяца', 'от 1 до 12')
    print(f"Месяц {my_month:02} - это {lv_tab}",
          f_get_season_list_simple(my_month),
          f"{lv_tab}результат получен проверкой списка.")
    print(f"Месяц {my_month:02} - это {lv_tab}",
          f_get_season_list_advanced(my_month),
          f"{lv_tab}результат получен проверкой вложенного списка.")
    print(f"Месяц {my_month:02} - это {lv_tab}",
          f_get_season_from_dict(my_month),
          f"{lv_tab}результат получен проверкой словаря.")
    print(f"Месяц {my_month:02} - это {lv_tab}",
          f_get_season_from_dict_advanced(my_month),
          f"{lv_tab}результат получен проверкой словаря (заполнен из из списка).")


###
d2u3()
