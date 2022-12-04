"""
2. Создать 2 класса Truck и Sedan, которые являются наследниками Auto. 
Класс Truck имеет дополнительный обязательный атрибут max_load. 
Переопределить метод drive, который перед появление сообщения «Car <brand> <mark> drives» выводит сообщение «Attention!». 
Реализовать дополнительный метод load. При его вызове происходит пауза в 1 секунду (используя модуль time), затем выводится сообщение «load», 
а затем снова происходит пауза в 1 секунду. Класс Sedan имеет дополнительный метод обязательный атрибут max_speed и при вызове метода drive, 
после появления сообщения «Car <brand> <mark> drives», выводит сообщение «max speed of sedan <brand> <mark> is <max_speed>». 
Инициализировать по 2 отдельных объекта этих классов, проверить работы их методов и атрибутов (вызвать методы, атрибуты вывести в печать)
"""

from L10_1 import Auto

class Truck(Auto):
    max_load = 150

    def __init__(self, brand: str, age: int, mark: str,max_load:int):
        super().__init__(brand, age, mark)
        self.max_load = max_load
    
    def drive(self):
        print ('Attention!')
        return super().drive()

# class Sedan(Auto):
#     ....

daf = Truck('DAF', 2013, 'af103', 150)
daf.drive()