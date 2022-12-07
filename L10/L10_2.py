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
import time

class Truck(Auto):
    max_load = 150

    def __init__(self, brand: str, age: int, mark: str,max_load:int):
        super().__init__(brand, age, mark)
        self.max_load = max_load
    
    def drive(self):
        print ('Attention!')
        return super().drive()

class Sedan(Auto):
    max_speed = 60
    
    def __init__(self, brand: str, age: int, mark: str, max_speed:int):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def drive(self):
        super().drive()
        print(f'max speed of sedan {self.brand} {self.mark} is {self.max_speed}')

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)


daf = Truck('DAF', 2013, 'af103', 150)
daf.drive()
daf.max_load = 90
print(daf.max_load)

ford = Sedan('Ford', 2021, 'Focus', 120)
ford.drive()
ford.load()
print('time out 1 sec')
