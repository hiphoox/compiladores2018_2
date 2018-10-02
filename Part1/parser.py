import re
import os

from c_classes import *

from lex_function import lex

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

def iterate(l):
    for i in l:
        if type(i) == list:
            iterate(i)
        else:
            if isinstance(i, Int_kw):
                int_kw = i.kw
                print("FUN RETURN TYPE: "+str(int_kw))
            elif isinstance(i, Id_kw):
                id_kw = i.id
                print("\t FUN NAME: "+str(id_kw))
            elif isinstance(i, Ret_kw):
                ret = i.kw
                print("\t\t FUN BODY:")
                print("\t\t\t"+str(ret)+" ", end='')
            elif isinstance(i, Literal_num):
                n = i.num
                print(str(n), end='')
            

def generate(ast):
    print("----Pretty AST----")
    iterate(ast)

generate(parse(lex()))