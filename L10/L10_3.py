"""
3. Реализуйте класс Counter, который дополнительно принимает начальное значение и конечное значение счетчика. 
Если начальное значение не указано, счетчик должен начинаться с 0. Если стоп-значение не указано, оно должно 
считаться вверх бесконечно. Если счетчик достигает стоп-значения, выведите «Maximal value is reached».
Реализовать методы: "increment" (увеличивает счетчик на 1) и "get" (выводит информацию о значении счетчика)
"""



class Counter():
    def __init__(self, start:int = 0, stop:int=float ( "inf" )):
        self.start = start
        self.stop = stop

    def increment(self):
        self.start += 1
        if self.start >= self.stop:
            self.start = self.stop
            return print("Maximal value is reached")
<<<<<<< HEAD

=======
        # return(self.start = elf.start + 1 if self.start != self.stop else print("Maximal value is reached"))
    
>>>>>>> parent of bb06b8c (increment update 2)
    def get(self):
        print(self.start)


c = Counter(start=42)
c.increment()
c.get()
c.increment()
c.get()

c = Counter(start=42,stop=44)
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()
c.increment()
c.get()