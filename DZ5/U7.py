# Кonstantin Filippov 09.01.2021
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


from contextlib import contextmanager
import json

@contextmanager
def open_file(name, mode):
    """
        Пример контектсного менеджера как генератор
        https://book.pythontips.com/en/latest/context_managers.html#implementing-a-context-manager-as-a-generator
    """
    f = open(name, mode)
    try:
        yield f
    except Exception as err:
        print("Ошибка:",err)
    finally:
        f.close()

def d5u7():

    Local_Printer = True
    out_file = 'out_companies.txt'
    file  = 'companies.txt'
    read  = 'r'
    write = 'w'
    space = " "
    regex = r'\d+'  # числа (детали в D5/U6.py)
    profit_txt = "average_profit"


    with open_file(file, write) as f:
        """
        Генерируем тестовый файл:
        название, форма собственности, выручка, издержки
        разделитьель пробел
        """
        f.write('Копыто ООО 3000000 10000\n')
        f.write('Pukka OY 40000 45000\n')
        f.write('DamnBrothers LLC 110000 30000\n')
        f.write('Kawai KK 13000 8000')

    col_firm     = 0
    col_org_form = 0
    col_revenue  = 2
    col_costs    = 3

    total_profit = 0
    firms_number = 0

    profit_dict = dict()
    firms_dict  = dict()
    result_list = list([])

    with open_file(file, read) as f:
        for el in f.readlines():
            split = el.split(space)

            curr_cost = int(split[col_costs])
            curr_revn = int(split[col_revenue])
            curr_profit = curr_revn - curr_cost

            firms_dict.update({split[col_firm] : curr_profit})

            if curr_cost < curr_revn:
                firms_number += 1
                total_profit += curr_profit
            if Local_Printer:
                print(split)

    avg_profit = total_profit / firms_number

    profit_dict.update({profit_txt : avg_profit})

    result_list.append(firms_dict)
    result_list.append(profit_dict)

    if Local_Printer:
        print("----------------------------")
        print("Общая прибыль..:",total_profit)
        print("Компаний учтено:",firms_number)
        print("Средняя прибыль:",avg_profit)
        print("----------------------------")
        print(result_list)

    with open_file(out_file, write) as f_result:
        json.dump(result_list, f_result)

d5u7()