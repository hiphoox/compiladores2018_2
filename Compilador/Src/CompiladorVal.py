from Lexer import *
from Parser import *



def compilador():
	file = "pruebas/ex1.c"
	

	tokens = Lex(file)
	if not tokens:
		print("Error de compilacion")
		return 0
	print(tokens)

	ast = parcerProgram(tokens)
	
	if ast == False:
		print("Error sintactico")
		return 0
	print("Valor regreso", ast)
	#codeGenerator(_ast)

compilador()