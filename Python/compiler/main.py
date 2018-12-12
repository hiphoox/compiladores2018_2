import sys
from tokens import Token
from lexer import *
from parser import *
from colorama import init, Fore, Back, Style

#leyendo de un archivo
with open(sys.argv[1],"r") as f:
	linea = f.read()

init()
print(Fore.BLUE + Back.WHITE + Style.DIM+'\n\nProbando con ' + sys.argv[1])


tokens = tokeniza(linea)
print(Fore.BLUE + Back.CYAN + Style.DIM +"\------------------------------Tokens------------------------------------")
print(tokens)
print('\-------------------------------------------------------------------------' + Fore.RESET)

if(type(tokens) is list):
	ast = parse_program(tokens)	
if(ast != None):
	print(Fore.MAGENTA + Back.WHITE + Style.DIM +"\------------------------------------AST--------------------------------")
	imprime(ast)
	print("\-----------------------------------------------------------------------")
