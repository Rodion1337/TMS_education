text = input('Введите строку: ')
text = text.capitalize().split(' ')
text1 = str(text[len(text)-1]).capitalize()
print(' '.join(text[0:-1]) + ' ' + text1)