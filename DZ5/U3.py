# Кonstantin Filippov 09.01.2021
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 200 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Пример файла:
# Ivanov,100
# Petrov,200
# Sidorov,900

def d5u3():

    file_name = "salaries.txt"
    file_mode = 'r'
    empty_list = ['']
    col_names   = 0
    col_salaries = 1
    salary_norm = 200

    f_obj = open(file_name, file_mode)

    content = f_obj.readlines()

    list = []
    for el in content:
        value = (el.replace("\n",'')).split(',')
        if value != empty_list:
            list.append(value)

    print(list)

    sum = 0
    cnt = 0

    print("\nФамилии сотрудников с зп меньше 200:")
    print("-----------------")
    for n in list:
        salary = int(n[col_salaries])
        if salary < salary_norm:
            print(n[col_names])
        sum += salary
        cnt += 1


    print("-----------------")
    print("ФОТ             : ", sum)
    print("Сотрудников     : ", cnt)
    print("Средняя зарплата: ", sum/cnt)

    f_obj.close()


d5u3()

