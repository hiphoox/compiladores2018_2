import os, re, sys
from specialToken import specialToken
from keywords import keywords

def separar(renglon,lista_token):
	renglon = renglon.strip()
	print(renglon + "\n")
	id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', renglon)
	numero = re.match('[0-9]',renglon)
	if (len(renglon)==0):
	    return
	if(id):
		obj = keywords(id.group(0))
		lista_token.append([obj.elemento, obj.name])
		separar(renglon.lstrip(id.group(0)),lista_token)
	elif(numero):
		lista_token.append(['Int',numero.group(0)])
		separar(renglon.lstrip(numero.group(0)),lista_token)
	else:
		tok = specialToken(str(renglon[0]))
		if(tok.name != "Error"):
			lista_token.append([tok.caracter,tok.name])
			separar(renglon.lstrip(Token[tok].value),lista_token)
				
def leerArchivo(source_file):
    with open(source_file,'r') as file:
        renglon = file.read()
    return renglon
			
lista_token = []
source_file = sys.argv[1]
renglon = leerArchivo(source_file)
separar(renglon,lista_token)
print(lista_token)
