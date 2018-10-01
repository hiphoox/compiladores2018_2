from enum import Enum, unique
import re
import sys

#creando enumeracion de tokens

@unique
class Token(Enum):
	OpenBrace =  "{"
	CloseBrace = "}"
	OpenParen = "("
	CloseParen = ")"
	Semicolon = ";"
	IntKeyword = "int"
	CharKeyword = "char"
	ReturnKeyword = "return"

'''lista que guardará en listas de longitud 2 
   los tokens, [etiqueta,token]
'''

'''Función principal, se encarga de buscar identificadores
	y dígitos decimales con ayuda de expresiones regulares
	de no encontrar los dos anteriores, busca los tokens
	especificados en la enumeracion token
	Se quita la parte de la cadena que hace match y se 
	llama de manera recursiva a la funcion
	@param string line
	@param list tokens
'''
def tokeniza(linea,tokens = []):
	linea = linea.lstrip()	
	id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', linea) #expresion regular para identificadores
	numero = re.match('[0-9]+',linea)  #expresión regular para numeros
	if(len(linea)==0):
		return 
	if(id):
		tokens.append([keyWords(id.group(0)),id.group(0)])
		tokeniza(linea.lstrip(id.group(0)),tokens)
	elif(numero):
		tokens.append(['Int',numero.group(0)])
		tokeniza(linea.lstrip(numero.group(0)),tokens)
	else:
		tok = singularTokens(linea[0])
		if(tok!=False):
			tokens.append([tok,Token[tok].value])
			tokeniza(linea.lstrip(Token[tok].value),tokens)
		else:
			return linea[0]
	return tokens
'''
	KeyWords recibe un  token obtenido de ls expresión regular 
	para identificadores y determina 
	de qué tipo es este token
	@param: string token
	@return: etiqueta del token
'''
def keyWords(token):
	#print(token)
	if(token == Token.ReturnKeyword.value):
		return Token.ReturnKeyword.name
	elif(token == Token.IntKeyword.value):
		return Token.IntKeyword.name
	elif(token == Token.CharKeyword.value):
		return Token.CharKeyword.name
	else:	
		return 'Id'

'''
	recibe un caracter y valida si se encuentra
	definido en los tokens de la enumeracion
	@param string linea
	@return string etiqueta del token || false
'''
def singularTokens(token):
	if(token == "{"):
		return Token.OpenBrace.name
	elif(token == "}"):
		return Token.CloseBrace.name
	elif(token == "("):
		return Token.OpenParen.name
	elif(token == ")"):
		return Token.CloseParen.name
	elif(token == ";"):
		return Token.Semicolon.name
	else: 
		return False

