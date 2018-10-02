'''Autor: Ramos Estrada Gerardo
Descricion: Este programa genera el archivo ensamblador recibiendo como
parametro un AST'''

aux=[]
from scanner import scanner
from parser import parser

def hijoDerecho(arbol):
    return arbol[2]

def hijoIzquierdo(arbol):
    return arbol[1]
    
def postOrden(arbol):    
    if len(arbol) != 0:
        postOrden(hijoIzquierdo(arbol))
        postOrden(hijoDerecho(arbol))
        aux.append(arbol[0])
        
def generation(ast):
    postOrden(ast)
    archivo=open("retun_2.asm","w")
    archivo.write(".globl _"+aux[2]+"\n")
    archivo.write("_"+aux[2]+":"+"\n")
    archivo.write("movl    $"+str(aux[0])+", %eax"+"\n")
    archivo.write("ret")
    archivo.close()
    
generation(parser(scanner()))
