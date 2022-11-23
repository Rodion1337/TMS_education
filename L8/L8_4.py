"""4. Имеется строка, содержащая имена через запятую «Tim,John,Sally,Trevor,Harry» и соответствующий именам кортеж содержащий возраст (12,34,24,57,18)
Создать новый словарь, который будет иметь следующую структуру
Ключ — сгенерированое шестизначное число, значения — словарь который состоит из 2 ключей «name» и «age» с соответствующими значениями из строки с именами и кортежа с возрастами, например
{
	'127492': {
			'name': 'Tim',
			'age': 12
		},
	'538956': {
		…..
}
Сохранить итоговый словарь в виде json файла
"""
names = 'Tim,John,Sally,Trevor,Harry'.split(',')
ages = '12,34,24,57,18'.split(',')
name_age_list = list((name, age) for name,age in zip(names,ages))
#print(name_age_list)
import json
name_age_dict_id = {(100000 + id) : {'name':name_age_list[id][0], 'age':int(name_age_list[id][1]) } for id in range(len(name_age_list))}
#print(name_age_dict_id)
name_age_json = json.dumps(name_age_dict_id, indent=4)
#print(name_age_json)
file = open('l8\\id_name_age_json.json', 'w')
file.write(name_age_json)
file.close()