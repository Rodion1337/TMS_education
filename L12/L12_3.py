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

class InvalidIntDivision(Exception):
    pass

class InvalidIntNumberCount(Exception):
    pass

class InvalidFloat(Exception):
    pass

class InvalidFloatNumber(Exception):
    pass

class InvalidStr(Exception):
    pass

class Queue():
    from typing import Any