"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('file1.txt', 'w', encoding='utf=8') as f:
    print('Введите строки. Для выхода строка должны быть пустая')
    while True:
        next_str = input('Следующая строка: ')
        if not next_str:
            break
        f.write(f'{next_str}\n')
