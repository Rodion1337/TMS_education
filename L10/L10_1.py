"""
1. Создать родительский класс Auto, у которого есть атрибуты: brand, age, color, mark и weight. 
В классе должны быть реализованы следующие методы — drive, use и stop. 
Методы drive и stop выводят сообщение «Car <brand> <mark> drives / stops». 
Метод use увеличивает атрибут age на 1 год. Атрибуты brand, age и mark необходимо инициализировать при объявлении объекта
"""

class Auto():
    color = 'green'
    weight = 2100

    def __init__(self, brand:str, age:int, mark:str):
        self.brand = brand
        self.age = age
        self.mark = mark
    
    def use(self):
        self.age += 1
    
    def drive(self):
        print(f"Car {self.brand} {self.mark} drives")
    
    def stop(self):
        print(f"Car {self.brand} {self.mark} stops")


# bmw = Auto('BMW', 2010, 'E46')
# print(bmw.brand, bmw.mark, bmw.age, bmw.color, bmw.weight)
# bmw.use()
# bmw.drive()
# bmw.stop()
# print(bmw.age)

# audi = Auto('Audi', 2019, 'Q7')
# print(audi.brand, audi.mark, audi.age, audi.color, audi.weight)