import re
from tokens import Token
'''Función principal, se encarga de buscar identificadores
	y dígitos decimales con ayuda de expresiones regulares
	de no encontrar los dos anteriores, busca los tokens
	especificados en la enumeracion token
	Se quita la parte de la cadena que hace match y se 
	llama de manera recursiva a la funcion
	@param string line
	@param list tokens
'''
def tokeniza(linea,tokens = []):
	id_regex = '\\(*[A-Za-z][A-Za-z0-9]*\\)*'
	num_regex = '\\d+'
	special_char_regex = "^({|}|\\(|\\)|;|-|!|~)"
	
	linea = linea.lstrip()

	if(len(linea)==0):
		return 
	if(re.match(id_regex, linea)):
		id = re.match(id_regex, linea)
		tokens.append([keyWords(id.group(0)),id.group(0)])
		tokeniza(linea.lstrip(id.group(0)),tokens)
	elif(re.match(num_regex,linea)):
		numero = re.match(num_regex,linea) 
		tokens.append(['Int',numero.group(0)])
		tokeniza(linea.lstrip(numero.group(0)),tokens)
	elif(re.match(special_char_regex,linea)):
		special_char = re.match(special_char_regex,linea)
		tok = singularTokens(special_char.group(0))
		tokens.append([tok,Token[tok].value])
		tokeniza(linea.lstrip(Token[tok].value),tokens)
	else:
		return 'token inválido: ' + linea[0]
	return tokens
'''
	KeyWords recibe un  token obtenido de ls expresión regular 
	para identificadores y determina 
	de qué tipo es este token
	@param: string token
	@return: etiqueta del token
'''
def keyWords(token):
	#print(token)
	if(token == Token.ReturnKeyword.value):
		return Token.ReturnKeyword.name
	elif(token == Token.IntKeyword.value):
		return Token.IntKeyword.name
	elif(token == Token.CharKeyword.value):
		return Token.CharKeyword.name
	else:	
		return 'Id'

'''
	recibe un caracter y valida si se encuentra
	definido en los tokens de la enumeracion
	@param string linea
	@return string etiqueta del token || false
'''
def singularTokens(token):
	if(token == "{"):
		return Token.OpenBrace.name
	elif(token == "}"):
		return Token.CloseBrace.name
	elif(token == "("):
		return Token.OpenParen.name
	elif(token == ")"):
		return Token.CloseParen.name
	elif(token == ";"):
		return Token.Semicolon.name
	elif(token == "-"):
		return Token.Negation.name
	elif(token == "~"):
		return Token.BitwiseComplement.name
	elif(token == "!"):
		return Token.LogicalNegation.name
