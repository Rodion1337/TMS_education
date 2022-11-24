"""5. Открыть файл из п.4. Создать функцию ('transform_to_csv') которая будет выполнять следующее:
каждую запись в json файле функция будет преобразовывать в строку с данными в виде name,age,id (например, Tim,12,127492) и сохранять все данные в виде csv файла
Путь к json файлу и имя сохраняемого csv файла должно запрашиваться у пользователя
"""

import csv, json

with open('l8\\id_name_age_json.json', 'r') as file_json:
    file_json_on_form = json.load(file_json)
#    print(file_json_on_form)

def transform_to_csv(file_json_to_format):
    keys_id = file_json_to_format.keys()
    file_json_to_format_list = list(file_json_to_format)
    print(file_json_to_format_list)
    print(keys_id)
    data_to_csv = []
    i = 0
    for x in keys_id:
        data_to_csv[i].append()
#    print(str(list(id for id in keys_id)))
#    x = list(f'{(file_json_to_format[id]["name"])}, {(file_json_to_format[id]["age"])}, {id}' for id in keys_id)
#    print(x)
#    print(';'.join(x))
    with open('L8\\file_csv.csv', 'wt') as file_csv:
        csv_out = csv.writer(file_csv)
        csv_out.writerows(list(file_json_to_format))

transform_to_csv(file_json_on_form)