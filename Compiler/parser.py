import lex
"""
Gramatica de Backus-NaurForm para primer programa:
	<program> ::= <function>
	<function> ::= "int" <id> "(" ")" "{" <statement> "}"
	<statement> ::= "return" <exp> ";"
	<exp> ::= <int>
"""

#Define la gramatica: <exp> ::= <int>
def expresion(_expresion):
	_ast = []
	if type(_expresion[0]) is lex.Integer:
		_ast.append(_expresion[0].int)
		return _ast
	else:
		return False

#Define la gramatica: <statement> ::= "return" <exp> ";"
def statement(_statement):
	_ast = []
	if _statement[0]=='returnKeyWord':
		_ast.append(_statement[0])
		_ast.append(expresion(_statement[1:]))
		return _ast
	else:
		return False

#Define la gramatica: <function> ::= "int" <id> "(" ")" "{" <statement> "}"
def function(_function):
	_ast = []
	if (type(_function[0]) is lex.Identifier) and (_function[1]=='openParentesis') and (_function[2]=='closeParentesis') and (_function[3]=='openBrace'):
		_ast.append(_function[0].id)
		_ast.append(statement(_function[4:]))
		return _ast
	else:
		return False

#Define la gramatica: <program> ::= <function>
def program(_program):
	if _program[0] == 'intKeyWord':
		return function(_program[1:])
	else:
		return False

#Funcion parcer
def parcer(_tokens):
	_ast = []
	if _tokens != []:
		_ast = (program(_tokens))
	return _ast