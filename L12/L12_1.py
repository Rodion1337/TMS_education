x = ''

class InputFormulaError(Exception):
    pass
class InputNumberError(Exception):
    pass
class InputOperatorError(Exception):
    pass


while x != 'yes':
    match_input = input ('Введите формулу, следующего вида "2 + 2", "22 / 11": ')
    # match_input = ('1 Ё 3')
    a = match_input.split(' ')
    if len(a) != 3:
        raise InputFormulaError('В формуле больше знаков чем должно быть!')
    try:
        a[0] = float(a[0]) 
        a[2] = float(a[2])
    except ValueError:
        raise InputNumberError('Проверьте введённые значения. Возможно это буквы!')
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
        raise InputOperatorError('Не известный оператор!')
    
    x = input('завершить вычисления? (yes / no)\n').lower()

