'''Autor: Ramos Estrada Gerardo
Descricion: Este programa genera el AST recibiendo como parametro la 
lista de tokens que manda el scanner'''

import sys
import re
import Lexer

def buscaOp(lista):
    operadores=[]
    for i in lista:
        if i.startswith("Nega"):
            operadores.append(i)
        elif i.startswith("Add"):
            operadores.append(i)
        elif i.startswith("Mult"):
            operadores.append(i)
        elif i.startswith("Div"):
            operadores.append(i)
    return operadores

def encontrarConstante(tkns, ast):
    if ast == [[], [], []]: 
        for i in tkns:
            if i.startswith("Const"):
                aux=constante(i)
                ast=[aux, [], []]
                return ast
    else: 
        for i in tkns:
            if i.startswith("Const"):
                aux=constante(i)
                if len(ast[1]) == 0:
                    ast.pop(1)
                    ast.insert(1, aux)
                else:
                    ast.pop(2)
                    ast.insert(2, aux)
                    return ast

def constante(programa):
    expresion=re.compile('\d+')
    num=expresion.findall(programa)
    return num[0]

def factor(tokenLista,ast,pila):
    if tokenLista[0].startswith("Constant"):
        ast=encontrarConstante(tokenLista,ast)
        tokenLista.pop(0)
        tokenLista.pop(0)
    return ast
         
def term(tokenLista,ast,pila):
    operadores=[]
    if tokenLista[0].startswith("Constant") and (tokenLista[1] == "Multiplication" or tokenLista[1] == "Division"):
        operadores=buscaOp(tokenLista)
        if len(operadores) > 1:#Hay mas operadores
            mas=operadores.count("Multiplication")
            menos=operadores.count("Division")
            if mas > 1 or menos > 1:#asociatividad
                ast.pop(0)
                ast.insert(0,tokenLista[1])
                tokenLista.pop(1)
                ast=factor(tokenLista,ast,pila)
                aux=constante(tokenLista[1])
                ast=[tokenLista[0], ast, aux]
                tokenLista.pop(0)
                tokenLista.pop(0)
            else:
                if operadores[0] == "Multiplication":
                    ast.pop(0)
                    ast.insert(0,tokenLista[1])
                    tokenLista.pop(1)
                    ast=factor(tokenLista,ast,pila)
                    aux=constante(tokenLista[1])
                    ast=[tokenLista[0], ast, aux]
                    tokenLista.pop(0)
                    tokenLista.pop(0)
                else:
                    ast.pop(0)
                    ast.insert(0,tokenLista[3])
                    tokenLista.pop(3)
                    nueva=[tokenLista[2], tokenLista[3]]
                    tokenLista.pop(2)
                    tokenLista.pop(2)
                    ast=factor(nueva,ast,pila)
                    aux=constante(tokenLista[0])
                    ast=[tokenLista[1], aux, ast]
                    tokenLista.pop(0)
                    tokenLista.pop(0)
        else:#Si no hay mas operadores
            ast.pop(0)
            ast.insert(0,tokenLista[1])
            tokenLista.pop(1)
            ast=factor(tokenLista, ast, pila) 
    else:
        ast=factor(tokenLista, ast, pila)
    return ast
    
def unary_op(tokenLista,ast,pila):
    if tokenLista[0] == "Semicolon":
        return []    
    else:
        if tokenLista[0] == "Negation":
            ast=["Negation", ast, []]
            tokenLista.pop(0)
        elif tokenLista[0] == "BitwiseComplement":
            ast = ["BitwiseComplement", ast, []]
            tokenLista.pop(0)
        elif tokenLista[0] == "LogicalNegation":
            ast=["LogicalNegation", ast, []]
            tokenLista.pop(0)
        elif tokenLista[0].startswith("Const"):
            tokenLista.pop(0)
    unary_op(tokenLista,ast,pila)
    return ast

