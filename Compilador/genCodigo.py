def listaRetorno (lista, bandera):
    #print (lista)
    e1, e2 , ex, instruccion = '', '', '', ''
    for i in lista:
        if (str(type(i)).find("list") != -1):
            if (bandera == 1):
                ex, bandera = listaRetorno(i, 0)
                e1 = e1[:e1.find("\n\tpush")]
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
            elif (i in ['+', '-', '*', '/', '~', '!', ]):
                pass
            else:
                print("INVALIDO")
                instruccion = "INVALIDO"
                break
        else:
            print ("INVALIDO")
            instruccion = "INVALIDO"
            break
        #instruccion = ex + e1 + e2
        #print (instruccion)
    return instruccion, bandera

def generadorASM(AST):
    #print (AST[0])
    #print (type(AST[0]))
    valRet = AST.pop(0)
    tipoRecibido = type(valRet)
    if (str(tipoRecibido).find("str") != -1):
        instruccionVRetorno = "\n\tmovl  $" + valRet[4:-1] + ", %eax"
        #print (instruccionVRetorno)
    elif (str(tipoRecibido).find("list") != -1):
        #print ("LISTA DE OPERACIONES")
        instruccionVRetorno, bandera = listaRetorno(valRet, 0)
        #print (instruccionVRetorno)
    else:
        instruccionVRetorno = "AST INVALIDO"
        return instruccionVRetorno
    
    if (instruccionVRetorno != 'INVALIDO'):
        #print ("RETURN VERIFICATION")
        if (AST.pop(0) == 'RETURN KEYWORD'):
            instruccionVRetorno = instruccionVRetorno + "\n\tret"
        else:
            instruccionVRetorno = "AST INCORRECTO"
            return instruccionVRetorno
    else:
        instruccionVRetorno = "AST INCORRECTO"
        return instruccionVRetorno
    
    if (len(AST) != 0):
        name = AST.pop(0)
        functionName = name[3:-1]
        instruccionVRetorno = "\t.globl _" + functionName + "\n_" + functionName + ":" + instruccionVRetorno
        if (len(AST) != 0):
            instruccionVRetorno = "AST INCORRECTO"
            return instruccionVRetorno
    else:
        instruccionVRetorno = "AST INCORRECTO"
        return instruccionVRetorno

    return instruccionVRetorno

    


def x(programa):
    if (len(programa) == 3):
        asm = generadorASM(programa)
        #print (asm)
    else:
        print("Programa no compilado")
        return ("AST INVALIDO")
    return asm
