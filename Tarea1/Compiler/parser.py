from enum import Enum, unique
import re
import sys
import Lexer
#leyendo de un archivo
with open(sys.argv[1],"r") as f:
	linea = f.read()

tokens = Lexer.tokeniza(linea)

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

def parse_program(tokens, ast = []):
	result = parse_function_declaration(tokens,ast)
	if(result[0] != False):
		ast.append(result)
		return ast		
	else: 
		print('Unexpected token ' + result[1][1] + '\n')

def parse_function_declaration(tokens,ast):
	nodo = []
	tk = tokens.pop(0)
	if(tk[0] != Token.IntKeyword.name and tk[0] != Token.CharKeyword.name):
		return [False,tk]
	nodo.append(Token[tk[0]].value)
	tk = tokens.pop(0)
	if(tk[0] != 'Id'):
		return [False,tk]
	nodo.append(tk[1])
	tk = tokens.pop(0)
	if(tk[0] != Token.OpenParen.name):
		return [False,tk]
	nodo.append(tk[1])
	tk = tokens.pop(0)
	if(tk[0] != Token.CloseParen.name):
		return [False,tk]
	nodo.append(tk[1])
	tk = tokens.pop(0)
	if(tk[0] != Token.OpenBrace.name):
		return [False,tk]
	nodo.append(tk[1])	
	result = parse_statement(tokens,ast)
	if(result[0] == False):
		return result
	nodo.append(result)
	tk = tokens.pop(0)
	if(tk[0] != Token.CloseBrace.name):
		return [False,tk]
	nodo.append(tk[1])
	return(['Function: ',nodo])

def parse_statement(tokens,ast):
	nodo = []	
	tk = tokens.pop(0)
	if(tk[0] != Token.ReturnKeyword.name):
		return[False,tk]
	nodo.append(tk[1])
	tk = tokens.pop(0)
	result = parse_expresion(tk)
	if(result[0] == False):
		return result
	nodo.append(result)
	tk = tokens.pop(0)
	if(tk[0] != Token.Semicolon.name):
		return[False,tk]
	nodo.append(tk[1])
	return(['Statement: ', nodo])
	
def parse_expresion(token):
	nodo = []
	if(token[0] == 'Int'):
		return['Expresion',token[1]]
	else:
		return[False,token] 

	

def imprime(nodes):
	for l in nodes:
		if(type(l) is list):
			print('\n')
			imprime(l)
		else:
			print(list)

print('probando con ' + sys.argv[1])
ast = parse_program(tokens)
#imprime(ast)
