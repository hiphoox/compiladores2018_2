from tokens import Token

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
		print('Unexpected token ' + result[1][1] + '\n')

#Parsea la estructura de una funcion
def parse_function_declaration(tokens,ast):
	nodo = []
	tk = tokens.pop(0)
	if(tk[0] != Token.IntKeyword.name and tk[0] != Token.CharKeyword.name):
		return [False,tk]
	nodo.append(Token[tk[0]].value)

	tk = tokens.pop(0)
	if(tk[0] != 'Id'):
		return [False,tk]
	nodo.append(tk[1])

	tk = tokens.pop(0)
	if(tk[0] != Token.OpenParen.name):
		return [False,tk]
	nodo.append(tk[1])

	tk = tokens.pop(0)
	if(tk[0] != Token.CloseParen.name):
		return [False,tk]
	nodo.append(tk[1])

	tk = tokens.pop(0)
	if(tk[0] != Token.OpenBrace.name):
		return [False,tk]
	nodo.append(tk[1])	

	result = parse_statement(tokens,ast) # se llama a parse_statement para buscar una expresion valida
	if(result[0] == False):              #si regresa false, en la lista, entonces no encontró algo válido
		return result						
	nodo.append(result)					  #si encontró algo válido lo agrego al nodo 'function'	

	tk = tokens.pop(0)
	if(tk[0] != Token.CloseBrace.name):
		return [False,tk]
	nodo.append(tk[1])
	return(['Function: ',nodo]) # se retorna el nodo funcion

#parsea la estructura de un statement
def parse_statement(tokens,ast):
	nodo = []	
	tk = tokens.pop(0)
	if(tk[0] != Token.ReturnKeyword.name):
		return[False,tk]
	nodo.append(tk[1])

	tk = tokens.pop(0)
	result = parse_expresion(tk)  #se busca encontrar una expresion válida, si no retorna false
	if(result[0] == False):		  #implica que sí encontró un nodo 'expresion' y se agrega al nodo 'statement'
		return result
	nodo.append(result)

	tk = tokens.pop(0)
	if(tk[0] != Token.Semicolon.name):
		return[False,tk]
	nodo.append(tk[1])
	return(['Statement: ', nodo]) #se retorna el nodo statement

#parsea la estructura de una expresion
def parse_expresion(token):
	nodo = []
	if(token[0] == 'Int'):
		return['Expresion',token[1]]  #busca que la expresion sea un int, sino, retorna false
	else:
		return[False,token] 

#imprime ast en pretty mode
def imprime(nodes,level = 1):
	for l in nodes:
		if(type(l) is list):
			imprime(l,level + 1)
		else:
			print(" "*level+l)

