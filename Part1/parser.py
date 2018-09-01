import re
import os
from lex_function import lex

def expression(ret):
    num=[]
    for l in ret:
        numero_searched=re.search(r'[0-9]+',l)
        if(numero_searched):
            num.append(numero_searched.group(0))
            return num

def statement(tokens):
    stat=[]
    for t in tokens:
        numero_searched=re.search(r'INT<[0-9]+>',t)
        if(numero_searched):
            stat.append(expression(numero_searched.group(0)))
            tokens.remove(t)
    return stat

def program(tokens):
    p=[]
    for t in tokens:
        if(t=="INT_ID<int>"):
            p.append(t)
            tokens.remove(t)
        elif(t=="ID<main>"):
            p.append(t)
            tokens.remove(t)
        else:
            p.append(statement(tokens))
    return p

def parse(tokens):
    ast=[]
    ast.append(program(tokens))
    print(ast)
    return ast






parse(lex())