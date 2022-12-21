"""1) Сколько всего байт «занимают» песни из таблицы tracks"""
SELECT Composer, sum(bytes) as "Размер" FROM tracks group by Composer;


"""2) Сколько записей находится в таблицах employees и customers"""
SELECT sum(count_for_sum) FROM (SELECT count(*) as count_for_sum from employees UNION SELECT count(*) as count_for_sum from customers)


"""3) Получить список треков tracks из альбома «A-Sides»"""
SELECT count(name) as 'A-Sides' FROM tracks where AlbumId = (SELECT AlbumId FROM albums WHERE Title = 'A-Sides');


"""4) Используя группировку (https://www.w3schools.com/sql/sql_groupby.asp) определите общую стоимость треков в каждом альбоме"""
SELECT albums.Title, sum(tracks.UnitPrice) FROM albums JOIN tracks on albums.AlbumId = tracks.AlbumId GROUP by albums.Title