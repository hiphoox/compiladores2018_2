def tipo(num):
	tmp = str(type(num))
	if (tmp == "<class 'int'>"):
		return "int"
	else:
		return "Error"

class number:
	def __init__(self,num):
		self.numero = num
		self.type = tipo(num)