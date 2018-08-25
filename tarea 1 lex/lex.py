import os, re, sys
from enum import Enum

class Token(Enum):  # se crea la clase token tal como seindica en el archivo de nora
	LlaveAbre =  "{"
	LlaveCierrra = "}"
	AbreParen = "("
	CierraParen = ")"
	Puntoycoma = ";"
	IntKeyword = "INT"
	ReturnKeyword = "RETURN"

def tokenizar(programa,token_list): #se separa el string "programa" 
	programa = programa.strip()
	id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', programa)#se buscan patrones el en string y se sacan
	numero = re.match('[0-9]',programa)
	if (len(programa)==0):#cuando ya se haya sacado todo del renglón se empieza a salir de la recursividad
	    return
	if(id):
		token_list.append([keyWords([id.group(0)]),id.group(0)])#se agregan la "palabra" al nuevo arreglo
		tokenizar(programa.lstrip(id.group(0)),token_list)# se vuelve a tokenizar el programa pero quitandole la "palabra que ya se agregó
	elif(numero):
		token_list.append(['Int',numero.group(0)])#mismo paso que arriba pero con los numeros solos que se tomarán siempre como enteros(por ahora)
		tokenizar(programa.lstrip(numero.group(0)),token_list)#mismo paso que arriba
	else:
		tok = specialToks(programa)#en caso de no ser palabra ni numero se compara en el proceso "specialtoks" para ver si es un caracter reconosido
		if(tok!=False): #si no hay un false el proceso sigue sin errores
			token_list.append([tok,Token[tok].value])
			tokenizar(programa.lstrip(Token[tok].value),token_list)#mismo paso que arriba	
				
def specialToks(programa):#se comparan todos los caracteres que hasta este punto tenemos y se regresa la "palabra clave" en caso de encontrarse uno
	if(programa[0] == "{"):
	    return Token.LlaveAbre.name
	elif(programa[0] == "}"):
		return Token.LlaveCierrra.name
	elif(programa[0] == "("):
		return Token.AbreParen.name
	elif(programa[0] == ")"):
		return Token.CierraParen.name
	elif(programa[0] == ";"):
		return Token.Puntoycoma.name
	else: return False#se regresa un false si no es caracter reconosido 

def keyWords(token): #si es alguna de las palabras que se tienen, se regresa el keyword, si no se regresa la palabra
	token=token[0]
	if(token =='return'):
		return Token.ReturnKeyword.name
	elif(token == 'int'):
		return Token.IntKeyword.name
	else:	
		return token			

def leerArchivo(source_file):#se lee el programa
    with open(source_file,'r') as file:
        programa = file.read()
    return programa 
		
#se crea el arreglo y se ejecutan las funciones	
token_list = []
source_file = sys.argv[1]#sys.argv funciona para abrir el programa desde la consola 
programa = leerArchivo(source_file)
tokenizar(programa,token_list)
print(token_list)
