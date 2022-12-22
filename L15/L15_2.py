"""2. Используя ORM peewee (https://pypi.org/project/peewee/) создайте функцию которая 
получает от пользователя название альбома через input и выводит список всех треков в этом альбоме"""

from peewee import *


def input_tracks(alb):
    bd = SqliteDatabase(r'L15\chinook.db')
    cursor = bd.cursor()
    cursor.execute('SELECT tracks.Name FROM albums JOIN tracks on albums.AlbumId = tracks.AlbumId WHERE albums.Title = "{alb}"')
    # cursor.execute("SELECT Name FROM tracks")
    result = cursor.fetchall()
    print(result)
    bd.close()


input_tracks('Jagged Little Pill')

# class BaseModel(Model): 
# 	class Meta: 
# 		database = bd