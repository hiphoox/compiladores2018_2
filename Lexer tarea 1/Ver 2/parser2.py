from specialToken import specialToken
from keywords import keywords
from number import number

def paser_program(lista_token,ast):
	if(len(lista_token) == 0): #comprobamos que el lexer salió bien
		return ast
	ast[1] = "Program"
	tmp = function(lista_token)
	if(tmp[0] == False):
		print("Error, elemento no esperado: " + tmp[1])
		ast =[]
		return ast
	ast[2] = tmp
	print(ast)
	return ast

def function(token):
	ls = [None,None,None]
	tok = token.pop(0)
	if(tok.name != "INTKEYWORD"):
		ls = [False,tok.elemento]
		return ls
	
	tok = token.pop(0)
	if(tok.name != "ID"):
		ls = [False,tok.elemento]
		return ls
	ls[1] = tok.elemento

	tok = token.pop(0)
	if(tok.name != "openParen"):
		ls = [False,tok.elemento]
		return ls

	tok = token.pop(0)
	if(tok.name != "closeParen"):
		ls = [False,tok.elemento]
		return ls

	tok = token.pop(0)
	if(tok.name != "openBrace"):
		ls = [False,tok.elemento]
		return ls

	tmp = statement(token)
	if(tmp[0] == False):
		return tmp
	ls[2] = tmp

	tok = token.pop(0)
	if(tok.name != "closeBrace"):
		ls = [False,tok.elemento]
		return ls
	return ls

def statement(token):
	ls = [None,None,None]
	tok = token.pop(0)
	if(tok.name != "RETURNKEYWORD"):
		ls = [False,tok.elemento]
		return ls
	ls[1] = tok.elemento
	
	tmp = expression(token)
	if(tmp[0] == False):
		return tmp
	ls[2] = tmp

	tok = token.pop(0)
	if(tok.name != "semicolon"):
		ls = [False,tok.elemento]
		return ls
	return ls

def expression(token):
	ls = [None,None,None]
	tok = token.pop(0)
	if(tok.name != "int"):
		ls = [False,tok.elemento]
		return ls
	ls[1] = tok.elemento
	return ls