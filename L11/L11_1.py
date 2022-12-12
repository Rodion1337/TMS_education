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


class Order():
    def __init__(self, name_dish, price, weight):
        self.name_dish = name_dish
        self.price = price
        self.weight = weight

    def to_pay(x) -> int:
        """подсчет суммы к оплате"""
        to_pay_order = 0
        for i in x:
            to_pay_order = to_pay_order + i.price
        return to_pay_order

    def count_dish(x) -> int:
        """подсчет количества блюд"""
        count_dish_order = 0
        for i in x:
            count_dish_order = count_dish_order + 1
        return count_dish_order

    def balance(x) -> int:
        """подсчет остатка к оплате"""
        you_pay = input(f'Сумма вашего заказа {Order.to_pay(x)}. Прошу внести денежные средства: ')
        pay = Order.to_pay(x) - int(you_pay)
        return pay


my_order = (dish_1, dish_2)
print(f'Вы заказали всего {Order.count_dish(my_order)} блюд, сумма вашего заказа: {Order.to_pay(my_order)}')
print(f'Вы заказали: {my_order[0].name_dish} и {my_order[1].name_dish}')
print(f'Остаток к оплате: {Order.balance(my_order)}')
