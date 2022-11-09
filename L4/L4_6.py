text = input('Введите строку: ')
#text = 'Я ЛюбЛю ЛюДей'
text = text.capitalize().split(' ')
#text = text.split(' ')
text1 = str(text[len(text)-1]).capitalize()
#text1 = text1.capitalize()
print(' '.join(text[0:-1]) + ' ' + text1)