import re

#Realiza la busqueda del simbolo correspondiente
def simbols(code_section):
	if code_section == '(':
		return 'openParentesis'
	if code_section == ')':
		return 'closeParentesis'
	if code_section == '{':
		return 'openBrace'
	if code_section == '}':
		return 'closeBrace'
	if code_section == ';':
		return 'semiColon'

#Realiza la busqueda del keyWord correspondiente
def keyWords(code_section):
	if code_section == 'int':
		return 'intKeyWord'
	if code_section == 'return':
		return 'returnKeyWord'

#Clase contenedora de un entero
class Integer:
	def __init__(self, code_section):
		self.int = int(code_section)

#Clase contenedora de un identificador
class Identifier:
	def __init__(self, code_section):
		self.id = code_section


def lex(fileName):
	code = '#'.join((open(fileName, "r").read().split()))

	simbol = re.compile('\(|\)|\{|\}|\;')
	keyWordd = re.compile('int|return')
	identifierd = re.compile('main')
	integers = re.compile('(\d)+')

	string = ''
	tokensList = []
	#for que itera en cada uno de los elementos de la cadena 'code'.
	for x in range(0,len(code)):
		if code[x]!='#':
			key = simbol.search(code[x])
			if not key:
				string += code[x]
				#Realiza una busqueda dentro de keyWords e indentifiers
				identifier = identifierd.search(string)
				keyWord = keyWordd.search(string)
				if identifier != None:
					tokensList.append(Identifier(string))
					string=''
				elif keyWord != None and code[x+1]=='#':
					tokensList.append(keyWords(keyWord.group(0)))
					string=''
				elif keyWord != None or identifier != None and code[x+1]!='#':
					return False
			else:
				"""Comprobamos que lo anterior sea un numero, de no serlo significara que no se encuentra definido
				dentro de ningun diccionario y en consecuencia debera mandar un error lexico"""
				if string.isdigit():
					tokensList.append(Integer(string))
				elif string != '':
					return False
				tokensList.append(simbols(code[x]))
				string = ''
	return tokensList