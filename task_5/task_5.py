"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random
from functools import reduce

with open('file1.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join([str(random.randint(0, 1000)) for i in range(50)]))

with open('file1.txt', 'r', encoding='utf-8') as f:
    print(reduce(lambda prev_num, next_num: prev_num + next_num, map(lambda n: int(n), f.readline().split())))
