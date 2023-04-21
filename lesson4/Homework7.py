"""Реализуйте класс CourtCase.

При вызове метода конструктора экземпляра (__init__) должны создаваться следующие атрибуты экземпляра:
case_number (строка с номером дела — обязательный параметр) передаётся в качестве аргумента при создании экземпляра
case_participants (список по умолчанию пустой)
listening_datetimes (список по умолчанию пустой)
is_finished (значение по умолчанию False)
verdict (строка по умолчанию пустая)

У экземпляра должны быть следующие методы:
set_a_listening_datetime — добавляет в список listening_datetimes судебное заседание (структуру можете придумать сами)
add_participant — добавляет участника в список case_participants (можно просто ИНН)
remove_participant — убирает участника из списка case_participants
make_a_decision — вынести решение по делу, добавить verdict и сменить атрибут is_finished на True """

class CourtCase:
    def __init__(self, case_number:str, case_participants=[], listening_datetimes=[], verdict=""):
        self.case_number = case_number
        self.case_participants = case_participants
        self.listening_datetimes = listening_datetimes
        self.is_finished = False
        self.verdict = verdict
    def set_a_listening_datetime(self, new_datetimes):
        print(self.listening_datetimes.append(new_datetimes))

    def add_participant(self,participant):
        print(self.case_participants.append(participant))

    def remove_participant(self, participant):
        if participant in case_participants:
            print(self.case_participants.remove(participant))

    def make_a_decision(self,verdict):
        self.verdict=verdict
        self.is_finished = True
        print(f"{self.verdict} решение по делу вынесено.")