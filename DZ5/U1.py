# Кonstantin Filippov 09.01.2021
# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

def d5u1():
    import os
    cwd = os.getcwdb()

    filename = "U1_texts.txt"
    print(f"Текущая рабочая директория: {cwd}")
    filename2 = input(f"Введите путь и имя файла [Enter чтобы записать в файл по умолчанию: {filename}]")

    if filename2 != "":
        filename = filename2

    f_obj = open(filename, "w")
    while ( True ):
        str = input(f"Запись в {filename}, Enter для завершения >>")
        if str == "":
            f_obj.close()
            print(f"Файл \"{f_obj.name}\" записан.")
            break
        else:
            f_obj.write(str)

    f_obj.close()

d5u1()