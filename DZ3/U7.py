# Кonstantin Filippov 03.01.2021
# 7.	Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(s):
    return str(s).capitalize()

def int_multi(s):
    l = str(s).split()
    result = ""
    for el in l:
        if result != "":
            result = result + " "
        result = result + int_func(el)
    return result

def d3u7():
    s1 = \
    input("Введите слова с маленькой буквы: ")
    s2 = int_multi(s1)
    print("Слова с большой буквы          :", s2)

d3u7()
