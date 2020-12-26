# Кonstantin Filippov 26.12.2020
# 3)	Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

def get_number():
    while (True):
        a = input('Введите число:')
        try:
            a = int(a)
            if a < 0 :
                print('Вы ввели отрицательное число, расчёт будет произведён по модулю.')
                return abs(a)
            return a
        except ValueError:
            print(f'{a} не удалось привести к целочисленному типу. Попробуйте снова.')

def get_degree(number):
    decimal = 10
    while (number // decimal > 0):
        try:
            decimal = decimal * 10
        except ValueError:
            print(f'приехали, похоже что вы ввели слишком большое число.')
    return decimal

def d1u3()
    n      = get_number()
    degree = get_degree(n)
    n2     = n + n*degree
    n3     = n2 + n*(degree**2)

    print(f'{n},{n2},{n3}')

d1u3()