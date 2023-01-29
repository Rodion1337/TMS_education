"""3. Создайте класс Validator который позволяет проводить проверку данных пользователя при
регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — от 6 до 10 символов английского алфавит и цифр 0-9 в любой последовательности
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Проверку на соответствие правилам выполнить регулярными выражениями. По результатам работы метода validate пользователь получит 
True если все 3 элемента прошли проверку, в противном случае - False
"""
from re import match

class InvalidLogin(Exception):
    pass

class InvalidPassword(Exception):
    pass

class InvalidEmail(Exception):
    pass


class Validator():
    #from string import ascii_lowercase, ascii_uppercase, punctuation

    # def __init__(self, login: str, password: str, email: str):
    #     self.login = login
    #     self.password = password
    #     self.email = email
    #     self.pattern_login = r'^[A-Za-z0-9]{6,10}$'
    #     self.pattern_password = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    #     self.pattern_email = r'^[\w.-]+@[\w.-]+\.(\S{2}$)'
    

    pattern_login = r'^[A-Za-z0-9]{6,10}$'
    pattern_password = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    pattern_email = r'^[\w.-]+@[\w.-]+\.(\S{2}$)'


    def validate_login(login:str, pattern_login=pattern_login) -> bool:
        """login — не менее 6 символов"""
        if match(pattern_login, login):
            return True 
        else:
            raise InvalidLogin('Длина логина менее 6 знаков!')
            # return ('Длина логина менее 6 знаков!')



    def validate_password(password: str, pattern_password=pattern_password) -> bool:
        """password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)"""
        if match(pattern_password, password):
            return True 
        else:
            raise InvalidPassword ('Ошибка. Пароль не соответствует следующим требованиям: не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа')
            # return ('Ошибка. Пароль не соответствует следующим требованиям: не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа')

    def validate_email(email: str, pattern_email=pattern_email) -> bool:
        """email — присутствует символ @, оканчивается . и 2 символами (.by)"""
        email_zone = {'.by','.com','.ru','.io','.net'}
        # print(self.email[(self.email.rfind('.')):])
        # if '@' in self.email and self.email[(self.email.rfind('.')):] in email_zone:
        if match(pattern_email, email):
            return True
        else:
            raise InvalidPassword ('Ошибка. Email не соответствует следующим требованиям:  присутствует символ @, оканчивается . и 2 символами (.by)')
            # return ('Ошибка. Email не соответствует следующим требованиям:  присутствует символ @, оканчивается . и 2 символами (.by)')

    def validate(self) -> bool:
        try:
            self.validate_login()
            self.validate_password()
            self.validate_email()
        except (InvalidLogin, InvalidEmail, InvalidPassword):
            return False
        else:
            return True
