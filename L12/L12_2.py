"""
2) Создайте класс Validator который позволяет проводить проверку данных пользователя при регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — не менее 6 символов
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Валидация каждого элемента в кортеже производится отдельным методом для каждого элемента (validate_email, validate_login, 
validate_password) в которых в случае непрохождения валидации вызывается ошибка (InvalidPassword, InvalidLogin, InvalidEmail), 
при соответствии — возвращается значение True. В методе validate необходимо предусмотреть обработку этих ошибок и в случае их 
наличия — вызвать ошибку ValidationError.
Ошибки создать самостоятельно
например
validator = Validator()
validator.validate(user_login, Some!Password, mail@mail.com)
# True
validator.validate(user, Some!Password, mail@mail.com)
#  ValidationError
"""

class InvalidLogin(Exception):
    pass

class InvalidPassword(Exception):
    pass

class InvalidEmail(Exception):
    pass


class Validator():

    def __init__(self, login: str, password: str, email: str):
        self.login = login
        self.password = password
        self.email = email


    def validate_login(self) -> bool:
        """login — не менее 6 символов"""
        if len(self.login) < 6:
            raise InvalidLogin('Длина логина менее 6 знаков!')
        else:
            return True


    def validate_password(self) -> bool:
        from string import ascii_lowercase, ascii_uppercase, punctuation
        """password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)"""
        if len(self.password) >= 8 and len(set(self.password) & set(ascii_lowercase)) > 1 and len(set(self.password) & set(ascii_uppercase)) > 1 and len(
            set(self.password) & set(punctuation)) > 1:
                return True
        else:
            raise InvalidPassword ('Ошибка. Пароль не соответствует следующим требованиям: не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа')

    def validate_email(self) -> bool:
        """email — присутствует символ @, оканчивается . и 2 символами (.by)"""
        email_zone = {'.by','.com','.ru','.io','.net'}
        # print(self.email[(len(self.email) - self.email[::-1].find('.') - 1):])
        if '@' in self.email and self.email[(len(self.email) - self.email[::-1].find('.') - 1):] in email_zone:
            return True
        else:
            raise InvalidPassword ('Ошибка. Email не соответствует следующим требованиям:  присутствует символ @, оканчивается . и 2 символами (.by)')

    def validate(self) -> bool:
        try:
            self.validate_login()
            self.validate_password()
            self.validate_email()
        except (InvalidLogin, InvalidEmail, InvalidPassword):
            return False
        else:
            return True





pass_valid = Validator('Radik1337Blr','qwe!@#QWEzxc','radikmotocross@gmail.com')
print(pass_valid.validate())

pass_valid2 = Validator('Radik1337Blr','qwe!@#QWEzxc','radikmotocross@gmail.com').validate()
print(pass_valid2)