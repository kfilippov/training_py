# Кonstantin Filippov 09.01.2021
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def d5u5():
    import random as r
    file  = 'numbers.txt'
    read  = 'r'
    write = 'w'
    space = " "
    n     = 10

    with open(file, write) as outp:
        i = 0
        for el in range(r.randrange(n, 1 + r.randrange(n, n*n))):
            if i == 0 :
                outp.write( str(r.randrange(el, 1+r.randrange(n,n*n))) )
            else:
                outp.write(space + str(el))
            i += 1

    with open(file) as inp:
        row1 = [ n for n in next(inp).split(' ') ]


    print("Массив в файле %s", row1)

    sum = 0
    for el in row1:
        if el != '':
           sum += int(el)

    print("Сумма чисел в файле: %s" % sum)

d5u5()
