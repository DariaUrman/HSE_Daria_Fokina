"""Реализуйте структуру данных «Участники спора». Она должна представлять собой список (list) словарей (dict).

Каждый словарь хранит информацию об отдельном участнике. Словарь содержит пары «ключ-значение» параметрами, то есть характеристиками участника: наименование, статус, ИНН.

Заполнение данных должно быть произведено пользователем через консоль для трёх различных участников.

Пример готовой структуры:
[
{“name”: 'ООО "Рога и Копыта"', “status”: "Истец", “inn”: "4545454545"},
{“name”: 'Баширов А.А.', “status”: "Ответчик", “inn”: "32323232323232"},
{“name”: 'Петров А.А.', “status”: "Третье лицо", “inn”: "12121212121212"}
]

Выведите полученные данные в консоль.
"""

a=None
proj_dict = {"name": None, "status": None, "inn": None}
fp_dict=proj_dict.copy()
fp_dict["name"] = "ООО Рога и Копыта"
fp_dict["status"]="Истец"
fp_dict["inn"]=4545454545

sp_dict=proj_dict.copy()
sp_dict["name"] = "Баширов А.А."
sp_dict["status"]="Ответчик"
sp_dict["inn"]=32323232323232

tp_dict=proj_dict.copy()
tp_dict["name"] = "Петров А.А."
tp_dict["status"]="Третье лицо"
tp_dict["inn"]=12121212121212

list =[fp_dict,
       sp_dict,
       tp_dict]
print (*list, sep ="\n")
