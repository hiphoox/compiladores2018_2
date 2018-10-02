import re


"""
	<program> ::= <function>
	<function> ::= "int" <id> "(" ")" "{" <statement> "}"
	<statement> ::= "return" <exp> ";"
	<exp> ::= <int>

"""


#<exp> ::= <int>
def expresion(fn):
	fin=re.match('[0-9]+',fn)
	print(fin.group(0))
	return fin.group(0)

#<statement> ::= "return" <exp> ";"
def statement(fn):
	for token in fn:
		if re.match('[0-9]+',token):
			regreso = expresion(token)
			return regreso;
		if token == 'Semicolon':
			fn.remove(token)
		elif token== 'CloseBrace':
			fn.remove(token)
		else:
			return False;



#<function> ::= "int" <id> "(" ")" "{" <statement> "}"
def function(tokens):
	fn=[]
	fn = tokens

	for token in fn:
		if token == 'CharKeyword':
			fn.remove(token)
		elif token  == 'OpenParen':
			fn.remove(token)
		elif token  == 'CloseParen':
			fn.remove(token)
		elif token == 'OpenBrace':
			fn.remove(token)
			print(fn)
		elif token  == 'ReturnKeyword':
				fn.remove(token)
				Val_Retorno = statement(fn)
				####
				print(Val_Retorno)
				print(fn)
				if Val_Retorno == False:
					return False
				else:
					return Val_Retorno
		else:
			print("Error de Compilacion")
			return False

#<program> ::= <function>
def program(tokens):
	if tokens.pop(0) == 'IntKeyword':
		return function(tokens)
	else:
		print("Error de Compilacion")
		return False
	

#Parseo
def parcerProgram(tokens):
	if tokens == []:
		print("Error de Compilacion")
	else:
		return program(tokens)
	