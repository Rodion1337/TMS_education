def double_factorial(x):
    s = 1
    if x % 2 == 0:
        for i in range(2, x + 1 ,2):
            s *= i 
    else:
        for i in range(1, x + 1 ,2):
            s *= i 
    return(s)


print(double_factorial(10))
print(double_factorial(11))