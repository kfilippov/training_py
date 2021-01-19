# Кonstantin Filippov 09.01.2021
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def d5u4():
    file_name_source = "123.txt"
    file_mode_source = 'r'

    file_name_target = "123_ru.txt"
    file_mode_target = 'w'

    empty_list = ['']
    col_text     = 0
    col_numbers  = 1
    dict = {  1:"Один"
            , 2:"Два"
            , 3:"Три"
            , 4:"Четыре"
            , 5:"Пять"
            }

    f_obj_source = open(file_name_source, file_mode_source)

    content = f_obj_source.readlines()
    print("Считан: %s" % content)

    list = []
    for el in content:
        value = (el.replace("\n",'')).replace(' ', '').split('-')
        if value != empty_list:
            value[col_text] = dict.get(int(value[col_numbers]))
            value = ' - '.join(value)
            list.append(value)



    with open(file_name_target, file_mode_target) as f_obj_target:
        for el in list:
            f_obj_target.write("%s\n" % el)

    print("Записан: %s" % list)

    f_obj_source.close()
    f_obj_target.close()

d5u4()