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

