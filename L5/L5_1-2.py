while True:
    name = input('Добрый день. Как вас зовут? ')
    year = input('Ваш возвраст? ')
    if int(year) >= 18:
        print(name, ', рады вас видеть в нашем заведении.')
    else:
        print(name, ', к сожалению вам нельзя пройти.')