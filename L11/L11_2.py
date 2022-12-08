"""
2. Реализуйте класс который представляет собой универсальный интерфейс по представлению температуры в шкалах 
Цельсия/Кельвина/Фаренгейта и поддерживает конвертацию значений температуры между этими шкалами 
(https://www.cuemath.com/temperature-conversion-formulas/)
"""

class Temperature_Conversion():
    def __init__(self, type_transf: str, temp: int) -> int:
        self.type_transf = type_transf
        self.temp = temp
    def tranform(self, type_transf: str, temp: int):
        # input
        if self.type_transf in ('CF','CK','FC','FK','KF','KC'):
            if self.type_transf == 'FC':
                return round((self.temp - 32)*(5/9), 2)
            elif self.type_transf == 'KC':
                return round(self.temp - 273.15, 2)
            elif self.type_transf == 'CK':
                return round(self.temp + 273.15, 2)
            elif self.type_transf == 'FK':
                return round((self.temp - 32)*(5/9) + 273.15, 2)
            elif self.type_transf == 'CF':
                return round((self.temp * (9/5)+ 32), 2)
            elif self.type_transf == 'KF':
                return round((273.15 - self.temp)*9/5 - 32, 2)
            else:
                return 'Ошибка проверьте введенные значения'

type_transf = input('Введите тип преобразования, по типу цельсий в фаренгейт: CF и т.п.')
temp_transf = float(input('Введите преобразуемое значение: '))

trans = Temperature_Conversion(type_transf, temp_transf)
print(trans.tranform(type_transf, temp_transf))