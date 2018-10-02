import lex
"""
Gramatica de Backus-NaurForm para primer programa:
	<program> ::= <function>
	<function> ::= "int" <id> "(" ")" "{" <statement> "}"
	<statement> ::= "return" <exp> ";"
	<exp> ::= <int>
"""

# (1) -> La funcion realiza lo que debe de manera natural.
# (0) -> La funcion realiza lo que debe pero no de manera natual.

#Define la gramatica: <exp> ::= <int> (1)
def expresion():
	value = tokens.pop(0)
	_ast = []
	if tokens != [] and type(value) is lex.Integer:
		_ast.append(value.int)
		return _ast
	else:
		return False

#Define la gramatica: <statement> ::= "return" <exp> ";" (1)
def statement():
	_statement = tokens.pop(0)
	_ast = []
	if _statement=='returnKeyWord':
		_ast.append(_statement)
		_ast.append(expresion())
		if tokens != [] and  tokens.pop(0) == 'semiColon':
			return _ast
	else:
		return False

#Define la gramatica: <function> ::= "int" <id> "(" ")" "{" <statement> "}" (1)
def function():
	_ast = []
	function_Name = tokens.pop(0)
	if (tokens != [] and type(function_Name) is lex.Identifier) and (tokens.pop(0)=='openParentesis') and (tokens.pop(0)=='closeParentesis') and (tokens.pop(0)=='openBrace'):
		_ast.append(function_Name.id)
		_ast.append(statement())
		if tokens != [] and tokens.pop(0) == 'closeBrace':
			return _ast
	else:
		return False

#Define la gramatica: <program> ::= <function> (1)
def program():
	if tokens != [] and tokens.pop(0) == 'intKeyWord':
		return function()
	else:
		return False

#Funcion parcer (1)
def parcer(_tokens):
	global tokens
	tokens = _tokens
	if tokens != []:
		return program()
	return False