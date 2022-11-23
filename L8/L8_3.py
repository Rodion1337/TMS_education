"""3. Откройте файл «unsorted_names.txt» содержащий имена студентов.
Прочитайте данные, отсортируйте их и запишите в новый файл «sorted_names.txt» (каждое имя начинается с новой строки
_______
Aaron
Adrian
…..
Wiley
________
"""

names = open(r'l8\unsorted_names.txt', 'r')          #открытие файла на чтение
name_list = sorted(names.readlines())            #построчное прочтение содержимого + сортировка
names.close()

name_list_sorted = open(r'l8\sorted_names.txt', 'w', encoding="utf-8") #создание файла для записи данных
name_list_sorted.write(''.join(name_list))       #запись данных
name_list_sorted.close()
