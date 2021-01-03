# Кonstantin Filippov 03.01.2021
# 6.	Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func_simple(s):
    return str(s).capitalize()

def int_func_advanced(s):
    return s[0:1].upper() + s[1:]

def d3u6():
    s1 = input("Введите слово: ")
    s2 = int_func_simple(s1)
    print("Слово с большой буквы (capitalize):", s2)
    s2 = int_func_advanced(s1)
    print("Слово с большой буквы (   срез   ):", s2)

d3u6()