# Кonstantin Filippov 06.01.2021
# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

def get_salary(rate, hours, bonus):
    return hours * rate + bonus

def d4u1(args):
    try:
        if args[2] == "" or args[1] == "" or args[3] == "":
            print("Запуск с обязательными параметрами: python U1.py <rate> <hours> <bonus>")
            return
        else:
            print("Ставка в час     :", args[1])
            print("Выработка в часах:", args[2])
            print("Премия           :", args[3])
            print("------------------")
            print("Зарплата         :", get_salary(float(args[1]), float(args[2]), float(args[3])))

    except Exception as e:
        print("Запуск с обязательными параметрами: python U1.py <rate> <hours> <bonus>")
        print(e)

from sys import argv

d4u1(argv)
