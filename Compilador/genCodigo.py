import os

def listaRetorno (lista, bandera):
    #print (lista)
    e1, e2 , ex, instruccion = '', '', '', ''
    for i in lista:
        if (str(type(i)).find("list") != -1):
            if (bandera == 1):
                ex, bandera = listaRetorno(i, 0)
                e1 = e1[:e1.find("\n\tpush")-1]
                #print (e1)
                ex = ex + "\n\tpush %eax\n\tpop %ecx" + e1 + "\n\taddl %ecx, %eax"
                bandera = 0
                instruccion = ex
            else:
                ex, bandera = listaRetorno(i, bandera)
                ex = ex + "\n\tpush %eax"
                bandera = 1
                instruccion = ex
            #print ("PRUEBA 2")
        elif (str(type(i)).find("str") != -1):
            if (i.find("INT") == 0 and bandera == 0):
                e1 = "\n\tmovl  $" + i[4:-1] + ", %eax\n\tpush %eax"
                bandera = 1
                instruccion = instruccion + e1
            elif (i.find("INT") == 0 and bandera == 1):
                e2 = "\n\tpop %ecx\n\tmovl  $" + i[4:-1] + ", %eax\n\taddl %ecx, %eax"
                bandera = 0
                instruccion = instruccion + e2
            else:
                break
        #instruccion = ex + e1 + e2
        #print (instruccion)
    return instruccion, bandera

def valorRetorno(AST):
    #print (AST[0])
    #print (type(AST[0]))
    valRet = AST.pop(0)
    tipoRecibido = type(valRet)
    if (str(tipoRecibido).find("str") != -1):
        instruccionVRetorno = "\n\tmovl  $" + valRet[4:-1] + ", %eax"
        print (instruccionVRetorno)
    elif (str(tipoRecibido).find("list") != -1):
        print ("LISTA DE OPERACIONES")
        instruccionVRetorno, bandera = listaRetorno(valRet, 0)
        print (instruccionVRetorno)
    else:
        print ("AST INVALIDO")
    #print (AST)
    return "blah   "

def x(programa):
    if (len(programa) == 3):
        resultado = valorRetorno(programa)
        print (resultado)
    else:
        print("Programa no compilado")
        return 
    return






prueba1 = ['INT<234>', 'RETURN KEYWORD', 'MAIN ID']
prueba2 = [['INT<1>', 'INT<2>', '+'], 'RETURN KEYWORD', 'MAIN ID']
prueba3 = [['INT<4>', ['INT<5>', 'INT<6>', '*'], '+'], 'RETURN KEYWORD', 'MAIN ID']
prueba4 = [[['INT<7>', 'INT<8>', '+'], 'INT<9>', '*'], 'RETURN KEYWORD', 'MAIN ID']
prueba5 = [[[['INT<1>', 'INT<2>', '+'], 'INT<3>', '*'], 'INT<4>', '-'], 'RETURN KEYWORD', 'MAIN ID']
x(prueba1)
x(prueba2)
x(prueba3)
x(prueba4)
x(prueba5)
