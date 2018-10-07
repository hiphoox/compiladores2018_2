from Lexer import *
from Parser import *
from codeGenerator import *


def compilador():
	file = "pruebas/ex1.c"
	

	tokens = Lex(file)
	if not tokens:
		print("Error de compilacion")
		return 0
	print(tokens)

	ast = parcerProgram(tokens)
	
	if ast == False:
		print("Error sintactico: False")
		return 0
	print("---->", ast)
	
	codeGenerator(ast)



compilador()