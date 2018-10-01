def nombre(elemento):
		if(elemento == "int"):
			return "INTKEYWORD"
		elif(elemento == "return"):
			return "RETURNKEYWORD"
		elif(elemento == "main"):
			return "ID"
		else:
			return "Error"

class keywords:
	def __init__(self,elemento):
		self.elemento = elemento
		self.name = nombre(elemento)
