"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

lang_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

content = []
with open('file1.txt', 'r', encoding='utf-8') as f_1:
    content = f_1.readlines()


def replace_word(string, dict_words):
    return f"{' '.join(map(lambda a: dict_words[a] if a in dict_words else a, string.split()))}\n"


content2 = []
with open('file2.txt', 'w', encoding='utf-8') as f_2:
    content2 = map(lambda a: replace_word(a, lang_dict), content)
    f_2.writelines(content2)
