"""
Gramatica de Backus-NaurForm para primer programa:
	<program> ::= <function>
	<function> ::= "int" <id> "(" ")" "{" <statement> "}"
	<statement> ::= "return" <exp> ";"
	<exp> ::= <int>
"""

def expresion(expresion):
	expresion.remove('semicolon')
	for position in range(0,len(expresion)):
		if expresion[position] == 'returnKeyWord':
			return(expresion[position+1][6:len(expresion[position+1])-1])

def function(function):
	function.remove('openParentesis')
	function.remove('closeParentesis')
	for position in range(0,len(function)):
		if function[position].find('id') != -1:
			print(function[position].replace('id<','').rstrip('>') + expresion(function[position+2:function.index('closeBrace')]))

def parcer(_tokens):
	"""tokens = ['openParentesis','closeParentesis','openBrace',
			  'closeBrace','semicolon','intKeyWord','returnKeyWord',
			  'id','const']
	#funcion = int id ( ) { statement }
	if _tokens[0] == tokens[5]:
		if _tokens[1].find(tokens[7]) != -1 and _tokens[2].find(tokens[0]) != -1 and _tokens[3].find(tokens[1]) != -1 and _tokens[4].find(tokens[2]) != -1:
			name_function = _tokens[1][3:len(_tokens[1])-1]
	print(_tokens)"""
	for token in range(0,len(_tokens)):
		if _tokens[token] == 'intKeyWord':
			function(_tokens[token+1:_tokens.index('closeBrace')+1])