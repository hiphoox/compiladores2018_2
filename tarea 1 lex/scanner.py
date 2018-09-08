from enum import Enum
import re

class Integers(Enum): #Se crea la clase que contiene los elementos que puede presentar el programa.
	LlaveIn =  "{"
	LlaveOut = "}"
	IntKey = "INT"
	CharKey = "CHAR"
	ReturnKey = "RETURN"
	ParentesisIn = "("
	ParentesisOut = ")"
	Semicolon = ";"

tok = []                               #Arreglo que contendra la separacion del programa.
with open("return_2.c","r") as f:
	cadena = f.read()                  #Leemos el archivo que solo se carga en modo de lectura.


def Separa(cadena,tok):
	cadena = cadena.strip()            #Elimina los espacios que puedan existir entre las palabras de la cadena
	id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', cadena)   # Busca las palabras entre el rango establecidos.
	numero = re.match('[0-9]',cadena)                    #Busca numeros entre el rango establecido
	if(len(cadena)==0):
		return
	if(id):
		tok.append([keyW([id.group(0)]),id.group(0)])     #Si existe alguna coincidencia group() devolverá el resultado
		Separa(cadena.lstrip(id.group(0)),tok)            #Se corta de la cadena el numero que se haya encontrado
	elif(numero):
		tok.append(['Int',numero.group(0)])
		Separa(cadena.lstrip(numero.group(0)),tok)
	else:
		toks = TokensNormales(cadena)
		if(toks!=False):                             #En caso de no coincidir, se busca un caracter especial
			tok.append([toks,Integers[toks].value])
			Separa(cadena.lstrip(Integers[toks].value),tok)     #Se corta de la cadena el caracter especial que se haya encontrado

def TokensNormales(cadena):                #Se verifica las coincidencias dentro de la cadena
	if(cadena[0] == "{"):
		return Token.LlaveIn.name
	elif(cadena[0] == "}"):
		return Token.LlaveOut.name
	elif(cadena[0] == "("):
		return Token.ParentesisIn.name
	elif(cadena[0] == ")"):
		return Token.ParentesisOut.name
	elif(cadena[0] == ";"):
		return Token.Semicolon.name
	else: return False                   

def keyW(token):                         #Se verifica las coincidencias dentro de la clase definida al inicio
	token=token[0]
	if(token =='return'):
		return Integers.ReturnKey.name
	elif(token == 'int'):
		return Integers.IntKey.name
	elif(token == 'char'):
		return Integers.CharKey
	else:	
		return 'Id'


Separa(cadena,tok)
print(tok)
