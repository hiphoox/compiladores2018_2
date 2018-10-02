'''Autor: Ramos Estrada Gerardo
Descricion: Este programa genera el AST recibiendo como parametro la 
lista de tokens que manda el scanner'''

from scanner import scanner

def parser(tokens):
    ast=[[],[],[]]
    ast = function(tokens, ast)
    ast= ["PROGRAM", ast, []]
    return ast

def function(tokens, ast):
    for iterador in range(0, len(tokens)):
        if tokens[0] == 'INTKEYWORD' or tokens[0] == 'ID' or tokens[0] == 'OPENPARE' or tokens[0] == 'CLOSEPARE' or tokens[0] == 'OPENBRACE':
            tokens.remove(tokens[0])
        elif tokens[0] == "RETURNKEYWORD":
            ast = statement(tokens, ast)
        elif tokens[0] == "CLOSEBRACE":
            tokens.remove(tokens[0])
            ast = ["MAIN", ast, []]
            break
        else:
            print('Error')
            break
    return ast
    
def statement(tokens, ast):
    for iterador in range(0, len(tokens)):
        if tokens[0] == "RETURNKEYWORD":
            tokens.remove(tokens[0])
        elif tokens[0].isdigit():
            ast = exp(tokens, ast)
        elif tokens[0] == "SEMICOLON":
            tokens.remove(tokens[0])
            ast = ["RETURN", ast, []]
            break
        else:
            print('Error')
            break
    return ast
        
def exp(tokens, ast):
    for iterador in range(0, len(tokens)):
        if tokens[0].isdigit():
            ast.pop(0)
            ast.insert(0,int(tokens[0]))
            tokens.remove(tokens[0])
            break
        else:
            print("Error")
            break
    return ast
