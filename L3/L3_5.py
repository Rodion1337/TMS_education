a = input('Введите слово №1: ')
b = input('Введите слово №2: ')
print(a + b)
print(''.join(list(reversed(list(a[1:-1])))) + ''.join(list(reversed(list(b[1:-1])))))
a1 = a[1:-1]
b1 = b[1:-1]
print(a1[::-1] + b1[::-1])