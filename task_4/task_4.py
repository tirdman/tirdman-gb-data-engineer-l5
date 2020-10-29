"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

from functools import reduce

with open('file1.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

emp_salary = [{'family': next_info.split()[0], 'salary': float(next_info.split()[1])} for next_info in content]

print(list(map(lambda next_emp: next_emp['family'], filter(lambda next_emp: next_emp['salary'] < 20000, emp_salary))))

print(reduce(lambda emp1, emp2: emp1 + emp2['salary'], emp_salary, 0) / len(emp_salary))
