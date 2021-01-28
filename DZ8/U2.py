# Кonstantin Filippov 22.01.2021
#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnDivByZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt

numerator   = input("Введите числитель..:  ")
denominator = input("Введите знаменатель:  ")

try:
    numerator = int(numerator)
    denominator = int(denominator)
    if denominator == 0 :
        raise OwnDivByZeroException("Вы ввели ноль в знаменателе.")
except  ValueError as val_err:
    print("Вы ввели не число ", val_err)
except OwnDivByZeroException as err:
    print(err)
else:
    print("Результат деления..: ", numerator/denominator)