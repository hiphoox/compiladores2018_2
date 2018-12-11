import sys
from tokens import Token
from lexer import *
from parser import *

#leyendo de un archivo
with open(sys.argv[1],"r") as f:
	linea = f.read()


print('\n\nProbando con ' + sys.argv[1])


tokens = tokeniza(linea)
print(tokens)
if(type(tokens) is list):
	ast = parse_program(tokens)	
if(ast != None):
	imprime(ast)
