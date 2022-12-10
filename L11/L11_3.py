"""3. Реализуйте класс DataObject который имеет обязательный атрибут data (произвольного типа данных)
Реализуйте класс очередь (Deque) с атрибутом класса deque в котором будут хранится элементы добавляемые в очередь, 
Класс Deque имеет методы 
- append_left для добавления элемента в начало очереди deque
- append_right для добавления элемента в конец очереди deque
(в данных методах необходимо реализовать возможность добавления в очередь только экземпляров класса DataObject (и его дочерних),
а также проверку длины очереди — одновременно там может находится не более 5 элементов — в случае добавления 6 элемента добавление 
не производится и пользователю выдается сообщение о переполнении очереди). 
- pop_left — удаляет из очереди первый элемент слева и возвращает его
- pop_right - удаляет из очереди первый элемент справа и возвращает его
При реализации методов класса Deque воспользуйтесь методами класса (classmethod)
"""

from dataclasses import dataclass
from typing import Any

@dataclass
class DataObject:
    data : Any


class Deque:
    deque_list = []

    @classmethod
    def append_left(self, data):
        return self.deque_list.insert(0, data) if len(self.deque_list) < 5 else ('очередь переполнена')


    @classmethod
    def append_right(self, data):
        return self.deque_list.append(data) if len(self.deque_list) < 5 else ('очередь переполнена')


    @classmethod
    def pop_left():
        pass

    @classmethod
    def pop_right():
        pass

"""тестовая часть"""
data_1 = DataObject(69)
data_2 = DataObject("abc")
data_3 = DataObject("abcasd")
data_4 = DataObject("qwerty")
data_5 = DataObject('zxcvb123')
data_6 = DataObject(1231245235)

print(f'data 1: {data_1}, data_2: {data_2}, data_3: {data_3}, data_4: {data_4}, data 5: {data_5}, data_6: {data_6}')

result = Deque
result.append_right(data_1)
print(result.deque_list)
result.append_left(data_2)
print(result.deque_list)
result.append_right(data_3)
print(result.deque_list)
result.append_left(data_4)
print(result.deque_list)
result.append_left(data_5)
print(result.deque_list)
result.append_left(data_6)
print(result.deque_list)
#L11_3 update