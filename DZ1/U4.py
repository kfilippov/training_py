# Кonstantin Filippov 26.12.2020
# 4)	Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
# цикл while и арифметические операции.
def get_number():
    while (True):
        a = input('Введите целое положительное число:')
        try:
            a = int(a)
            if a < 0 :
                print('Вы ввели отрицательное число, расчёт будет произведён по модулю.')
                return abs(a)
            return a
        except ValueError:
            print(f'{a} не удалось привести к целочисленному типу. Попробуйте снова.')

def print_max_digit(number):
    decimal = 10
    tmp_number = number
    max_digit = tmp_number % 10

    while ( True ) :
        tmp_number = tmp_number // decimal
        if tmp_number == 0:
            break
        elif max_digit < tmp_number % decimal:
            max_digit =  tmp_number % decimal
    print(max_digit)

def d1u4():
    print_max_digit(get_number())

d1u4()

