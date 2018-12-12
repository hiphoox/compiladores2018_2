from Lexer import *
from Parser import *
from codeGenerator import *


def compilador():
	file = "pruebas/ex1.c"           #Funciona
	#file = "pruebas/multi_digit.c"    #Funciona
	#file = "pruebas/newlines.c"        #Funciona
	#file = "pruebas/no_newlines.c"     #Funciona
	#file = "pruebas/return_0.c"      #Funciona
	#file = "pruebas/return_2.c"   #Funciona
	#file = "pruebas/spaces.c"     #Funciona
	

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