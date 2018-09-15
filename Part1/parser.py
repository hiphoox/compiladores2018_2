import re
import os
from lex_function import lex

def expression(ret):
    num=[]
    for l in ret:
        numero_searched=re.search(r'INT<[0-9]+>',l)
        if(numero_searched):
            numero=re.search(r'[0-9]+',numero_searched.group(0))
            if(numero):
                num.append(numero.group(0))
            return num

def statement(tokens):
    stat=[]
    for t in tokens:
        if(t=="RETURN"):
            stat.append(t)
            tokens.remove(t)
        else:
            stat.append(expression(t))
    return stat

def program(tokens):
    p=[]
    for t in tokens:
        if(t=="ID<main>"):
            p.append(t)
            tokens.remove(t)
        else:
            p.append(statement(tokens))
            break
    return p

def parse(tokens):
    ast=[]
    for t in tokens:
        if(t=="INT_ID<int>"):
            ast.append(t)
            tokens.remove(t)
        else:
            ast.append(program(tokens))
            break
    print(ast)
    return ast






parse(lex())