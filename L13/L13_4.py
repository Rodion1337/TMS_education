"""4*. Реализуйте класс итератора EvenRange, который принимает начало и конец интервала 
в качестве аргументов инициализации и выдает только четные числа во время итерации.
Если пользователь попытается выполнить итерацию после того, как он выдал все возможные 
числа следует вывести «Out of number!».

_Примечание: вообще не используйте функцию range()_
Пример:
>>> er1 = EvenRange(7,11)
next(er1)
>>> 8
next(er1)
>>> 10
next(er1)
>>> "Out of numbers!"
next(er1)
>>> "Out of numbers!"
>>> er2 = EvenRange(3, 14)
>>> for number in er2:
    print(number)
>>> 4 6 8 10 12 "Out of numbers!"
"""

class EvenRange():
    def __init__(self, iter_start: int, iter_finish: int) -> int:
        self.iter_start = iter_start
        self.iter_finish = iter_finish
        self.index = 0

    def __next__(self):
        if self.iter_start < self.iter_finish:
            if self.iter_start % 2 == 0:
                self.iter_start += 2
            else:
                self.iter_start += 1
            return self.iter_start
        else:
            print ("Out of numbers!")
            raise StopIteration

    def __iter__(self):
        return self




er1 = EvenRange(7,11)
next(er1)
next(er1)
next(er1)

er2 = EvenRange(3, 14)
for number in er2:
    print(number)

x = EvenRange(3,14)
print(list(x))