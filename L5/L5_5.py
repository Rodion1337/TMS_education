text = input('Введите строку для подсчета повторения символов: ').lower()
#text = 'Oh, it is Python'.lower() ## проверка работоспособности по образцу
c = ''.join(sorted(set(text)))
d = {a: text.count(a) for a in c}
print(d)