import random
x = random.randrange(1, 101)
q = ''
print('Привет, я загодал число от 1 до 100.\nПредлагаю угодаеть его.\nЧтобы сдаться введи: stop')
while True:
    q = input('введите свой ответ: ')
    if q == x:
        print('Вы угодалите, верный ответ:', x)
        break
    elif q == 'stop':
        print('Жаль, что вы сдались. Ответ:', x)
        break
    else:
        print('Попытка хорошая, но не удачная.')