"""2. Реализуйте свой пользовательский класс итератора с именем MySquareIterator, 
который дает квадраты элементов коллекции, по которой он итерируется.
Пример:
>>> lst = [1, 2, 3, 4, 5]
>>> itr = MySquareIterator(lst)
>>> for el in itr:
	print(el)
>>> 1 4 9 16 25

"""
class MySquareIterator():
	def __init__(self, list_Iterator: list) -> int:
		self.list_Iterator = list_Iterator
	
	def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

	# def __iter__(self):
	# 	return self
	
	# def __next__(self.list_Iterator):
	# 	return self.list_Iterator ** 2

print([x **2 for x in [1, 2, 3, 4, 5]]) #классический вариант, но как реализовать автоматический запуск не понятно



lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
print(itr)
