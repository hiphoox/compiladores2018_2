import re


"""
	<program> ::= <function>
	<function> ::= "int" <id> "(" ")" "{" <statement> "}"
	<statement> ::= "return" <exp> ";"
	<exp> ::= <int>

"""


#<exp> ::= <int>
def expresion(fn):
	if len(fn) == 2:
		const=fn[0]+fn[1] 
	else:
		const=fn[0]

	return const

#<statement> ::= "return" <exp> ";"
def statement(tokens):
	if tokens.pop(0) == 'ReturnKeyword':
		const=expresion(tokens[0])
		tokens.pop(0)
		if tokens.pop(0) == 'Semicolon':
			return const
		else:
			print("Falto Semicolon")
			return False
	else:
		print("Falta Statement")
		return False;



#<function> ::= "int" <id> "(" ")" "{" <statement> "}"
def function(tokens):
	if tokens.pop(0) == 'CharKeyword' and tokens.pop(0) == 'OpenParen' and tokens.pop(0) == 'CloseParen' and tokens.pop(0) == 'OpenBrace': 
		const = statement(tokens)
		if tokens == []:
			print("Error de Sintaxis")
			return False
		if tokens.pop(0) == 'CloseBrace':
			return const
		else:
			print("Error de Sintaxis Falta un }")
			return False
	else:
		print("Error de compilación Error de Sintaxis") 
		return False;


#<program> ::= <function>
def program(tokens):
	if tokens.pop(0) == 'IntKeyword':
		return function(tokens)
	else:
		print("Error de Compilacion: Falta de tipo de Dato int")
		return False
	

#Parseo
def parcerProgram(tokens):
	if tokens == []:
		print("Error de Compilacion: Falta de tokens")
	else:
		return program(tokens)
	