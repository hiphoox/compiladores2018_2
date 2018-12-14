from pruebaPar import parser
from tokenizerV2 import tokenizerV2
from genCodigo import x

pruebaV = ['multi_digit.c', 'newlines.c', 'no_newlines.c', 'return0.c', 'return2.c', 'spaces.c']
pruebaI = ['missing_paren.c', 'missing_retval.c', 'no_semicolon.c', 'no_space.c', 'wrong_case.c']

print ("\t----------- Pruebas validas -----------")
for i in pruebaV:
    print ("------------- DIVISION ENTRE PRUEBAS -------------")
    print ('\n'+i)
    tokens = tokenizerV2(i)
    print(tokens)
    ast,programa = parser(tokens)
    
    if (len(programa) != 0):
        print(programa)
        asm = x(programa)
        print ("Compilacion realizada exitosamente\n\n SU CODIGO ENSAMBLADOR QUEDA DE LA SIGUIENTE FORMA: \n\n")
        print(asm)
    else:
        print ("Compilacion no exitosa")

print ("\t----------- Pruebas invalidas -----------")
for i in pruebaI:
    print ("------------- DIVISION ENTRE PRUEBAS -------------")
    print ('\n'+i)
    tokens = tokenizerV2(i)
    print(tokens)
    ast,programa = parser(tokens)
    
    if (len(programa) != 0):
        print(programa)
        asm = x(programa)
        print ("Compilacion realizada exitosamente\n\n SU CODIGO ENSAMBLADOR QUEDA DE LA SIGUIENTE FORMA: \n\n")
        print(asm)
    else:
        print ("Compilacion no exitosa")
