"""2. Реализуйте свой пользовательский класс итератора с именем MySquareIterator, 
который дает квадраты элементов коллекции, по которой он итерируется.
Пример:
>>> lst = [1, 2, 3, 4, 5]
>>> itr = MySquareIterator(lst)
>>> for el in itr:
	print(el)
	print(el)
>>> 1 4 9 16 25

"""

class MySquareIterator():
	def __init__(self, iter_list: list) -> int | list:
		self.iter_list = iter_list
		self.index = 0

	def __next__(self):
		try:
			res = self.iter_list[self.index]
		except IndexError:
			raise StopIteration
		else:
			self.index += 1
			return res ** 2

	def __iter__(self):
		return self


lst = [1, 2, 3, 4, 5]

itr = MySquareIterator(lst)

for el in itr:
	print(el)

lst_2 = [1, 2, 3, 4, 5]

itr_2 = MySquareIterator(lst_2)
print([a for a in itr_2])