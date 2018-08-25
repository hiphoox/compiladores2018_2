import os, re, sys
from enum import Enum

class Token(Enum):
	LlaveAbre =  "{"
	LlaveCierrra = "}"
	AbreParen = "("
	CierraParen = ")"
	Puntoycoma = ";"
	IntKeyword = "INT"
	ReturnKeyword = "RETURN"

def separar(renglon,token_list):
	renglon = renglon.strip()
	#print(renglon)
	id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', renglon)
	numero = re.match('[0-9]',renglon)
	if (len(renglon)==0):
	    return
	if(id):
	    if id.group(0) == "{":
		    print("Hola Mundo")
		else:
			token_list.append([keyWords([id.group(0)]),id.group(0)])
			separar(renglon.lstrip(id.group(0)),token_list)
	elif(numero):
		token_list.append(['Int',numero.group(0)])
		separar(renglon.lstrip(numero.group(0)),token_list)
	else:
		tok = specialTokens(renglon)
		if(tok!=False):
			token_list.append([tok,Token[tok].value])
			separar(renglon.lstrip(Token[tok].value),token_list)	
				
def specialTokens(renglon):
	if(renglon[0] == "{"):
	    return Token.LlaveAbre.name
	elif(renglon[0] == "}"):
		return Token.LlaveCierrra.name
	elif(renglon[0] == "("):
		return Token.AbreParen.name
	elif(renglon[0] == ")"):
		return Token.CierraParen.name
	elif(renglon[0] == ";"):
		return Token.Puntoycoma.name
	else: return False

def keyWords(token):
	token=token[0]
	if(token =='return'):
		return Token.ReturnKeyword.name
	elif(token == 'int'):
		return Token.IntKeyword.name
	else:	
		return 'Id'			

def leerArchivo(source_file):
    with open(source_file,'r') as file:
        renglon = file.read()
    return renglon
		
def escribirArchivo(token_file):
    with open(token_file,'w') as file:
	    for i in range(len(token_list)):	
		    file.write(str(token_list[i]) + "\n")
	
	
token_list = []
source_file = sys.argv[1]
renglon = leerArchivo(source_file)
separar(renglon,token_list)
token_file = os.path.splitext(source_file)[0] + ".txt"
escribirArchivo(token_file)
print(token_list)