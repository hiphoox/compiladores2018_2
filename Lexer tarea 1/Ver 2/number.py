def tipo(elemento):
	tmp = str(type(elemento))
	if (tmp == "<class 'int'>"):
		return "int"
	else:
		return "Error"

class number:
	def __init__(self,elemento):
		self.elemento = elemento
		self.name = tipo(elemento)
