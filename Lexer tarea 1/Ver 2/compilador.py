import os, sys
from Lex2 import lexer
from archivos import leerArchivo
			
lista_token = []
source_file = sys.argv[1]
renglon = leerArchivo(source_file)
lista_token = lexer(renglon,lista_token)
print(lista_token)