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
    """
    Создание блюд
    """
    name : str
    price : int
    weight : int

dish_1 = Dish('Цезарь', 15, 150)
dish_2 = Dish('Пюре', 5, 100)
dish_3 = Dish('Котлета', 8, 70)
dish_4 = Dish('Картофель фри', 5, 100)



class Order():
    
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def to_pay(*args): #подсчет суммы к оплате
        to_pay_order = 0
        for i in args:
            to_pay_order = to_pay_order + i.price
        return to_pay_order

summ_to_pay = Order.to_pay(dish_1, dish_2)
print(summ_to_pay)

class client():
    def __init__(self, name):
        self.name = name