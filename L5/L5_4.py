import random
x = random.randint(99, 100)
q = ''
print('Привет, я загодал число от 1 до 100.\nПредлагаю угодаеть его.\nЧтобы сдаться введи: stop')
while True:
    q = int(input('введите свой ответ: '))
    if q == x:
        print('Вы угодали, верный ответ:', x)
        break
    elif q == 'stop':
        print('Жаль, что вы сдались. Ответ:', x)
        break
    else:
        print('Попытка хорошая, но не удачная. \nВ следующий раз, точно повезёт.')