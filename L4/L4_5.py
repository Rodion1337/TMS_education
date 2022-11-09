date = input ('Ввежите дату рождения в формате дд/мм/гггг: ')
date_now = input ('Ввежите текущую дату в формате дд/мм/гггг: ')
date = date.split('/')
date_now = date_now.split('/')
print(date, date_now)
print('вам ' + str(int(date_now[2]) - int(date[2])) + ' полных лет и ' +
    str((int(date_now[1]) - int(date[1])) * 30 + int(date_now[0]) - int(date[0]))  + ' дней')