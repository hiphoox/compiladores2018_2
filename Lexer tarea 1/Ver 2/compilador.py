import os, sys
from archivos import leerArchivo
from Lex import lexer
from parser2 import paser_program
			
lista_token = [] #Lista de tokens
ast = [None,None,None]
source_file = sys.argv[1] #Pasamos el argumento del archivo a compilar
renglon = leerArchivo(source_file) #leemos el archivo y lo pasamos a un renglón
lista_token = lexer(renglon,lista_token) #Ejecutamos el lexer
ast = paser_program(lista_token,ast) #Ejecutamos el parser
