"""3. Откройте файл «unsorted_names.txt» содержащий имена студентов.
Прочитайте данные, отсортируйте их и запишите в новый файл «sorted_names.txt» (каждое имя начинается с новой строки
_______
Aaron
Adrian
…..
Wiley
________
"""

names = open('unsorted_names.txt', 'r')          #открытие файла на чтение
name_list = sorted(names.readlines())            #построчное прочтение содержимого + сортировка

name_list_sorted = open('sorted_names.txt', 'w')
name_list_sorted.write(''.join(name_list))

