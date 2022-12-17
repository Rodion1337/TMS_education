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
    def append_left(self, data: Any):
        """Добавление элемента в начало списка"""
        if isinstance(data, DataObject):
            self.deque_list.insert(0, data.data) if len(self.deque_list) < 5 else print('Очередь переполнена')
            return None
        else:
            return(f'Переданный: {data}, не является наследником DataObject')

    @classmethod
    def append_right(self, data: Any):
        """Добавление элемента в конец списка"""
        if isinstance(data, DataObject):
            self.deque_list.append(data.data) if len(self.deque_list) < 5 else print('Очередь переполнена')
            return None
        else:
            return(f'Переданный: {data}, не является наследником DataObject')

    @classmethod
    def pop_left(self):
        """Удаление элемента в начале списка"""
        return self.deque_list.pop(0)

    @classmethod
    def pop_right(self):
        """Удаление элемента в конце списка"""
        return self.deque_list.pop(-1)




"""тестовая часть"""
data_1 = DataObject(1)
data_2 = DataObject("2")
data_3 = DataObject("3")
data_4 = DataObject("4")
data_5 = DataObject('5')
data_6 = DataObject(6)


result = Deque
print(result.append_right(data_1))
print(result.append_left(data_2))
print(result.append_right(data_3))
print(result.append_left(data_4))
print(result.append_left(data_5))
print(result.append_left(data_6))
print(result.pop_left())
print(result.pop_left())
print(result.pop_left())
print(f'принт элемента №2 {Deque.deque_list[1]}')
print(result.append_left("test approved"))
print(Deque.deque_list)
#L11_3 update