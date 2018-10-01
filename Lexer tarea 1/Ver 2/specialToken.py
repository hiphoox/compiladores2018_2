class specialToken:
    def __init___(self,char):
        self.caracter = char
        self.name = nombre(char)
    
	def nombre(self,char):
	    if(cahr == "{"):
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
		    print("Elemento no identificado.")
			return "Error"
