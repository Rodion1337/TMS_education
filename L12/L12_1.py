x = ''
while x != 'yes':
    match_input = input ('Введите формулу, следующего вида "2 + 2", "22 / 11": ')
    # match_input = ('1 2 1')
    a = match_input.split(' ')
    try:
        if a[1] in ('+', '-', '/', '*', '**'):
            print (a[1])
            if a[1] == '+':
                print (float(a[0]) + float(a[2]))
            elif a[1] == '-':
                print (float(a[0]) - float(a[2]))
            elif a[1] == '/':
                print (round(float(a[0]) / float(a[2]), 2))
            elif a[1] == '*':
                print (float(a[0]) * float(a[2]))
            elif a[1] == '**':
                print (float(a[0]) ** float(a[2]))
            else:
                print ('InputFormulaErrorQ')
        else:
            print ('InputFormulaErrorQ')
    except IndexError:
        print ('InputFormulaErrorQ')
    x = input('завершить вычисления? (yes / no)\n').lower()

