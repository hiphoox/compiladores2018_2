'''Autor: Ramos Estrada Gerardo
Descripcion: Este programa realiza la funcion de escanear un programa 
en lenguaje C y obtener los tokens para mandarlos al parser'''
from Token import tokenLista
import os.path
import re

def OpBinaria(programa, constantes, tkns):
    if programa.startswith(constantes[0]):
        tkns.append(tokenLista.Constant+constantes[0])
        return tkns
     
    
def sacarTokenComplejo(programa):
    if programa.startswith("return"):
        return programa[len("return"):len(programa)]
    elif programa.startswith("main"):
        return programa[len("main"):len(programa)]
    elif programa.startswith("int"):
        return programa[len("int"):len(programa)]
    elif programa[0].isdigit():
        aux=constante(programa)
        if len(aux) > 1:
            return programa[len(aux[0]):len(programa)]
        else:
            expresion=re.compile('\d+')
            programa=expresion.sub('',programa)
            return programa
    else:
        return []

def constante(programa):
    expresion=re.compile('\d+')
    num=expresion.findall(programa)
    return num
    '''if len(num) > 1:
        return num
    else:
        return num[0]'''

def tokenComplejo(programa, tkns):
    if programa.startswith("return"):
        tkns.append(tokenLista.ReturnKeyword)
        return tkns
    elif programa.startswith("main"):
        tkns.append(tokenLista.Id+"main")
        return tkns
    elif programa.startswith("int"):
        tkns.append(tokenLista.IntKeyword)
        return tkns
    elif programa[0].isdigit():
        const=constante(programa)
        if len(const) > 1:
            tkns=OpBinaria(programa, const, tkns)
            return tkns 
        else:
            tkns.append(tokenLista.Constant+const[0])
            return tkns
    else:
        return tkns

def recortar(cadena):
    return cadena[1:len(cadena)]

def encontrarTokens(tkns,programa):
    if programa == '':
        return []
    else:
        aux=programa[0]
        if aux == "{":
            resto=recortar(programa)
            tkns.append(tokenLista.OpenBrace)
        elif aux == "}":
            resto=recortar(programa)
            tkns.append(tokenLista.CloseBrace)
        elif aux == "(":
            resto=recortar(programa)
            tkns.append(tokenLista.OpenPare)
        elif aux == ")":
            resto=recortar(programa)
            tkns.append(tokenLista.ClosePare)
        elif aux == ";":
            resto=recortar(programa)
            tkns.append(tokenLista.Semicolon)
        elif aux == "-":
            resto=recortar(programa)
            tkns.append(tokenLista.Negation)
        elif aux == "~":
            resto=recortar(programa)
            tkns.append(tokenLista.BitwiseComplement)
        elif aux == "!":
            resto=recortar(programa)
            tkns.append(tokenLista.LogicalNegation)
        elif aux == "+":
            resto=recortar(programa)
            tkns.append(tokenLista.Addition)
        elif aux == "*":
            resto=recortar(programa)
            tkns.append(tokenLista.Multiplication)
        elif aux == "/":
            resto=recortar(programa)
            tkns.append(tokenLista.Division)
        else:
            tkns=tokenComplejo(programa, tkns)
            resto=sacarTokenComplejo(programa)
    encontrarTokens(tkns, resto)
    return tkns

def juntar(programa):
    expresion=re.compile('\s+')
    lineaCompleta=''
    for linea in programa:
        linea=linea.strip(" ")
        linea=expresion.sub('',linea)
        lineaCompleta=lineaCompleta+linea
    return lineaCompleta

def Lex(programa):
    tkns=[]
    if os.path.isfile(programa):
        archivo=open(programa,"r")
        archivo=juntar(archivo)
        tkns=encontrarTokens(tkns, archivo)
        print(tkns)
    else:
        print("El archivo no se encuentra")
