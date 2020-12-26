# Кonstantin Filippov 26.12.2020
# 1) Поработайте с переменными, создайте несколько, выведите на экран,
#    запросите у пользователя несколько чисел и
#    строк и сохраните в переменные, выведите на экран.

def my_get(var_type):
    while( True ):
        if var_type == 'int':
            a = input('Введите целочисленную переменную: ')
            try:
                a = int(a)
                # break
                return a
            except ValueError:
                print(f'"{a}" не удалось привести к целочисленному типу. Попробуйте снова.')
        elif var_type == 'float':
            b = input('Введите дробную переменную(разделитель - точка): ')
            try:
                b = float(b)
                # break
                return b
            except ValueError:
                print(f'"{b}" не удалось привести к дробному типу. Попробуйте снова.')
        elif var_type == 'string':
            c = input('Введите строковую переменную: ')
            try:
                c = str(c)
                # break
                return c
            except ValueError:
                print(f'"{c}" не удалось привести к дробному типу. Попробуйте снова.')
        else:
            return;

def d1u1():
    # считываем и распечатываем
    i  = my_get('int')
    f  = my_get('float')
    s1 = my_get('string')
    s2 = my_get('string')

    # печать
    print('Целочисленная ', i, 'Дробная =', f, f'Строковая1 = "{s1}"', f'Строковая2 = "{s2}"')

d1u1()