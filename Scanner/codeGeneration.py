'''Autor: Ramos Estrada Gerardo
Descricion: Este programa genera el archivo ensamblador recibiendo como
parametro un AST'''
import parser

def contarConstantes(pila):
    aux=[]
    for iterador in pila:
        if iterador.isdigit():
            aux.append(iterador)
    return len(aux)

def hijoDerecho(arbol):
    return arbol[2]

def hijoIzquierdo(arbol):
    return arbol[1]
    
def postOrden(arbol, aux):  
    if len(arbol) > 1:
        postOrden(hijoIzquierdo(arbol), aux)
        if arbol[1] != [] and len(arbol[1]) != 3:
            aux.append(arbol[1])
        postOrden(hijoDerecho(arbol), aux)
        if arbol[2] != [] and len(arbol[2]) != 3:
            aux.append(arbol[2])
        aux.append(arbol[0])
    return aux

def OperadorUn(lista, archivo):
    num=contarConstantes(lista)
    if num == 1:
        for iterador in lista:
            if iterador == "Negation":
                archivo.write("neg    %eax"+"\n")
            elif iterador == "BitwiseComplement":
                archivo.write("neg    %eax"+"\n")
            elif iterador == "LogicalNegation":
                archivo.write("cmpl   $0, %eax"+"\n")
                archivo.write("movl   $0, %eax"+"\n")
                archivo.write("sete   %al"+"\n")

def ret(aux, archivo):
    for iterador in aux:
        if iterador == "RETURN":
            archivo.write("ret")

def constante(pila, archivo):
    aux=[]
    for iterador in pila:
        if iterador.isdigit():
            aux.append(iterador)
    if len(aux) > 1:
        for iterador in pila:
            if iterador == "Negation":
                archivo.write("movl    $"+aux[0]+", %eax"+"\n")
                archivo.write("movl    $"+aux[1]+", %ecx"+"\n")
                archivo.write("sub    $eax, ecx"+"\n")
                break
            elif iterador == "Addition":
                archivo.write("movl    $"+aux[0]+", %eax"+"\n")
                archivo.write("movl    $"+aux[1]+", %ecx"+"\n")
                archivo.write("add    $eax, ecx"+"\n")
                break
            elif iterador == "Multiplication":
                archivo.write("movl    $"+aux[0]+", %eax"+"\n")
                archivo.write("movl    $"+aux[1]+", %ecx"+"\n")
                archivo.write("imul    $eax, ecx"+"\n")
                break
            elif iterador == "Division":
                archivo.write("movl    $"+aux[0]+", %eax"+"\n")
                archivo.write("movl    $"+aux[1]+", %ecx"+"\n")
                archivo.write("idiv    $ecx"+"\n")
                break
    else:
        archivo.write("movl    $"+aux[0]+", %eax"+"\n")

def globalMain(aux, archivo):
    for iterador in aux:
        if iterador == "MAIN":
            archivo.write(".globl _MAIN"+"\n")
            archivo.write("_MAIN:"+"\n")
    
def generation(ast):
    aux=[] 
    if ast != [[], [], []]:
        aux = postOrden(ast,aux)
        archivo=open("retun_2.txt","w")
        globalMain(aux, archivo)
        constante(aux, archivo)
        OperadorUn(aux, archivo)
        ret(aux, archivo)
        archivo.close()
    else:
        print("Arbol no encontrado")
    
generation(parser(Lexer()))
