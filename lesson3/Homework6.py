"""Соберите информацию о судебных заседаниях в деле № А40-183194/2015 (дело о банкротстве ООО «ТрансИнвестХолдинга»).

На сайте https://kad.arbitr.ru/ в каждом деле приложен .ics файл (стандартное расширение файлов для программ календарей), в котором присутствует информация о дате и времени судебных заседаний (вы можете открыть его, кликнув по дате заседания в карточке). Однако в них присутствует и «пустая» информация, дублирующая информацию о событиях по делу, но не относящуюся к конкретным судебным заседаниям.
Чтобы ознакомиться со структурой данных в ics файле и провести первичный анализ, достаточно открыть его в любом текстовом редакторе"""

from ics import Calendar
import json
from datetime import datetime, timedelta
import zoneinfo

def cleaned_list(case_number):
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    #f-string использовано, чтобы в наименование файла подавался аргумент
    with open(f"{case_number}.ics", "r") as f:
        all_list = f.read()
    c = Calendar(all_list)
    cleaned_events = [i for i in c.events if i.begin.datetime > datetime.now(zone) - timedelta(days=5000)]
    final_list = [{"case_number": f"{case_number}",
               "start": i.begin.datetime.isoformat(),
               "end": i.end.datetime.isoformat(),
               "location": i.location.strip(),
               "description": i.description
               } for i in cleaned_events]
    with open("court_dates.json", "w") as f:
        json.dump(final_list, f)
    return final_list







