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

if(tokens[0] !=  False):
	print(Fore.BLUE + Back.CYAN + Style.DIM +"\------------------------------Tokens------------------------------------")
	print(tokens)
	print('\-------------------------------------------------------------------------' + Fore.RESET)
	ast = parse_program(tokens)	
	if(ast[0] != False):
		print(Fore.MAGENTA + Back.WHITE + Style.DIM +"\------------------------------------AST--------------------------------")
		imprime(ast)
		print(genera(ast[0][1]))
		print("\-----------------------------------------------------------------------")
	else:
		print(Fore.RED + Back.WHITE + Style.DIM+'\----------------------------------------¡Error!------------------------------------/')
		print('Unexpected token ' + ast[1] + '\t' + 'Se esperaba ' + ast[2])
		print('\-----------------------------------------------------------------------------------/')
else:
	print(Fore.RED + Back.WHITE + Style.DIM+'\----------------------------------------¡Error!------------------------------------/')
	print('Invalid token: ' + tokens[1])
	print('\-----------------------------------------------------------------------------------/')



