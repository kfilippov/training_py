# Кonstantin Filippov 22.01.2021
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from random import randrange

class Date:
    date_numerator = 10 ** 6
    month_numerator = 10 ** 4

    year_denominator = 10**4
    month_denominator = 10**6


    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):

        list = date.split("-")

        rv  = int(list[0]) * cls.date_numerator
        rv += int(list[1]) * cls.month_numerator
        rv += int(list[2])
        return rv

    @staticmethod
    def validate(date):
        if date > 31129999:
            return False

        try:
            year  = int( date % Date.year_denominator)
            month = int( (date % Date.month_denominator -  year ) / Date.year_denominator )
            day   = int((date - date % Date.month_denominator ) / Date.month_denominator)
        except Exception as err:
            print(err)
            return False
        if year < 1 or month < 1 or day < 1:
            return False
        if month > 12:
            return False
        if year % 4 == 0 and month == 2 and day > 29:
            return False
        if year % 4 != 0 and month == 2 and day > 28:
            return False
        if month in [1,3,5,7,8,10,12] and day > 31:
            return False
        if month in [4,6,9,11] and day > 30:
            return False

        return True

def d8u1():
    for e in range(randrange(10,20)):
        demo_day = randrange(1,120)
        if demo_day < 10: demo_day = "0"+str(demo_day)
        else: demo_day = str(demo_day)

        demo_month = randrange(1,15)
        if demo_month < 10: demo_month = "0"+str(demo_month)
        else: demo_month = str(demo_month)

        demo_year = randrange(1,9999)
        if    demo_year < 10  : demo_year = "000"+str(demo_year)
        elif  demo_year < 100 : demo_year = "00" +str(demo_year)
        elif  demo_year < 1000: demo_year = "0"  +str(demo_year)
        else: demo_year = str(demo_year)

        demo_date = demo_day+"-"+demo_month+"-"+demo_year

        date_o = Date(demo_date)

        date_i = Date.get_date(date_o.date)

        print("Date as string...............:", demo_date)
        print("Date as number...............:", date_i)
        print("Date validation successfull? :", Date.validate(date_i), "\n")

d8u1()