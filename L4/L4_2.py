weight = int(input('Введите свой вес (в килограммах): '))
growth = int(input('Введите свой рост (в санитемрах): ')) / 100
index = round(weight / growth ** 2, 2)
print ('Индекс массы тела: ' + str(index))

if index <= 16:
    print('Выраженный дефицит массы тела')
elif index <= 18.5:
    print('Недостаточная (дефицит) масса тела')
elif index <= 25:
    print('норма')
elif index <= 30:
    print('Избыточная масса тела (предожирение)')
else:
    print('Тренажерный зал и диета - лучшие друзья!')