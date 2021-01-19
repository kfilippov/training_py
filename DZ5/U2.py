# Кonstantin Filippov 09.01.2021
# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.
def d5u2():
    file_name = "U1_texts.txt"
    file_mode = 'r'

    f_obj = open(file_name, file_mode)
    content = f_obj.read()
    print("Количество строк в файле:", content.count('\n')+1)

    f_obj.close()

d5u2()