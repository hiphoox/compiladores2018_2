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
def expresion(_expresion):
	value = _expresion.pop(0)
	_ast = []
	if _expresion != [] and type(value) is lex.Integer:
		_ast.append(value)
		return (_ast, _expresion)
	else:
		return False

#Define la gramatica: <statement> ::= "return" <exp> ";" (1)
def statement(_statement):
	statement = _statement.pop(0)
	_ast = []
	if statement=='returnKeyWord':
		_ast.append(statement)
		piece, _statement = expresion(_statement)
		_ast.append(piece)
		if _statement != [] and  _statement.pop(0) == 'semiColon':
			return (_ast, _statement)
	else:
		return False

#Define la gramatica: <function> ::= "int" <id> "(" ")" "{" <statement> "}" (1)
def function(_function):
	_ast = []
	function_Name = _function.pop(0)
	if (_function != [] and type(function_Name) is lex.Identifier) and (_function.pop(0)=='openParentesis') and (_function.pop(0)=='closeParentesis') and (_function.pop(0)=='openBrace'):
		_ast.append(function_Name)
		piece, _function = statement(_function)
		_ast.append(piece)
		if _function != [] and _function.pop(0) == 'closeBrace':
			return _ast
	else:
		return False

#Define la gramatica: <program> ::= <function> (1)
def program(_program):
	if _program != [] and _program.pop(0) == 'intKeyWord':
		return function(_program)
	else:
		return False

#Funcion parcer (1)
def parcer(_tokens):
	if _tokens != []:
		return program(_tokens)
	return False