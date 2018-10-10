from tokenizerV2 import tokenizerV2
from parser import parser
#from genCodigo import x

pruebaV = ['multi_digit.c', 'newlines.c', 'no_newlines.c', 'return0.c', 'return2.c', 'spaces.c']
pruebaI = ['missing_paren.c', 'missing_retval.c', 'no_semicolon.c', 'no_space.c', 'wrong_case.c']

print ("\t----------- Pruebas validas -----------")
for i in pruebaV:
    print ('\n'+i)
    tokens = tokenizerV2(i)
    print(tokens)
    ast,programa = parser(tokens)
    if (len(programa) != 0):
    	print(programa)
    	#x(programa)
    else:
    	print ("Compilacion no exitosa")

print ("\t----------- Pruebas invalidas -----------")
for i in pruebaI:
    print ('\n'+i)
    tokens = tokenizerV2(i)
    print(tokens)
    ast,programa = parser(tokens)
    if (len(programa) != 0):
    	print(programa)
    	#x(programa)
    else:
    	print ("Compilacion no exitosa")
