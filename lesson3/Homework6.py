"""Соберите информацию о судебных заседаниях в деле № А40-183194/2015 (дело о банкротстве ООО «ТрансИнвестХолдинга»).

На сайте https://kad.arbitr.ru/ в каждом деле приложен .ics файл (стандартное расширение файлов для программ календарей), в котором присутствует информация о дате и времени судебных заседаний (вы можете открыть его, кликнув по дате заседания в карточке). Однако в них присутствует и «пустая» информация, дублирующая информацию о событиях по делу, но не относящуюся к конкретным судебным заседаниям.
Чтобы ознакомиться со структурой данных в ics файле и провести первичный анализ, достаточно открыть его в любом текстовом редакторе"""

from ics import Calendar, Event
from datetime import datetime

with open('/Users/dariafokina/Downloads/А40-183194-2015.ics', 'r') as c_c:
    f = Calendar(c_c.read())
    new_c = Calendar()
    for event in f.events:
        if event.begin and isinstance(event.begin, datetime):
            new_c.events.add(event)
import json
with open('court_dates.json', 'w') as c_c:
    json.dump(new_c,c_c)










