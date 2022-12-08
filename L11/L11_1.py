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
    name_dish : str
    price : int
    weight : int

dish_1 = Dish('Цезарь', 15, 150)
dish_2 = Dish('Пюре', 5, 100)
dish_3 = Dish('Котлета', 8, 70)
dish_4 = Dish('Картофель фри', 5, 100)
menu = []
menu.append(dish_1)
menu.append(dish_2)
menu.append(dish_3)
menu.append(dish_4)
print(menu)


class Order():
    def __init__(self, name_dish, price, weight):
        self.name_dish = name_dish
        self.price = price
        self.weight = weight

    def to_pay(*args) -> int:
        """подсчет суммы к оплате"""
        to_pay_order = 0
        for i in args:
            to_pay_order = to_pay_order + i.price
        return to_pay_order

    def balance() -> int:
        you_pay = input(f'Сумма вашего заказа {Order.to_pay}')
        pay = Order.to_pay - you_pay

class Client():
    def __init__(self):
        self.name = input('добрый день.\nкак вас зовут?')

    def my_order():
        
        x = input(f'будете что-то заказывать? (Y / N)').upper()
        if x = 'Y':
            my_dish = input(f'на выбор есть Dish_1: {dish_1.name_dish}, ценна:{dish_1.price}, вес блюда {dish_1.weight}. Будете заказывать? (Y / N)')
                if my

start = Client()

