"""Напишите скрипт, который будет производить сбор данных с выбранной страницы на сайте ЦБ РФ, либо осуществлять загрузку xsl, xslx, pdf, csv или иного файла с данными в рабочую директорию с последующим его парсингом.

У класса должен быть только один публичный метод start(). Все остальные методы, содержащие логику по выгрузке и сохранению данных, должны быть приватными.

Определите структуру для хранения. Например, для ключевой ставки ЦБ РФ это может быть словарь (dict), где ключом будет выступать дата, а значением — размер ключевой ставки на указанную дату.

Оберните весь написанный код парсера в класс ParserCBRF
"""
import requests
from bs4 import BeautifulSoup
import json


class ParserCBRF:
    def __init__(self):
        self.url = "https://cbr.ru/currency_base/daily/"
        self.currency = {}
        self.start()
        pass

    def __get_rates_soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, "html.parser")
        raw_currency = soup.find("table", "data").find_all("tr")[1:]
        for line in raw_currency:
            currency_line = line.find_all("td")
            currency_name = currency_line[1].text.strip()
            currency_rate = currency_line[4].text.strip()
            self.currency[currency_name] = currency_rate
            return self.currency

    def __save_file(self):
        with open("currency.json", "w") as file:
            json.dump(self.currency, file)
    def start(self):
        self.__get_rates_soup()
        self.__save_file()
        pass
def main():
    parser = ParserCBRF()
    currency = parser.start()
    print(currency)

if __name__=="__main__":
    main()
    print("stop")
