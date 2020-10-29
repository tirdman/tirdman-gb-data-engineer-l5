"""
6)	Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re


def get_num_from_string(string):
    num_list = re.findall("\d+", string)
    if len(num_list) > 0:
        return int(num_list[0])
    return 0


with open('file1.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

subjects = {
    next_info.split()[0][:-1]:
        get_num_from_string(next_info.split()[1]) +
        get_num_from_string(next_info.split()[2]) +
        get_num_from_string(next_info.split()[3])
    for next_info in content
}

print(subjects)
