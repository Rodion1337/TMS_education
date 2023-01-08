class Temperature_Conversion():
    """
    RUS:
    Данная функция создана с целью облегчения перевода одних единиц измерения температуры в другие.
    Работает с Celsius, Kelvin, Fahrenheit. Тип преобразование температуры выбирается на основание заглавных букв <из><в>: Celsius to Fahrenheit = CF
    Ввод типа преобразования температуры вводиться только латинскими буквами.
    Вводимая температура  для преобразования допускается не целое числи, выводиться температуру с округлением до 2 заков после запятой

    ENG:
    This function was created to facilitate the conversion of one temperature unit to another.
    Works with Celsius, Kelvin, Fahrenheit. The temperature conversion type is selected based on capital letters <from><to>: Celsius to Fahrenheit = CF
    Entering the type of temperature conversion should be entered only in Latin letters.
    The input temperature for conversion is allowed not an integer, the output temperature is rounded up to 2 decimal points

    Celsius to Kelvin: K = C + 273.15 -> CK
    Kelvin to Celsius: C = K - 273.15 -> KC
    Fahrenheit to Celsius: C = (F-32) (5/9) -> FC
    Celsius to Fahrenheit: F = C(9/5) + 32 -> CF
    Fahrenheit to Kelvin: K = (F-32) (5/9) + 273.15 -> FK
    Kelvin to Fahrenheit: F = (K-273.15) (9/5) + 32 -> KF
    """
    def __init__(self):
        self.converts = {
            "FC": lambda x: round((self.temp - 32) * (5 / 9), 2),
            "KC": lambda x: round(self.temp - 273.15, 2),
            "CK": lambda x: round(self.temp + 273.15, 2),
            "FK": lambda x: round((self.temp - 32) * (5 / 9) + 273.15, 2),
            "CF": lambda x: round((self.temp * (9 / 5) + 32), 2),
            "KF": lambda x: round((self.temp - 273.15) * (9 / 5) + 32, 2)
            }

    def tranform(self, type_transf: str, temp: int) -> int:
        convert = self.converts.get(type_transf.upper(), None)
        if convert:
            return convert(temp)
        else:
            return 'Ошибка проверьте введенные значения / Error check entered values'

if __name__ == '__main__':
    type_transf = input('Введите тип преобразования: ')
    temp_transf = float(input('Введите преобразуемое значение: '))
    trans = Temperature_Conversion(type_transf, temp_transf)
    print(trans.tranform(type_transf, temp_transf))


# type_transf = 'cf'
# temp_transf = 100