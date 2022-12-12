"""3*) Создайте класс, который имеет атрибут queue (допускается использование списка) 
который имеет метод add позволяющий добавлять в queue следующие объекты — целые числа, 
числа с плавающей запятой, строки. При этом в момент добавления происходит валидация элементов по следующим правилам:

1. Целые числа — должны делится на 8, состоять из не более чем 4 символов
2. Числа с запятой — не более 3 символов после запятой
3. Строки — длина не более 4 символов без дублирования символов

В результате работы метода add элементы прошедшие валидацию добавляются в queuе, элементы 
не прошедшие валидацию  выводятся пользователю с сообщением о причине недобавления, например 
q=Queue()
q.add(1, 16, 280, 80000, 2.51, 1.875, text, data, world)
InvalidIntDivision → 1 # не делится на 8
InvalidIntNumberCount → 80000 # больше 4 символов
InvalidFloat → 1.875 # больше 2 символов после запятой
InvalidTextLength → world # больше 4 символов
DuplicatesInText → data # повторяющиеся символы
q.queue
# [16,280,text]
"""

class InvalidInt(Exception):
    pass

class InvalidFloat(Exception):
    pass

class InvalidStr(Exception):
    pass


class Queue():
    queue = []

    def add(self, *agrs):
        for i in agrs:
            try:
                if isinstance(i, int):
                    if i % 8 == 0 and len(str(i)) <= 4:
                        self.queue.append(i)
                    else:
                        raise InvalidInt
                elif isinstance(i, float):
                    if round(i, 2) == i:
                        self.queue.append(i)
                    else:
                        raise InvalidFloat
                elif isinstance(i, str):
                    a = 0
                    for c in i:
                        if i.count(c) > 1:
                            a = i.count(c) 
                    if len(i) <= 4 and a < 2:
                        self.queue.append(i)
                    else:
                        raise InvalidStr
            except InvalidInt:
                print(f'{i} - не делится на 8 или больше 4 символов')
            except InvalidFloat:
                print(f'{i} - больше 2 символов после запятой')
            except InvalidStr:
                print(f'{i} - содержит 2 повторяющихся знака или длиннее 4 знаков')
        print(f'{self.queue}')


q = Queue()
q.add(1, 16, 280, 80000, 2.51, 1.875, 'text', 'data', 'world', 'qwertyy', 'kent')