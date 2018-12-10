import re

# (1) -> La funcion realiza lo que debe de manera natural.
# (0) -> La funcion realiza lo que debe pero no de manera natual.

#Realiza la busqueda del simbolo correspondiente (1)
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
	if code_section == '-':
		return 'nagation'
	if code_section == '!':
		return 'logicalNegation'
	if code_section == '~':
		return 'bitwiseComplement'

#Realiza la busqueda del keyWord correspondiente (1)
def keyWords(code_section):
	if code_section == 'int':
		return 'intKeyWord'
	if code_section == 'return':
		return 'returnKeyWord'

#Clase contenedora de un entero (1)
class Integer:
	def __init__(self, code_section):
		self.int = int(code_section)

#Clase contenedora de un identificador (1)
class Identifier:
	def __init__(self, code_section):
		self.id = code_section


#Pese a que el lexer ya realiza todo como deberia, pensar en algun algoritmo
#que realize los mismo paso, pero de manera natural (0)
#NOTA: Preguntar al profe sobre la duda del error del archivo 'no_space.c'
#OTRA NOTA: En caso de axistir un error, no terminar el programa, seguir con la ejecucion del mismo,
#al termino del analizador lexico debo regresar el el numero de errores y su linea.
def lex(fileName):
	#Recordar que C no reconoce UNICODE
	code = open(fileName, "r")
	line = code.readline()
	lineNumber = 1
	simbol = re.compile('\(|\)|\{|\}|\;')
	keyWord = re.compile('int$|return$') #Delimitar las expresiones regulares con simbolos
	identifierd = re.compile('main')
	integers = re.compile('^[0-9]+')

	string = ''
	tokensList = []

	while line:
		#print('line {}: {}'.format(lineNumber, ' '.join(line.split())))
		line = line.split()
		for item in line:
			for char in item:
				key = simbol.search(char)
				if key:
					tokensList.append(simbols(char))
				else:
					string += char
					key = keyWord.search(string)
					if key:
						tokensList.append(keyWords(string))
						string = ''
					else:
						key = identifierd.search(string)
						if key:
							tokensList.append(Identifier(string))
							string = ''
						else:
							key = integers.search(string)
							if key:
								tokensList.append(Integer(string))
								string = ''
		line = code.readline()
		lineNumber += 1

	return tokensList