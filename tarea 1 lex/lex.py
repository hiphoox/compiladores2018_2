from definitions import tokens, keyWords

def lex(fileName):
	file = open(fileName, "r")
	text = ''.join(file.read().split())

	tokens = '(){};'
	keyWords = dict()
	keyWords = {
		'int' : 'intKeyWord',
		'return' : 'returnKeyWord',
		'main'	: 'functionKeyWord'
	}
	string = ''
	tokensList = []

	for x in text:
		if tokens.find(x) == -1:
			string += x
			key = keyWords.get(string)
			if key != None:
				tokensList.append(key+'('+string+')')
				string=''
		else:
			if string.isdigit():
				tokensList.append('int('+string+')')
			tokensList.append(x)
			string = ''

	return tokensList