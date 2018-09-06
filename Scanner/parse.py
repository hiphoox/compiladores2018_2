'''Autor: Ramos Estrada Gerardo
Descricion: Este programa genera el AST recibiendo como parametro la 
lista de tokens que manda el scanner'''

import re

def parser(tokens):
    ast=insertar("programa") 
    function(tokens, ast)
    statement(tokens, ast)
    exp(tokens, ast)
    return ast

def insertar(r):
    return [r, [], []]
    
def function(tkn, ast):
    if "INT" in tkn and "Opare" in tkn and "CPare" in tkn and "Obrace" in tkn and "Cbrace" in tkn:
        ast.pop(1)
        ast.insert(1, ["MAIN", [], []])
    else:
        print("Error")

def statement(tkn, ast):
    if "RETURN" in tkn:
        ast[1].pop(1)
        ast[1].insert(1,["RETURN", [], []])
    else:
        print("Error")

def exp(tkn, ast):
    patron4=re.compile('(ID<[0-9]>)')
    for iterador in tkn:        
        id=patron4.findall(iterador)
        if len(id) != 0:
            ast[1][1].pop(1)
            ast[1][1].insert(1,[int(id[0][3]), [], []])
