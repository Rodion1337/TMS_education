# match_input = input ('Введите формулу, следущеюго вида "2 + 2", "22 / 11"')

match_input = ('1 2 1')
a = match_input.split(' ')

try:
    if a[1] in ('+', '-', '/', '*'):
        print(a[1])
        if a[1] == '+':
            print (int(a[0]) + int(a[2]))
        elif a[1] == '-':
            print (int(a[0]) - int(a[2]))
        elif a[1] == '/':
            print (int(a[0]) / int(a[2]))
        elif a[1] == '*':
            print (int(a[0]) * int(a[2]))
        else:
            print ('InputFormulaErrorQ')
except IndexError:
    print ('InputFormulaErrorQ')


    # if a[1] in ('+', '-', '/', '*'):
    #     print(a[1])
    # if a[1] == '+':
    #     print (int(a[0]) + int(a[2]))
    # elif a[1] == '-':
    #     print (int(a[0]) - int(a[2]))
    # elif a[1] == '/':
    #     print (int(a[0]) / int(a[2]))
    # elif a[1] == '*':
    #     print (int(a[0]) * int(a[2]))
    # else:
    #         print ('InputFormulaErrorQ')