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
    name_exit = []
    # from os import getcwd, chdir
    # path_folder = getcwd()
    # if url_folder.split('\\')[0] == path_folder.split('\\')[-1]:
    #     url_folder = str(url_folder.split('\\')[1])
    # else:
    #     url_folder = 'L13\\' + url_folder
    files_names = open(fr'{url_folder}', 'r')
    list_names = files_names.readlines()
    files_names.close
    name_exit = [a for a in list_names if a.startswith(letter_gen.upper())]
    return name_exit


x = names_gen(r'L13\unsorted_names.txt','A')
print(x)