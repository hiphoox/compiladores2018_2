from tokenizerV2 import tokenizerV2		# Importamos nuestra función del tokenizer
from parser import parser				# Importamos la función principal del parser

# Lista con el nombre de los archivos que se deben compilar correctamente
pruebaV = ['multi_digit.c', 'newlines.c', 'no_newlines.c', 'return0.c', 'return2.c', 'spaces.c']

# Lista con el nombre de los archivos que se deben compilar incorrectamente
pruebaI = ['missing_paren.c', 'missing_retval.c', 'no_semicolon.c', 'no_space.c', 'wrong_case.c', 'no_brace.c']


print ("\t----------- Pruebas validas -----------")
for i in pruebaV:	# Iteramos en la lista de nombres y vamos probando uno por uno
	print ('\n'+i)
	tokens = tokenizerV2(i)
	print(tokens)
	ast = parser(tokens)
	print(ast)

print ("\t----------- Pruebas invalidas -----------")
for i in pruebaI:	# Iteramos en la lista de nombres y vamos probando uno por uno
	print ('\n'+i)
	tokens = tokenizerV2(i)
	print(tokens)
	ast = parser(tokens)
	print(ast)