"""2. Используя ORM peewee (https://pypi.org/project/peewee/) создайте функцию которая 
получает от пользователя название альбома через input и выводит список всех треков в этом альбоме"""

from peewee import *

bd = SqliteDatabase(r'chinook.db')
cursor=bd.cursor()
cursor.execute("SELECT albums.Title, sum(tracks.UnitPrice) FROM albums JOIN tracks on albums.AlbumId = tracks.AlbumId GROUP by albums.Title")
result = cursor.fetchall()
bd.close()
print(result)

# class BaseModel(Model): 
# 	class Meta: 
# 		database = bd