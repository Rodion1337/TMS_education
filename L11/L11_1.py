"""
1. Реализуйте класс Блюдо, описывающее количество, название, стоимость и массу блюда.
Далее создайте несколько инстансов этого класса с описанием блюд.
Реализуйте класс Заказ, в инстанс которого можно было бы добавлять блюда. 
Заказ должен содержать вычисляемые свойства: количество, стоимость, масса блюд в заказе.
Также реализуйте дополнительный метод "оплатить" (внесение определенной суммы в счет оплаты заказа) и дополнительное свойство, 
обозначающее сумму, которую осталось оплатить (с учетом стоимости заказа и внесенных с помощью метода «оплатить» денег)
"""

class Dish():
    def __init__(self, name : str, price : int, weight : int):
        self.name = name
        self.price = price
        self.weight = weight

dish_1 = Dish('Цезарь', 15, 150)
# dish_2 = Dish('Пюре', 5, 100)
# dish_3 = Dish('Котлета', 8, 70)
# dish_4 = Dish('Картофель фри', 5, 100)
print(type(dish_1))

class Order():
    dish_order = []
    # def __init__(self, dish_order):
    #     self.dish_order = dish_order

    def order_list(self):
        dish_order.append(dict(dish_order))
        return dish_order
        
order_1 = Order.order_list(dish_1)

print(order_1)