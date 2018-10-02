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
    python_comp = open("python_comp.s","a+")
    for i in l:
        if type(i) == list:
            iterate(i)
        else:
            if isinstance(i, Int_kw):
                int_kw = i.kw
                print("FUN RETURN TYPE: "+str(int_kw))
            elif isinstance(i, Id_kw):
                id_kw = i.id
                python_comp.write(' .globl _{}\n'.format(i.id))
                python_comp.write('_{}:\n'.format(i.id))
                print("\t FUN NAME: "+str(id_kw))
            elif isinstance(i, Ret_kw):
                ret = i.kw
                print("\t\t FUN BODY:")
                print("\t\t\t"+str(ret)+" ", end='')
                if isinstance(l[l.index(i)+1][0], Literal_num):
                    n = l[l.index(i)+1][0].num
                    python_comp.write(' movl  ${}, {}eax\n'.format(n, "%"))
                    python_comp.write('  ret\n')
                    print(str(n), end='')
                    break
            else:
                print("Error: AST badly constructed")
                break
    python_comp.close()
            

def generate(ast):
    print("----Pretty AST----")
    iterate(ast)
    f = open("python_comp.s","r")
    f_lines = f.readlines()
    assem=  open("c_program.s","w")
    f.close()
    assem.close()

generate(parse(lex()))