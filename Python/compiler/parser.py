from tokens import Token
from tokens import UnaryOp

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
	nodo.append(tk[1])
	return(['Function: ',nodo]) # se retorna el nodo funcion

#parsea la estructura de un statement
def parse_statement(tokens,ast):
	nodo = []	
	tk = tokens.pop(0)
	if(tk[0] != Token.ReturnKeyword.name):
		return[False,tk,Token.ReturnKeyword.name]
	nodo.append(tk[1])

#	tk = tokens.pop(0)
	result = parse_expresion(tokens)  #se busca encontrar una expresion válida, si no retorna false
	print(result)
	if(result[0] == False):		  #implica que sí encontró un nodo 'expresion' y se agrega al nodo 'statement'
		return result
	nodo.append(['Expresion',result])

	tk = tokens.pop(0)
	if(tk[0] != Token.Semicolon.name):
		return[False,tk,Token.Semicolon.name]
	nodo.append(tk[1])
	return(nodo) #se retorna el nodo statement

#parsea la estructura de una expresion
def parse_expresion(tokens,nodo = []):
	tk = tokens.pop(0)
	if(tk[0] == 'Int'):
		return ['Constant',tk[1]]  #busca que la expresion sea un int, sino, retorna false
	elif(tk[0] == UnaryOp.Negation.name or tk[0] == UnaryOp.BitwiseComplement.name or tk[0] == UnaryOp.LogicalNegation.name):
		result = parse_expresion(tokens,nodo)
		if(result[0] != False):
			my_node = []
			my_node.append([['UnaryOp',tk[0]],result])
			return my_node
		else:
			return result
	else:
		return[False,tk,'Const'] 


#imprime ast en pretty mode
def imprime(nodes,level = 1):
	for l in nodes:
		if(type(l) is list):
			imprime(l,level + 1)
		else:
			print(" "*level+l)

