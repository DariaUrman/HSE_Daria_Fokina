"""Необходимо собрать данные с сайта ЦБ РФ с помощью Python.

В ходе выполнения итогового задания вы самостоятельно:
выберите интересующие вас данные на сайте ЦБ РФ,
создадите парсер для их сбора,
подберёте структуру для хранения данных,
создадите модуль для работы с сохранёнными данными.

Шаг 1

Выбрать интересующие данные в следующих разделах на сайте ЦБ:

базы данных (https://www.cbr.ru/hd_base/),
реестры (https://www.cbr.ru/registries/),
статистика (https://www.cbr.ru/statistics/).

Примеры: курс валют, цены на аффинированные драгоценные металлы, реестр микрофинансовых организаций и пр.

! Для выбора недоступна ключевая ставка, которая будет разбираться на одном из вебинаров и примеры для которой приведены в этом ТЗ.

Шаг 2

Определите структуру для хранения и работы. Для ключевой ставки ЦБ РФ это может быть словарь (dict), где ключом будет выступать дата, а значением — размер ключевой ставки на указанную дату:

{
…
datetime.date(2022,4,7): Decimal("0.2000"),
datetime.date(2022,4,8): Decimal("0.2000"),
datetime.date(2022,4,11): Decimal("0.1700"),
datetime.date(2022,4,12): Decimal("0.1700"),
datetime.date(2022,4,13): Decimal("0.1700"),
…
}

Шаг 3

Напишите скрипт, который будет производить сбор данных с выбранной страницы на сайте ЦБ РФ либо осуществлять загрузку xsl/xslx/pdf/csv или иного файла с данными в рабочую директорию с последующим его парсингом.

Шаг 4

Сделайте метод сериализации и десериализации данных для сохранения их в JSON-файл и подготовки данных для работы модулем из Шага 7. При написании метода используйте dict/list comprehensions.

Пример сериализованных данных для ключевой ставки:

{
…
'2022-04-07': '0.2000',
'2022-04-08': '0.2000',
'2022-04-11': '0.1700',
'2022-04-12': '0.1700',
'2022-04-13': '0.1700'
…
}

! Формат JSON не позволяет хранить данные в виде объектов datetime и decimal.

Сохранение файла должно производиться в директорию parsed_data внутри папки проекта. Путь к директории parsed_data должен быть прописан так, чтобы он был кроссплатформенным. Написанный скрипт должен запуститься на любой операционной системе и при запуске скрипта из любой директории.

Шаг 5

Необходимо привести данные к рабочим типам. Например:
Даты привести к строковому формату ISO8601 или к типу datetime.
Числа с плавающей точкой привести к типу decimal или хранить в строковом виде.
И т. д.

Продумайте и реализуйте методологию заполнения пробелов в данных, если это необходимо для работы. Пример для ключевой ставки, которая не публикуется для нерабочих дней, однако используется в расчётах:

{
…
'2022-04-07': '0.2000',
'2022-04-08': '0.2000',
'2022-04-09': '0.2000',
'2022-04-10': '0.2000',
'2022-04-11': '0.1700',
'2022-04-12': '0.1700',
'2022-04-13': '0.1700'
…
}

Шаг 6

Оберните весь написанный код парсера в класс ParserCBRF.

Запуск парсера должен осуществляться через вызов метода start().

Шаг 7

Создайте отдельный класс для работы с собранными данными.

Для работы с ключевой ставкой можно описать класс KeyRateCBRF, экземпляр которого при работе будет обращаться к файлу с сохранёнными данными и через свои методы позволит быстро и удобно получать необходимые данные.

В рассматриваемом случае класс KeyRateCBRF может содержащий следующие публичные методы:

keyrate_by_date(date) — возвращает размер ставки на определённую дату

Input:
KeyRateCBRF.keyrate_by_date(“2022-04-07”)
Output:
"0.2000"

keyrate_last() — возвращает размер ключевой ставки на последнюю доступную дату

Input:
KeyRateCBRF.keyrate_last()
Output:
"0.7500"

keyrate_range_dates(from_date, to_date) — возвращает отсортированный список кортеж пар (дата, ключевая ставка) за определённый период

Input:
KeyRateCBRF.keyrate_range_dates('2022-04-07', '2022-04-13')
Output:
[
('2022-04-07', '0.2000'),
('2022-04-08', '0.2000'),
('2022-04-09', '0.2000'),
('2022-04-10', '0.2000'),
('2022-04-11', '0.1700'),
('2022-04-12', '0.1700'),
('2022-04-13', '0.1700')
]


Методы, указанные выше, являются примером для ключевой ставки. Список методов класса для работы с данными должен быть составлен в зависимости от вида данных, которые вы выбрали.

"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import date
import os
class ParserCBRF:
    def __init__(self):
        self.url = f"http://cbr.ru/hd_base/metall/metall_base_new/?" \
                   f"UniDbQuery.Posted=True&" \
                   f"UniDbQuery.From=01.07.2008&" \
                   f"UniDbQuery.To={self.__today_human_date()}" \
                   f"UniDbQuery.Gold=true&" \
                   f"UniDbQuery.Silver=true&" \
                   f"UniDbQuery.Platinum=true&" \
                   f"UniDbQuery.Palladium=true&" \
                   f"UniDbQuery.so=1"
        self.au_prices = {}
        self.ag_prices = {}
        self.pt_prices = {}
        self.pd_prices = {}
        self.start()
    def __today_human_date(self):
        today = date.today().strftime("%d.%m.%Y")
        return today
    def __get_au_prices_soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        raw_soup = soup.find("table", "data")
        header = raw_soup.find_all("th")[1:]
        au_header = header[0].text.strip()
        raw_price = raw_soup.find_all("tr")[1:]
        for line in raw_price:
            raw_line = line.find_all("td")
            au_date = raw_line[0].text.strip()
            au_price = raw_line[1].text.strip().replace(",", ".")
            self.au_prices[au_header] = au_date, au_price
            print(str(self.au_prices).replace("(", "").replace(")", ""))
            continue

    def __get_ag_prices_soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        raw_soup = soup.find("table", "data")
        header = raw_soup.find_all("th")[1:]
        ag_header = header[1].text.strip()
        raw_price = raw_soup.find_all("tr")[1:]
        for line in raw_price:
            raw_line = line.find_all("td")
            ag_date = raw_line[0].text.strip()
            ag_price = raw_line[2].text.strip().replace(",", ".")
            self.ag_prices[ag_header] = ag_date, ag_price
            print(str(self.ag_prices).replace("(", "").replace(")", ""))
            continue

    def __get_pt_prices_soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        raw_soup = soup.find("table", "data")
        header = raw_soup.find_all("th")[1:]
        pt_header = header[2].text.strip()
        raw_price = raw_soup.find_all("tr")[1:]
        for line in raw_price:
            raw_line = line.find_all("td")
            pt_date = raw_line[0].text.strip()
            pt_price = raw_line[3].text.strip().replace(",", ".")
            self.pt_prices[pt_header] = pt_date, pt_price
            print(str(self.pt_prices).replace("(", "").replace(")", ""))
            continue

    def __get_pd_prices_soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        raw_soup = soup.find("table", "data")
        header = raw_soup.find_all("th")[1:]
        pd_header = header[3].text.strip()
        raw_price = raw_soup.find_all("tr")[1:]
        for line in raw_price:
            raw_line = line.find_all("td")
            pd_date = raw_line[0].text.strip()
            pd_price = raw_line[4].text.strip().replace(",", ".")
            self.pd_prices[pd_header] = pd_date, pd_price
            print(str(self.pd_prices).replace("(", "").replace(")", ""))
            continue

    def __save_file(self):
        prices = {**self.au_prices, **self.ag_prices, **self.pt_prices, **self.pd_prices}
        print(str(prices).replace("(", "").replace(")", ""))
        if not os.path.exists("parsed_data"):
            os.makedirs("parsed_data")
        with open(os.path.join("parsed_data", "metal_prices.json"), "w") as file:
            json.dump(prices, file, ensure_ascii=False)

    def start(self):
        self.__get_au_prices_soup()
        self.__get_ag_prices_soup()
        self.__get_pt_prices_soup()
        self.__get_pd_prices_soup()
        self.__save_file()

def main():
    parser = ParserCBRF()
    prices = parser.start()
    return prices

if __name__=="__main__":
    main()
    print("stop")
