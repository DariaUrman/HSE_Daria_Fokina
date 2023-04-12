"""1. Найдите информацию об организациях:
Получите список ИНН из файла «traders.txt»;
Найдите информацию об организациях с этими ИНН в файле «traders.json»;
Сохраните информацию об ИНН, ОГРН и адресе организаций из файла «traders.txt» в файл «traders.csv»."""

#a.Получите список ИНН из файла «traders.txt»;

with open("/Users/dariafokina/Downloads/traders.txt", "r") as f:
    print(f.read())

#b.Найдите информацию об организациях с этими ИНН в файле «traders.json»;

import json

with open('/Users/dariafokina/Downloads/traders.json', 'r') as json_file:
    traders = json.load(json_file)

    result = [
        [a for a in traders if a['inn'] == '7702758341'],
        [b for b in traders if b['inn'] == '7802654025'],
        [c for c in traders if c['inn'] == '5027217264'],
        [d for d in traders if d['inn'] == '6324042940'],
        [e for e in traders if e['inn'] == '5834031870'],
        [f for f in traders if f['inn'] == '1657061756'],
        [g for g in traders if g['inn'] == '3665044042'],
        [h for h in traders if h['inn'] == '6453102410']

    ]

    print(result)

lines = result
with open("/Users/dariafokina/Downloads/traders.txt", "w") as txt_file:
        txt_file.writelines("%s\n" % line for line in lines)

#c.Сохраните информацию об ИНН, ОГРН и адресе организаций из файла «traders.txt» в файл «traders.csv».

import csv

with open('traders.csv', 'w') as out_file:
    names = ["inn", "ogrn", "address"]
    file_writer = csv.DictWriter(out_file, lineterminator="\r", fieldnames=names)
    file_writer.writeheader()
    file_writer.writerow({'inn': '7702758341', 'ogrn': '1117746257640', 'address': '119334, г Москва, Гагаринский р-н, ул Косыгина, д 5, помещ V ком 10'})
    file_writer.writerow({'inn': '7802654025', 'ogrn': '1187847030194', 'address': '197022, г Санкт-Петербург, Петроградский р-н, ул Профессора Попова, д 41/5 литера а, помещ 3Н офис 1'})
    file_writer.writerow({'inn': '5027217264', 'ogrn': '1145027017618', 'address': '140000, Московская обл, г Люберцы, Октябрьский пр-кт, д 249, помещ 22 офис 3'})
    file_writer.writerow({'inn': '6324042940', 'ogrn': '1136324009326', 'address': '445054, Самарская обл, г Тольятти, Центральный р-н, ул Карбышева, д 12, ком 10'})
    file_writer.writerow({'inn': '5834031870', 'ogrn': '1055802033737', 'address': '440023, Пензенская обл, г Пенза, Железнодорожный р-н, ул Стрельбищенская, д 60, офис 303'})
    file_writer.writerow({'inn': '1657061756', 'ogrn': '1061685050350', 'address': '420095, Респ Татарстан, г Казань, Московский р-н, ул Энергетиков, д 2, офис 17'})
    file_writer.writerow({'inn': '3665044042', 'ogrn': '1043600013929', 'address': '394038, Воронежская обл, г Воронеж, ул Дорожная, д 18, офис 7'})
    file_writer.writerow({'inn': '6453102410', 'ogrn': '1086453005594', 'address': '410033, Саратовская обл, г Саратов, Ленинский р-н, пр-кт им 50 лет Октября, д 101'})

"""2.Напишите регулярное выражение для поиска email-адресов в тексте.

Для этого напишите функцию, которая принимает в качестве аргумента текст в виде строки и возвращает список найденных email-адресов или пустой список, если email-адреса не найдены.

Используйте дата-сет на 1000 сообщений из Единого федерального реестра сведений о банкротстве (ЕФРСБ) для практики.

Есть дата-сеты и побольше:
дата-сет на 10 000 сообщений,
дата-сет на 100 000 сообщений,
но если компьютер слабый, ограничьтесь самым маленьким.

Текст сообщений можно найти по ключу «msg_text».

Найдите все email-адреса в дата-сете и соберите их в словарь, где ключом будет выступать ИНН опубликовавшего сообщение («publisher_inn»), а в значении будет хранится множество set() с email-адресами. Пример:

{
“77010127248512”: {“name_surname@yandex.ru”, “name_surname@mail.ru”}
“77011235421242”: {“name_surname@yandex.ru”, “name_surname@gmail.com”}
…
}

Сохраните собранные данные в файл «emails.json».
"""
import json
import re

with open('/Users/dariafokina/Downloads/1000_efrsb_messages.json', 'r') as json_register_file:
    register = json.load(json_register_file)
results = {}
for i in register:
    email = re.findall(r'\S+@\S+\.\S+', i['msg_text'])
    for one_email in email:
        one_email = one_email.lower()
        listed = results.get(i['publisher_inn'])
        if listed and one_email not in listed:
            results[i['publisher_inn']].append(one_email)
        elif not listed:
            new_msg = {i['publisher_inn']: [one_email]}
            results.update(new_msg)
    with open('email.json', "w") as json_register_file:
        json.dump(results, json_register_file)
    print("stop")
