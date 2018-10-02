def nombre(elemento): #compara el elemento que recibió con las keywords existentes
		if(elemento == "int"):
			return "INTKEYWORD"
		elif(elemento == "return"):
			return "RETURNKEYWORD"
		elif(elemento == "main"):
			return "ID"
		else:
			return "Error"

class keywords: #Creamos la clase keyword para etiquetar
	def __init__(self,elemento):
		self.elemento = elemento
		self.name = nombre(elemento)
