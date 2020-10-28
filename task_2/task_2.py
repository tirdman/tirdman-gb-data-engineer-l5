"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('file1.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
    count_words = 0
    for index, next_str in enumerate(content):
        next_count_words = len(next_str.split(" "))
        count_words += next_count_words
        print(f'Строка: {index + 1}. Количество слов: {next_count_words}')
    print('---')
    print(f'Всего строк: {len(content)}. Всего слов: {count_words}')
