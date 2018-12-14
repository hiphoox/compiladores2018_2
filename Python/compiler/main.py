import sys
from tokens import Token
from lexer import *
from parser import *
from generator import *
from colorama import init, Fore, Back, Style

#leyendo de un archivo
with open(sys.argv[1],"r") as f:
	linea = f.read()

init()
print(Fore.BLUE + Back.WHITE + Style.DIM+'\n\nProbando con ' + sys.argv[1])


tokens = tokeniza(linea)
if(type(tokens) != ErrorLexico):
	print(Fore.BLUE + Style.DIM +"\------------------------------Tokens------------------------------------")
	print(tokens)
	print('\-------------------------------------------------------------------------' + Fore.RESET)
	ast = parse_program(tokens)	
	if(type(ast) != ErrorSintactico):
		print(Fore.MAGENTA + Back.WHITE + Style.DIM +"\------------------------------------AST--------------------------------")
		imprime(ast)
		print("\-----------------------------------------------------------------------")
		print(Fore.RED + Back.WHITE + Style.DIM+genera(ast[0]))
	else:
		print(Fore.RED + Back.WHITE + Style.DIM+'\----------------------------------------¡Error!------------------------------------/')
		print(str(ast.informacion))
		print('\-----------------------------------------------------------------------------------/')
else:
	print(Fore.RED + Back.WHITE + Style.DIM+'\----------------------------------------¡Error!------------------------------------/')
	print(str(tokens.informacion))
	print('\-----------------------------------------------------------------------------------/')



