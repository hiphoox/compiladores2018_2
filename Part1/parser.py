import re
import os

from c_classes import *

from lex_function import lex

class Node:
    def __init__(self, value, parent, son ):
        self.value = value
        self.parent = parent
        self.son = son

def expression(tokens):
    num=[]
    for t in tokens:
        if  isinstance(t, Literal_num):
            num.append(t)
            break
    return num

def statement(tokens):
    stat=[]
    for t in tokens:
        if  isinstance(t, Ret_kw):
            stat.append(t)
            tokens.remove(t)
            stat.append(expression(tokens))
        elif isinstance(t, Semicolon):
            tokens.remove(t)
    return stat

def program(tokens):
    p=[]
    for t in tokens:
        if isinstance(t, Id_kw):
            p.append(t)
            tokens.remove(t)
        elif isinstance(t, Open_paren):
            tokens.remove(t)
        elif isinstance(t, Close_paren):
            tokens.remove(t)
        elif isinstance(t, Open_brace):
            tokens.remove(t)
        elif isinstance(t, Close_brace):
            tokens.remove(t)
        else:
            p.append(statement(tokens))
            break
    return p

def parse(tokens):
    ast=[]
    for t in tokens:
        if isinstance(t, Int_kw):
            ast.append(t)
            tokens.remove(t)
        else:
            ast.append(program(tokens))
            break
    
    print("----- AST -----")
    print(ast)
    print()
    return ast

parse(lex())