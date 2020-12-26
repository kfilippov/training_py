# Кonstantin Filippov 26.12.2020
# 2)	Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#     Используйте форматирование строк.
import datetime

def get_seconds():
    max_seconds = 86400
    min_seconds = 0

    while (True):
        a = input('Введите время в секундах(целое число): ')
        try:
            a = int(a)
            if ( a > max_seconds or a < min_seconds ) :
                print("В сутках только 60*60*24 секунд. Попробуйте ввести число от 0 до 86400.")
                continue
            return a
        except ValueError:
            print(f'"{a}" не удалось привести к целочисленному типу. Попробуйте снова.')

def print_seconds_formatted(a):

    seconds_in_hour    = 60*60
    seconds_in_minute  = 60

    try:
        a = int(a)
    except ValueError:
        print(f'{a} не удалось привести к целочисленному типу. Попробуйте снова.')

    hours = a // seconds_in_hour
    if len(str(hours)) < 2:
        hours = '0'+ str(hours)
    minutes = (a % seconds_in_hour ) // seconds_in_minute
    if len(str(minutes)) < 2:
        minutes = '0'+ str(minutes)
    seconds = a % seconds_in_minute
    if len(str(seconds)) < 2:
        seconds = '0' + str(seconds)
    print(f"Вы ввели время: {hours}:{minutes}:{seconds}")

def d1u2():
    print_seconds_formatted(get_seconds())

d1u2()
