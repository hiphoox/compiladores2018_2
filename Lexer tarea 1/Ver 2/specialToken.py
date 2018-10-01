class specialToken:
    def __init___(self,char):
        self.caracter = char
        self.name = nombre(char)
    
	def nombre(char):
        if(cahr == "{"):
            return "openBrace"
        elif (char == "}"):
            return "closeBrace"	