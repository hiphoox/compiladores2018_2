import os, sys
def leerArchivo(source_file): #De momento solo abrimos un archivo y ponemos su contenido en una sola variable
	with open(source_file,'r') as file:
		renglon = file.read()
	return renglon
