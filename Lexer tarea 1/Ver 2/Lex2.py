import os, re, sys
import os, re, sys, specialToken

def separar(renglon,token_list):
	renglon = renglon.strip()
	id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', renglon)
	numero = re.match('[0-9]',renglon)
	print(numero)
	if (len(renglon)==0):
	    return
	if(id):
		token_list.append([keyWords([id.group(0)]),id.group(0)])
		separar(renglon.lstrip(id.group(0)),token_list)
	elif(numero):
		token_list.append(['Int',numero.group(0)])
		separar(renglon.lstrip(numero.group(0)),token_list)
	else:
		tok = specialTokens(renglon[0])
		if(tok.name() != "Error"):
			token_list.append([tok.caracter,tok.name])
			separar(renglon.lstrip(Token[tok].value),token_list)
				
def leerArchivo(source_file):
    with open(source_file,'r') as file:
        renglon = file.read()
    return renglon
			
token_list = []
source_file = sys.argv[1]
renglon = leerArchivo(source_file)
separar(renglon,token_list)
print(token_list)
