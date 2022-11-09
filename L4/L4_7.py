text = input ('Введите текст (строку): ')
x = input ('Введите произвольный символ: ')
n = input ('Введите число: ')
#text = 'я люблю людей'
#x = ':'
#n = '10'
c = ''
for q in range(1, len(text), 2):
    c += text[q : (q + 1)] + n
c += ' '
for q in range(0, len(text) - 1, 2):
    c += text[q : ( q + 1 )] + x
print(text + '\n' + c + '\n' + str('!' * int(n)))