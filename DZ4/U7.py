# Кonstantin Filippov 06.01.2021
# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение.
#
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
#
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def f_gen_fact(n):
    cnt = 0
    fact = 1
    while cnt < n:
        cnt += 1
        fact *= cnt
        yield fact

def d4u7():

    try:
        n = int(input("Факториал числа: "))
    except Exception as err:
        print("Ошибка:", err)

    values = dict()
    fact = f_gen_fact(n)
    for el in range(n):
        if el == 0:
            print("Равен: ", el+1, end = '')
        else:
            print(" * ", el+1, end='')
        fact_result = next(fact)
        values.update({el+1 : fact_result})

    print(" = ", fact_result)
    print("Промежуточные значения факториала:", values)
d4u7()
