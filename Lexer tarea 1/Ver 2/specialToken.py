def nombre(elemento): #compara el elemento que recibió con los specialToken existentes
		if(elemento == "{"):
			return "openBrace"
		elif (elemento == "}"):
			return "closeBrace"
		elif (elemento == "("):
			return "openParen"
		elif (elemento == ")"):
			return "closeParen"
		elif (elemento == ";"):
			return "semicolon"
		else:
			return "Error"

class specialToken: #Creamos la clase specialToken para etiquetar
	def __init__(self,elemento):
		self.elemento = elemento
		self.name = nombre(elemento)