def exp(tokenLista, ast, pila):
    operadores=[]
    if (tokenLista[0].startswith("Negation") or 
        tokenLista[0].startswith("BitwiseComplement") or 
        tokenLista[0].startswith("LogicalNegation")):
        ast=encontrarConstante(tokenLista,ast)
        ast=unary_op(tokenLista,ast,pila)
        tokenLista.pop(0)
    elif tokenLista[0].startswith("Constant") and (tokenLista[1] == "Addition" or tokenLista[1] == "Negation"):
        operadores=buscaOp(tokenLista)
        if len(operadores) > 1:#Hay mas operadores
            mas=operadores.count("Addition")
            menos=operadores.count("Negation")
            if mas > 1 or menos > 1:#asociatividad
                ast.pop(0)
                ast.insert(0,tokenLista[1])
                tokenLista.pop(1)
                ast=term(tokenLista,ast,pila)
                aux=constante(tokenLista[1])
                ast=[tokenLista[0], ast, aux]
                tokenLista.pop(0)
                tokenLista.pop(0)
            else:
                if operadores[0] == "Addition" and operadores[1] != "Multiplication":
                    ast.pop(0)
                    ast.insert(0,tokenLista[1])
                    tokenLista.pop(1)
                    ast=term(tokenLista,ast,pila)
                    aux=constante(tokenLista[1])
                    ast=[tokenLista[0], ast, aux]
                    tokenLista.pop(0)
                    tokenLista.pop(0)
                else:
                    ast.pop(0)
                    ast.insert(0,tokenLista[3])
                    tokenLista.pop(3)
                    nueva=[tokenLista[2], tokenLista[3]]
                    tokenLista.pop(2)
                    tokenLista.pop(2)
                    ast=term(nueva,ast,pila)
                    aux=constante(tokenLista[0])
                    ast=[tokenLista[1], aux, ast]
                    tokenLista.pop(0)
                    tokenLista.pop(0)
        else:#Si no hay mas operadores
            ast.pop(0)
            ast.insert(0,tokenLista[1])
            tokenLista.pop(1)
            ast=term(tokenLista, ast, pila)     
    else:
        ast=term(tokenLista, ast, pila)
    return ast
        
def statement(tokenLista, ast, pila):
    for iterador in range(0, len(tokenLista)):
        if tokenLista[0] == "ReturnKeyword":
            tokenLista.pop(0)
            pila.append("ReturnKeyword")
            ast=exp(tokenLista, ast, pila)
        elif tokenLista[0] == "Semicolon":
            tokenLista.pop(0)
            ast = ["RETURN", ast, []]
            break
    return ast
        
def function(tokenLista, ast, pila):
    contador=0
    for iterador in range(0, len(tokenLista)):
        if tokenLista[0] == "Int":
            tokenLista.pop(0)
            pila.append("Int")
        elif tokenLista[0] == "ID: main" and pila[contador]=="Int":
            tokenLista.pop(0)
            pila.append("ID: main")
            contador+=1
        elif tokenLista[0] == "OpenPare" and pila[contador]=="ID: main":
            tokenLista.pop(0)
            pila.append("OpenPare")
            contador+=1
        elif tokenLista[0] == "ClosePare" and pila[contador]=="OpenPare":
            tokenLista.pop(0)
            pila.append("ClosePare")
            contador+=1
        elif tokenLista[0] == "OpenBrace" and pila[contador]=="ClosePare":
            tokenLista.pop(0)
            pila.append("OpenBrace")
            contador+=1
            ast=statement(tokenLista, ast, pila)
            if tokenLista[0] == "CloseBrace":
                tokenLista.pop(0)
                ast = ["MAIN", ast, []]
                break
        else:
            print("Error")
            sys.exit()
    return ast

def parser(tokenLista):
    if tokenLista != []:
        pila=[]
        ast=[[],[],[]]
        ast = function(tokenLista, ast, pila)
        if ast != [[],[],[]]: 
            ast= ["PROGRAM", ast, []]
            print(ast)
        else:
            print("Error")
    else:
        print("Error: no se encuentran los tokens")
