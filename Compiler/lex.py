import re
from wrappers import Operator
from wrappers import Integer
from wrappers import Identifier
from wrappers import simbols
from wrappers import keyWords
from wrappers import operators

#Funcion principal que se encarga de identificar los tokens del codigo
def lexer(line, tokensList):
	if line != '':
		simbol = re.compile('\(|\)|\{|\}|\;')
		operator = re.compile('\+|\-|\~|\!|\*|\/')
		keyWordd = re.compile('int\\b|return\\b')
		identifier = re.compile('[a-zA-Z]\w*')
		integers = re.compile('[0-9]+')

		token = simbol.search(line)
		if token and token.start() == 0:
			line = line.replace(token.group(),'',1).lstrip()
			tokensList.append(simbols(token.group()))
		token = operator.search(line)
		if token and token.start() == 0:
			line = line.replace(token.group(),'',1).lstrip()
			tokensList.append(Operator(token.group()))
		token = keyWordd.search(line)
		if token and token.start() == 0:
			line = line.replace(token.group(),'',1).lstrip()
			tokensList.append(keyWords(token.group()))
		token = identifier.search(line)
		if token and token.start() == 0:
			line = line.replace(token.group(),'',1).lstrip()
			tokensList.append(Identifier(token.group()))
		token = integers.match(line)
		if token and token.start() == 0:
			line = line.replace(token.group(),'',1).lstrip()
			tokensList.append(Integer(token.group()))
		lexer(line, tokensList)

def funcLeeArchivo(fileName):
	code = re.split('\n',open(fileName, "r").read())
	tokensList = []
	linea = 1

	for line in code:
		lexer(line.lstrip(), tokensList)
		linea += 1

	return tokensList