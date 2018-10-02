import os, sys
def leerArchivo(source_file):
	with open(source_file,'r') as file:
		renglon = file.read()
	return renglon