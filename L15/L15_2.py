"""2. Используя ORM peewee (https://pypi.org/project/peewee/) создайте функцию которая 
получает от пользователя название альбома через input и выводит список всех треков в этом альбоме"""

from peewee import *


def input_tracks():
    find_album = input('Введите название альбома, трека которго необходимо вывести: ')
    # find_album = "Jagged Little Pill"

    find_order = (f'SELECT tracks.Name FROM albums JOIN tracks on albums.AlbumId = tracks.AlbumId WHERE albums.Title = "{find_album}"')
    
    bd = SqliteDatabase(r'L15\chinook.db')
    cursor = bd.cursor()
    cursor.execute(find_order)
    return(cursor.fetchall())
    bd.close()
    



trecks = input_tracks()
print(trecks)

# class BaseModel(Model): 
# 	class Meta: 
# 		database = bd