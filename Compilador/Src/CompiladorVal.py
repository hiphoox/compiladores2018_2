from Lexer import *
from Parser import *
from codeGenerator import *


def compilador():
	#file = "pruebas/Funcionan/ex1.c"           #Funciona
	#file = "pruebas/Funcionan/multi_digit.c"    #Funciona
	#file = "pruebas/Funcionan/newlines.c"        #Funciona
	#file = "pruebas/Funcionan/no_newlines.c"     #Funciona
	#file = "pruebas/Funcionan/return_0.c"      #Funciona
	#file = "pruebas/Funcionan/return_2.c"   #Funciona
	file = "pruebas/Funcionan/spaces.c"     #Funciona
	#file = "pruebas/Funcionan/spaces2.c"     #Funciona

	#No funcionan
	#file = "pruebas/NoFuncionan/missing_paren.c"     #NoFunciona
	#file = "pruebas/NOFuncionan/missing_retval.c"     #NoFunciona
	#file = "pruebas/NOFuncionan/no_brace.c"     #NoFunciona
	#file = "pruebas/NOFuncionan/no_semicolon.c"     #NoFunciona
	#file = "pruebas/NOFuncionan/no_space.c"     #NoFunciona->

	

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