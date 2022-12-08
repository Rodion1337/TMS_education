"""
1. Реализуйте класс Блюдо, описывающее количество, название, стоимость и массу блюда.
Далее создайте несколько инстансов этого класса с описанием блюд.
Реализуйте класс Заказ, в инстанс которого можно было бы добавлять блюда. 
Заказ должен содержать вычисляемые свойства: количество, стоимость, масса блюд в заказе.
Также реализуйте дополнительный метод "оплатить" (внесение определенной суммы в счет оплаты заказа) и дополнительное свойство, 
обозначающее сумму, которую осталось оплатить (с учетом стоимости заказа и внесенных с помощью метода «оплатить» денег)
"""

from dataclasses import dataclass


@dataclass
class Dish():
    name : str
    price : int
    weight : int

dish_1 = Dish('Цезарь', 15, 150)
dish_2 = Dish('Пюре', 5, 100)
dish_3 = Dish('Котлета', 8, 70)
dish_4 = Dish('Картофель фри', 5, 100)
print(dish_1)
print(dish_2)




class Order():
    x = []
    def __init__(self, dish_order):
        self.dish_order = dish_order

    def order_list(x):
        dish_order = []
        dish_order.append(dict(x))
        return dish_order

    def summ_order(self,*args):
        for i in args:
            x.append(i)
        print x

Order(dish_1, dish_2)

lol