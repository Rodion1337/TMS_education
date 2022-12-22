"""2. Используя ORM peewee (https://pypi.org/project/peewee/) создайте функцию которая 
получает от пользователя название альбома через input и выводит список всех треков в этом альбоме"""

from peewee import *


class Input_album():
    
    
    def __init__(self, album: str, data_base: str) -> None:
        self.album = album
        self.data_base = data_base

    open_bd = SqliteDatabase(r'{self.data_base}')


    # class Meta:
    #     Database = self.data_base

album = Input_album('123', 'chinook.db')
print(album.open_bd)