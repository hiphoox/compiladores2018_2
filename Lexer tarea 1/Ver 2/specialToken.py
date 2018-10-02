def nombre(char): #compara el elemento que recibió con los specialToken existentes
		if(char == "{"):
			return "openBrace"
		elif (char == "}"):
			return "closeBrace"
		elif (char == "("):
			return "openParen"
		elif (char == ")"):
			return "closeParen"
		elif (char == ";"):
			return "semicolon"
		else:
			return "Error"

class specialToken: #Creamos la clase specialToken para etiquetar
	def __init__(self,char):
		self.caracter = char
		self.name = nombre(char)
