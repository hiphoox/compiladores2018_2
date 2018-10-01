from enum import Enum, unique
import re
import sys
from Compiler.Lexer import *
#leyendo de un archivo
with open(sys.argv[1],"r") as f:
	linea = f.read()

tok = tokeniza(linea)

if(type(tok) is list):
	print('Tokens de la prueba ' + sys.argv[1] + ': \n')
	for x in tok:
		print(x[0] + '<' + x[1] + '>\n')
	print('\n')
else:
	print('Token inválido: ' + tok)

