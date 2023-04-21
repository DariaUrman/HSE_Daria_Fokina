# Абстракция "Договор"

class Contract:
	def __init__(self, number, date, counterparty, subject, sum):
    	  self.number = number
    	  self.date = date
    	  self.counterparty = counterparty
          self.subject = subject
          self.sum = sum
    	  self.is_prolonged = False
    def is_active(self):
    	self.is_prolonged = True
    	print("Договор пролонгирован")
    def is_expired(self):
    	self.is_prolonged = False
    	print("Срок действия договора истек")
    def change_sum(self, new_sum):
    	self.sum = new_sum
    	print(f"Сумма договора {self.sum}")
