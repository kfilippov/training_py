# Кonstantin Filippov 09.01.2021
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

class FileWrapper(object):
    """
    Пример класса контектсного менеджера взят (и доработан) по ссылке:
    https://book.pythontips.com/en/latest/context_managers.html#implementing-a-context-manager-as-a-class
    """
    def __init__(self, file_name, method, encoding):
        self.file_obj = open(file_name, method, encoding=encoding)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exception_type, exception_val, exception_traceback):
        self.file_obj.close()

def d5u6():
    """
    Описание регулярного выражения: r'\d+'

    / r'\d+'/ gm

    r' matches the characters r' literally (case sensitive)
        \d+ matches a digit (equal to [0-9])
        + Quantifier — Matches between one and unlimited times, as many times as possible,
            giving back as needed (greedy)
        ' matches the character ' literally (case sensitive)

    Global pattern flags
        g modifier: global. All matches (don't return after first match)
        m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)

    Описание взято по ссылке:
    https://regex101.com/

    """
    import re

    regex = r'\d+'
    file = 'lessons.txt'
    read = 'r'
    write = 'w'
    space = " "
    encoding = "utf-8"

    col_lessons = 0
    col_hours   = 1

    res_dict = dict()

    with FileWrapper(file, read, encoding) as reader:
        for el in reader.readlines():
            split = el.split(":")
            key = split[col_lessons]
            value = 0
            for e in re.findall(regex, split[col_hours]):
                value += int(e)
            res_dict.update({key : value})

    print(res_dict)

d5u6()