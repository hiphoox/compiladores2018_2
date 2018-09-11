import re #Biblioteca para expresiones regulares

def lex(fileName):
	text = ''.join(open(fileName, "r").read().split())

	simbols = {
		'(' : 'openParentesis',
		')' : 'closeParentesis',
		'{' : 'openBrace',
		'}' : 'closeBrace',
		';' : 'semicolon'
	}
	keyWords = {
		'int' : 'intKeyWord',
		'return' : 'returnKeyWord'
	}
	identifiers = {
		'main' : 'id'
	}

	string = ''
	tokensList = []

	#for que itera en cada uno de los elementos de la cadena 'text'.
	for x in text:
		"""Pendiente: Debido a que estamos usando la funcion split, esta nos genera una cadena continua, por tal
		razon si dentro de 'return_2.c' ingreso 'int2return' el lexer lo separara internamente y lo dara por valido
		por lo tanto queda pendiente con caracter de IMPORTANTE, pues no afecta directamente al la siguiente etapa.

		Propuesta de solucion:
		string += x
		if x == '|':
			print(string)
		"""
		#Realiza la busqueda de alguna coincidencia con el diccionario tokens
		key = simbols.get(x)
		if key == None:
			string += x
			#Realiza una busqueda dentro de keyWords e indentifiers
			identifier = identifiers.get(string)
			keyWord = keyWords.get(string)
			if identifier != None:
				tokensList.append(identifier + '<'+string+'>')
				string=''
			elif keyWord != None:
				tokensList.append(keyWord)
				string=''
		else:
			"""Comprobamos que lo anterior sea un numero, de no serlo significara que no se encuentra definido
			dentro de ningun diccionario y en consecuencia debera mandar un error lexico"""
			if string.isdigit():
				tokensList.append('const<'+string+'>')
			elif string != '':
				return 'undefined simbol'
			tokensList.append(key)
			string = ''

	return tokensList