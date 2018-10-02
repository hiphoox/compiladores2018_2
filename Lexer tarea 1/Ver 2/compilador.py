import os, sys
from Lex import lexer
from archivos import leerArchivo
			
lista_token = [] #Lista de tokens
source_file = sys.argv[1] #Pasamos el argumento del archivo a compilar
renglon = leerArchivo(source_file) #leemos el archivo y lo pasamos a un renglón
lista_token = lexer(renglon,lista_token) #Ejecutamos el lexer
print(lista_token) #Imprimimos la lista
