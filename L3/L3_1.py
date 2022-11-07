name = input('Привет, как тебя завут? ')
print(str(name)+', я хочу сыграть с тобой в игру.')
x = int(input('мне нужно от тебя 2 числа. Ты готов? (1 - Да, 0 - нет)\n'))
if x ==  1:
    a = float(input('a:'))
    b = float(input('b:'))
    print("cумма: " + str(a + b))
    print('разность: ' + str(a - b))
    print('Произведение: ' + str(a * b))
    print('целочисленное деление: ' + str(a // b))
    print('Деление по модулю: ' + str(a % b))
    print('возведение числа а в степень b: ' + str(a ** b))

else:
    print('нуу и ладно.')
