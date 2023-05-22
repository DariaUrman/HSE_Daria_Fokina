"""Напишите класс SirotinskyAPI для взаимодействия с API, размещённым по адресу https://api.sirotinsky.com/.

Класс должен содержать в себе функционал для работы со всеми методами, указанными в документации к API, которые размещены по адресу https://api.sirotinsky.com/docs.

Метод инициализации экземпляра класса должен принимать в качестве аргументов логин и пароль для получения токена авторизации и сразу производить вызов приватного метода для получения токена в целях его сохранения как аргумента экземпляра.

Метод получения токена должен быть приватным и не доступен для вызова вне класса.

Методы для получения данных из ЕФРСБ должны быть публичными

Данные для доступа:
Логин: HSE_student
Пароль: 123123123

"""

import requests

class SirotinskyAPI:
    BASE_URL = "https://api.sirotinsky.com"
    auth = {
    "username":"HSE_student",
    "password":"123123123"
    }

    def __init__(self):
        self.__get_token()
        pass
    def get_root(self, url):
        r = requests.get(url)
        result = r.json()
        return result

    def __get_token(self):
        url = f"{self.BASE_URL}/token"
        r = requests.post(url, data=self.auth)
        result = r.json()["access_token"]
        self.token = result

    def get_hello(self, name):
        url = f"{self.BASE_URL}/hello/{name}"
        r = requests.get(url)
        return r.json()

    def get_manager(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/manager/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_trader(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/trader/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_person(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/person/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

    def get_organisation(self, inn):
        url = f"{self.BASE_URL}/{self.token}/efrsb/organisation/{inn}"
        r = requests.get(url)
        result = r.json()
        return result

def main():
    s_api = SirotinskyAPI()
    hello = s_api.get_hello("Someone")
    manager = s_api.get_manager("507901739192")
    trader = s_api.get_trader("742403257984")
    person = s_api.get_person("470313416330")
    organisation = s_api.get_organisation("7701272485")
    print(hello, manager, trader, person, organisation)

if __name__=="__main__":
    main()
    print("stop")


