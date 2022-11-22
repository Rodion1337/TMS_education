#name = input('введите ваше имя: ')
#color = input(f'{name}, какой цвет твой любимый? ')
#city = input(f'{name}, из какого ты города? ')
#bar = input(f'{name}, как называется лучший бар в {city}? ')

name = ('Radik1337Blr')
color = ('Green')
city = ('Minsk')
bar = ('na dne')

with open('files_8_2.txt', 'w') as file:
    data = [name, color]
    for line in data:
        file.write(line + "|\n")

with open('files_8_2.txt', 'a') as file:
    data = [city, bar]
    for line in data:
        file.write(line.upper() + "|\n")