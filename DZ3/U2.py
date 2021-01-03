# Кonstantin Filippov 03.01.2021
# 2.	Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой

def print_info(name, lastname, birth_year, city, email, phone):
    print("..............--===--..............")
    print(f"Вы ввели: , {name}, {lastname}, {birth_year}, {city}, {email}, {phone}")


def get_info():
    name = input("Введите имя.............:")
    lastname = input("Введите фамилию.........:")
    birth_year = input("Введите год рождения....:")
    city = input("Введите город проживания:")
    email = input("Введите email...........:")
    phone = input("Введите телефон.........:")

    print_info( name, lastname, birth_year, city, email, phone)


def d3u2():
    get_info()


###
d3u2()