"""
2) Создайте класс Validator который позволяет проводить проверку данных пользователя при регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — не менее 6 символов
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Валидация каждого элемента в кортеже производится отдельным методом для каждого элемента (validate_email, validate_login, validate_password) в которых в случае непрохождения валидации вызывается ошибка (InvalidPassword, InvalidLogin, InvalidEmail), при соответствии — возвращается значение True. В методе validate необходимо предусмотреть обработку этих ошибок и в случае их наличия — вызвать ошибку ValidationError.
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
    def __init__(self, , login: str, password: str, email: str):
        self.login = login
        self.password = password
        self.email = email

    def validate_login():
        if len(self.login) < 6:
            raise InvalidLogin('Длина логина менее 6 знаков!')
        else:
            return True