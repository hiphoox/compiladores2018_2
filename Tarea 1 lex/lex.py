def lex(fileName):
	file = open(fileName, "r")
	text = ''.join(file.read().split())

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
		'main' : 'identifier'
	}

	string = ''
	tokensList = []

	#for que itera en cada uno de los elementos de la cadena 'text'.
	for x in text:
		#Realiza la busqueda de alguna coincidencia con el diccionario tokens
		key = simbols.get(x)
		if key == None:
			string += x
			identifier = identifiers.get(string)
			keyWord = keyWords.get(string)
			if identifier != None:
				tokensList.append(identifier + '('+string+')')
				string=''
			elif keyWord != None:
				tokensList.append(keyWord)
				string=''
		else:
			if string.isdigit():
				tokensList.append('int('+string+')')
			tokensList.append(key)
			string = ''

	print(tokensList)

	return tokensList