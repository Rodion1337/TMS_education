def Temperature_Conversion():
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


"""можно сделать универсально через словарь и лямбды, например создаешь словарь как атрибут класса

converts = {
    "FC": lambda x: round((self.temp - 32)*(5/9), 2),
...
}
и в методе transfrom получать из этого словаря преобразование по ключу type_transform

def tranform(self, type_transf: str, temp: int):
    convert = converts.get(type_transf, None)
    if converts:
        return converts(temp)
    else:
        return 'Ошибка проверьте введенные значения'"""