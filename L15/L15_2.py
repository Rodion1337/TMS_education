"""2. Используя ORM peewee (https://pypi.org/project/peewee/) создайте функцию которая 
получает от пользователя название альбома через input и выводит список всех треков в этом альбоме"""

from peewee import *

# find_album = input('Введите название альбома, трека которго необходимо вывести: ')

def input_tracks(find_album):
    # find_album = input('Введите название альбома, трека которго необходимо вывести: ')
    # find_album = "Jagged Little Pill"

    find_order = (f'SELECT tracks.Name FROM albums JOIN tracks on albums.AlbumId = tracks.AlbumId WHERE albums.Title = "{find_album}"')
    
    bd = SqliteDatabase(r'L15\chinook.db')
    with bd:
        cursor = bd.cursor()
        cursor.execute(find_order)
        return(cursor.fetchall())



print(input_tracks('A-Sides'))