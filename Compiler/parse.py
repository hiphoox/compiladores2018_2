from wrappers import Prog
from wrappers import Fun
from wrappers import Return
from wrappers import Operator
from wrappers import Integer
from wrappers import UnOp
from wrappers import Identifier
from wrappers import BinOp
"""
Gramatica de Backus-NaurForm para primer programa:
	<program> ::= <function>
	<function> ::= "int" <id> "(" ")" "{" <statement> "}"
	<statement> ::= "return" <exp> ";"
	<exp> ::= <int>
"""
def unary_op(_unary_op):
	if _unary_op == 'minus':
		return True
	if _unary_op == 'logicalNegation':
		return True
	if _unary_op == 'bitwiseComplement':
		return True
	return False

#Define la gramatica: <factor> ::= "(" <exp> ")" | <unary_op> <factor> | <int>
def factor(_factor):
	tok = _factor.pop(0)
	if _factor == []:
		return (False, False)
	if tok == 'openParentesis':
		exp, _factor = expresion(_factor)
		if _factor.pop(0) != 'closeParentesis':
			return (False, False)
		return (exp, _factor)
	if type(tok) is Operator and unary_op(tok.operator):
		operator = tok
		print('--------- ' + tok.operator)
		tok, _factor = factor(_factor)
		if type(_factor) is bool:
			return (False, False)
		return (UnOp(operator, tok), _factor)
	if type(tok) is Integer:
		print('--------- ' + str(tok.int))
		return (tok, _factor)
	return (False, False)


#Define la gramatica: <term> ::= <factor> { ("*" | "/") <factor> }
def term(_term):
	termi, _term = factor(_term)
	if termi:
		operator = _term[0]
		if type(operator) is Operator and ( operator.operator == 'multiplication' or operator.operator == 'division'):
			operator = _term.pop(0)
			print('--------- ' + operator.operator)
			next_term, _term = factor(_term)
			if next_term is bool:
				return (False, False)
			return (BinOp(operator, termi, next_term), _term)
		return (termi, _term)
	return (False, False)


#Define la gramatica : <exp> ::= <term> { ("+" | "-") <term> }
def expresion(_expresion):
	termi, _expresion = term(_expresion)
	if termi:
		operator = _expresion[0]
		if type(operator) is Operator and ( operator.operator == 'addition' or operator.operator == 'minus'):
			operator = _expresion.pop(0)
			print('--------- ' + operator.operator)
			next_term, _expresion = term(_expresion)
			if next_term is bool:
				return (False, False)
			return (BinOp(operator, termi, next_term), _expresion)
		return (termi, _expresion)
	return (False, False)


#Define la gramatica: <statement> ::= "return" <exp> ";"
def statement(_statement):
	statement = _statement.pop(0)
	if statement!='returnKeyWord':
		return (False, False)
	print('------- Return')
	exp, _statement = expresion(_statement)
	if type(_statement) is bool or _statement == [] or _statement.pop(0) != 'semiColon':
		return (False, False)
	return (Return(exp), _statement)


#Define la gramatica: <function> ::= "int" <id> "(" ")" "{" <statement> "}"
def function(_function):
	function_Name = _function.pop(0)
	if (_function == [] or type(function_Name) is not Identifier) or (_function.pop(0)!='openParentesis') or (_function.pop(0)!='closeParentesis') or (_function.pop(0)!='openBrace'):
		return False
	print('---- Function ' + function_Name.funName)
	returnn, _function = statement(_function)
	if type(_function) is bool or _function == [] or _function.pop(0) != 'closeBrace':
		return False
	return Fun(function_Name, returnn)


#Define la gramatica: <program> ::= <function>
def program(_program):
	if _program == [] or _program.pop(0) != 'intKeyWord':
		return False
	print('-- Program')
	func = function(_program)
	if not func:
		return False
	return Prog(func)


#Funcion parcer
def parcer(_tokenList):
	if _tokenList == []:
		return False
	return program(_tokenList)