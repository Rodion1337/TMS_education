"""
1. Создайте генераторную функцию которая в качестве аргумента принимать путь к файлу «unsorted_names.txt» и 
букву английского алфавита, открывает файл по данному пути и генерирует последовательность из имен начинающихся на указанную букву
>>> names_with_letter = names_gen(«unsorted_names.txt», «A»)
>>> next(names_with_letter)
Amelia
>>> next(names_with_letter)
Adrienne
или
>>> for name in names_with_letter:
	print(i, end=““)
Amelia
Adrienne
"""
def names_gen(url_folder: str, letter_gen: str):
    files_names = open(fr'{url_folder}', 'r')
    list_names = sorted(list_names.readlines())
    files_names.close
    print(list_names)

names_gen('L13\unsorted_names.txt','A')