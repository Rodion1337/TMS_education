"""5*. Реализуйте генератор, который будет бесконечно 
генерировать числа Фибоначчи (https://en.wikipedia.org/wiki/Fibonacci_number).
Пример:
>>> gen = endless_fib_generator()
>>> while True:
	print(next(gen))
>>> 1 1 2 3 5 8 13 ...
"""
fib1, fib2 = 0, 1
while True:

	# for i in range(2,):
	fib1, fib2 = fib2, fib1 + fib2
	print(fib2, end=' ')
	# if fib2 >= 100:
	# 	break 