from tokens import Token, UnaryOp, BinaryOp
from Error import ErrorSintactico
'''
	Función principal, inicia el parseo de un programa
	al ser recursivo, el error llegará a esta función
	con un false y el token que generó el error
	si todo fué correcto, retorna el ast
'''
def parse_program(tokens, ast = []):
	result = parse_function_declaration(tokens,ast)
	if(type(result) != ErrorSintactico):
		ast.append(result)
		return ast		
	else: 
		return result

#Parsea la estructura de una funcion
def parse_function_declaration(tokens,ast):
	nodo = []
	tk = tokens.pop(0)
	if(tk[0] != Token.IntKeyword.name and tk[0] != Token.CharKeyword.name):
		return ErrorSintactico(tk,Token.IntKeyword.name)
	#nodo.append(['ReturnType' , Token[tk[0]].value])

	tk = tokens.pop(0) if len(tokens) > 0 else ['']
	if(tk[0] != 'Id'):
		return ErrorSintactico(tk,'Identifier')
	nodo.append(tk[1])

	tk = tokens.pop(0) if len(tokens) > 0 else ['']
	if(tk[0] != Token.OpenParen.name):
		return ErrorSintactico(tk,Token.OpenParen.name)
	#nodo.append(tk[1])

	tk = tokens.pop(0) if len(tokens) > 0 else ['']
	if(tk[0] != Token.CloseParen.name):
		return ErrorSintactico(tk[0],Token.CloseParen.name)
	#nodo.append(tk[1])

	tk = tokens.pop(0) if len(tokens) > 0 else ['']
	if(tk[0] != Token.OpenBrace.name):
		return ErrorSintactico(tk,Token.OpenBrace.name)
	#nodo.append(tk[1])	

	result = parse_statement(tokens,ast) # se llama a parse_statement para buscar una expresion valida
	if(type(result) == ErrorSintactico):              #si regresa false, en la lista, entonces no encontró algo válido
		return result						
	nodo.append(['Statement',result])					  #si encontró algo válido lo agrego al nodo 'function'	

	tk = tokens.pop(0) if len(tokens) > 0 else ['']
	if(tk[0] != Token.CloseBrace.name):
		return ErrorSintactico(tk[0],Token.CloseBrace.name)
	return(['Function',nodo]) # se retorna el nodo funcion

#parsea la estructura de un statement
def parse_statement(tokens,ast):
	nodo = []	
	tk = tokens.pop(0)
	if(tk[0] != Token.ReturnKeyword.name):
		return ErrorSintactico(tk[0],Token.ReturnKeyword.name)
	nodo.append(tk[1])

	result = parse_expresion(tokens)  #se busca encontrar una expresion válida, si no retorna false
	if(type(result) == ErrorSintactico):		  #implica que sí encontró un nodo 'expresion' y se agrega al nodo 'statement'
		return result
	nodo.append(result)
	tk = tokens.pop(0)
	if(tk[0] != Token.Semicolon.name):
		return ErrorSintactico(tk[0],Token.Semicolon.name)
	return nodo #se retorna el nodo statement

#parsea la estructura de una expresion
def parse_factor(tokens):
	tk = tokens.pop(0)
	if(tk[0] == 'Int'):
		return ['Constant',tk[1]]  #busca que la expresion sea un int, sino, retorna false
	elif(tk[0] == Token.Minus.name or tk[0] == UnaryOp.BitwiseComplement.name or tk[0] == UnaryOp.LogicalNegation.name):
		result = parse_factor(tokens)
		if(type(result) != ErrorSintactico):
			my_node = [['UnaryOp',tk[0]],result]
			return my_node
		else:
			return result
	elif(tk[0] == Token.OpenParen.name):
		result = parse_expresion(tokens)
		if(type(result) != ErrorSintactico):
			tk = tokens.pop(0)
			if(tk[0] == Token.CloseParen.name):
				my_node = result
				return my_node
			else:
				return ErrorSintactico(tk,Token.CloseParen.name)
		else:
			return result
	else:
		return ErrorSintactico(tk[0],'Const')

def parse_term(tokens):
	factor = parse_factor(tokens)
	if(type(factor) != ErrorSintactico):
		my_term = ['Term']
		while(True):
			#tk = tokens.pop(0)
			if(tokens[0][0] == BinaryOp.Multiplication.value.name or tokens[0][0] == BinaryOp.Division.value.name):
				tk = tokens.pop(0)
				other_factor = parse_factor(tokens)
				if(type(other_factor) != ErrorSintactico):
					factor = [["BinaryOp",BinaryOp.Multiplication.value.name] if (tk[0] == BinaryOp.Multiplication.value.name) else ["BinaryOp",BinaryOp.Division.value.name],['Factor',factor],['Factor',other_factor]]
				else:
					return other_factor
			else: 
				return ['Term',factor]
				break
		#my_term.append(factor)
	else:
		return factor


def parse_expresion(tokens):
	term = parse_term(tokens)
	if(type(term) != ErrorSintactico):
		my_exp = ['Expresion']
		while(True):
			if(tokens[0][0] == BinaryOp.Addition.value.name or tokens[0][0] == BinaryOp.Subtraction.value.name):
				tk = tokens.pop(0)
				other_term = parse_term(tokens)
				if(type(other_term) != ErrorSintactico):
					term = [["BinaryOp",BinaryOp.Addition.value.name] if (tk[0] == BinaryOp.Addition.value.name) else ["BinaryOp",BinaryOp.Subtraction.value.name],term,other_term]
				else:
					return other_term
			else: 
				return ['Expresion',term]
				break
		#my_exp.append(term)
	else:
		return term

#imprime ast en pretty mode
def imprime(nodes,level = 1):
	for l in nodes:
		if(type(l) is list):
			imprime(l,level + 2)
		else:
			print(" "*level+l)

