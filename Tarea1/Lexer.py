from enum import Enum, unique
import re

#creando enumeracion de tokens

@unique
class Token(Enum):
	OpenBrace =  "{"
	CloseBrace = "}"
	OpenParen = "("
	CloseParen = ")"
	Semicolon = ";"
	IntKeyword = "INT"
	CharKeyword = "CHAR"
	ReturnKeyword = "RETURN"


tokens = []
with open("prueba.txt","r") as f:
	linea = f.read()


def tokeniza(linea,tokens):
	linea = linea.strip()	
	id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', linea)
	numero = re.match('[0-9]',linea)
	if(len(linea)==0):
		return
	if(id):
		tokens.append([keyWords([id.group(0)]),id.group(0)])
		tokeniza(linea.lstrip(id.group(0)),tokens)
	elif(numero):
		tokens.append(['Int',numero.group(0)])
		tokeniza(linea.lstrip(numero.group(0)),tokens)
	else:
		tok = singularTokens(linea)
		if(tok!=False):
			tokens.append([tok,Token[tok].value])
			tokeniza(linea.lstrip(Token[tok].value),tokens)

def singularTokens(linea):
	if(linea[0] == "{"):
		return Token.OpenBrace.name
	elif(linea[0] == "}"):
		return Token.CloseBrace.name
	elif(linea[0] == "("):
		return Token.OpenParen.name
	elif(linea[0] == ")"):
		return Token.CloseParen.name
	elif(linea[0] == ";"):
		return Token.Semicolon.name
	else: return False

def keyWords(token):
	token=token[0]
	if(token =='return'):
		return Token.ReturnKeyword.name
	elif(token == 'int'):
		return Token.IntKeyword.name
	elif(token == 'char'):
		return Token.CharKeyword
	else:	
		return 'Id'


tokeniza(linea,tokens)
print(tokens)


