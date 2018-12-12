from tokens import Token, UnaryOp, BinaryOp

'''
	Función principal, inicia el parseo de un programa
	al ser recursivo, el error llegará a esta función
	con un false y el token que generó el error
	si todo fué correcto, retorna el ast
'''
def parse_program(tokens, ast = []):
	result = parse_function_declaration(tokens,ast)
	if(result[0] != False):
		ast.append(result)
		return ast		
	else: 
		print('Unexpected token ' + result[1][1] + '\n' + 'Se esperaba ' + result[2])

#Parsea la estructura de una funcion
def parse_function_declaration(tokens,ast):
	nodo = []
	tk = tokens.pop(0)
	if(tk[0] != Token.IntKeyword.name and tk[0] != Token.CharKeyword.name):
		return [False,tk,Token.IntKeyword.name]
	nodo.append(Token[tk[0]].value)

	tk = tokens.pop(0)
	if(tk[0] != 'Id'):
		return [False,tk,'Identifier']
	nodo.append(tk[1])

	tk = tokens.pop(0)
	if(tk[0] != Token.OpenParen.name):
		return [False,tk,Token.OpenParen.name]
	#nodo.append(tk[1])

	tk = tokens.pop(0)
	if(tk[0] != Token.CloseParen.name):
		return [False,tk,Token.CloseParen.name]
	#nodo.append(tk[1])

	tk = tokens.pop(0)
	if(tk[0] != Token.OpenBrace.name):
		return [False,tk,Token.OpenBrace.name]
	#nodo.append(tk[1])	

	result = parse_statement(tokens,ast) # se llama a parse_statement para buscar una expresion valida
	if(result[0] == False):              #si regresa false, en la lista, entonces no encontró algo válido
		return result						
	nodo.append(['Statement',result])					  #si encontró algo válido lo agrego al nodo 'function'	

	tk = tokens.pop(0)
	if(tk[0] != Token.CloseBrace.name):
		return [False,tk,Token.CloseBrace.name]
	return(['Function: ',nodo]) # se retorna el nodo funcion

#parsea la estructura de un statement
def parse_statement(tokens,ast):
	nodo = []	
	tk = tokens.pop(0)
	if(tk[0] != Token.ReturnKeyword.name):
		return[False,tk,Token.ReturnKeyword.name]
	nodo.append(tk[1])

	result = parse_expresion(tokens)  #se busca encontrar una expresion válida, si no retorna false
	if(result[0] == False):		  #implica que sí encontró un nodo 'expresion' y se agrega al nodo 'statement'
		return result
	nodo.append(['Expresion',result])
	tk = tokens.pop(0)
	if(tk[0] != Token.Semicolon.name):
		return[False,tk,Token.Semicolon.name]
	return(nodo) #se retorna el nodo statement

#parsea la estructura de una expresion
def parse_factor(tokens):
	tk = tokens.pop(0)
	if(tk[0] == 'Int'):
		return ['Constant',tk[1]]  #busca que la expresion sea un int, sino, retorna false
	elif(tk[0] == Token.Minus.name or tk[0] == UnaryOp.BitwiseComplement.name or tk[0] == UnaryOp.LogicalNegation.name):
		result = parse_factor(tokens)
		if(result[0] != False):
			my_node = []
			my_node.append([['UnaryOp',tk[0]],result])
			return my_node
		else:
			return result
	elif(tk[0] == Token.OpenParen.name):
		result = parse_expresion(tokens)
		if(result[0] != False):
			tk = tokens.pop(0)
			print("en los  que van dentro de parentesis")
			print(tk)
			if(tk[0] == Token.CloseParen.name):
				my_node = []
				my_node.append([['UnaryOp',tk[0]],result])
				return my_node
			else:
				return [False,tk,Token.CloseParen.name]
		else:
			return result
	else:
		return [False,tk,'Const'] 

def parse_term(tokens):
	factor = parse_factor(tokens)
	if(factor[0] != False):
		my_term = []
		my_term.append(['Term',['Factor',factor]])
		while(True):
			#tk = tokens.pop(0)
			if(tokens[0][0] == BinaryOp.Multiplication.value.name or tokens[0][0] == BinaryOp.Division.value.name):
				tk = tokens.pop(0)
				other_factor = parse_factor(tokens)
				if(other_factor[0] != False):
					my_term.append(["BinaryOp",BinaryOp.Multiplication.value.name] if (tk[0] == BinaryOp.Multiplication.value.name) else ["BinaryOp",BinaryOp.Division.value.name])
					my_term.append(['Factor',other_factor])
				else:
					return other_factor
			else: 
				return my_term
				break
	else:
		return factor


def parse_expresion(tokens):
	term = parse_term(tokens)
	if(term[0] != False):
		my_exp = []
		my_exp.append(term)
		while(True):
			if(tokens[0][0] == BinaryOp.Addition.value.name or tokens[0][0] == BinaryOp.Subtraction.value.name):
				tk = tokens.pop(0)
				other_term = parse_term(tokens)
				if(other_term[0] != False):
					my_exp.append(["BinaryOp",BinaryOp.Addition.value.name] if (tk[0] == BinaryOp.Addition.value.name) else ["BinaryOp",BinaryOp.Subtraction.value.name])
					my_exp.append(other_term)
				else:
					return other_term
			else: 
				return my_exp
				break
	else:
		return term



#imprime ast en pretty mode
def imprime(nodes,level = 1):
	for l in nodes:
		if(type(l) is list):
			imprime(l,level + 2)
		else:
			print(" "*level+l)

