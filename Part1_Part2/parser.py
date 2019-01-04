import re
import os

from c_classes import *

from lex_function import lex

def expression(tokens):
    num = []
    for t in tokens:
        if isinstance(t, Literal_num):
            num.append(t)
        elif isinstance(t, Negation):
            num.append(t)
        elif isinstance(t, BitwiseComplement):
            num.append(t)
        elif isinstance(t, LogicalNegation):
            num.append(t)
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
            python_comp.close()
        else:
            if isinstance(i, Int_kw):
                int_kw = i.kw
                print("FUN RETURN TYPE: "+str(int_kw))
            elif isinstance(i, Id_kw):
                id_kw = i.id
                python_comp.write(' .globl _{}\n'.format(i.id))
                python_comp.write('_{}:\n'.format(i.id))
                print("\t FUN NAME: "+str(id_kw))
                python_comp.close()
            elif isinstance(i, Ret_kw):
                ret = i.kw
                print("\t\t FUN BODY:")
                print("\t\t\t"+str(ret)+" ", end='')
                leaf = l[l.index(i)+1]
                leaf.reverse()
                for t in leaf:
                    if isinstance(t, Literal_num):
                        n = t.num
                        python_comp = open("python_comp.s","a+")
                        python_comp.write(' movl  ${}, {}eax\n'.format(n, "%"))
                        python_comp.close()
                    elif isinstance(t, Negation):
                        python_comp = open("python_comp.s","a+")
                        python_comp.write(' neg {}eax\n'.format("%"))
                        python_comp.close()
                    elif isinstance(t, BitwiseComplement):
                        python_comp = open("python_comp.s","a+")
                        python_comp.write(' neg {}eax\n'.format("%"))
                        python_comp.close()
                    elif isinstance(t, LogicalNegation):
                        python_comp = open("python_comp.s","a+")
                        python_comp.write(' cmpl  $0, {}eax\n'.format("%"))
                        python_comp.write(' movl  $0, {}eax\n'.format("%"))
                        python_comp.write(' sete  {}al\n'.format("%"))
                        python_comp.close()
                python_comp = open("python_comp.s","a+")
                python_comp.write(' ret\n')
                python_comp.close()
                leaf.reverse()
                for t in leaf:
                    if isinstance(t, Literal_num):
                        n = t.num
                        print(str(n), end='')
                    elif isinstance(t, Negation):
                        n = t.neg
                        print(str(n), end='')
                    elif isinstance(t, BitwiseComplement):
                        n = t.comp
                        print(str(n), end='')
                    elif isinstance(t, LogicalNegation):
                        n = t.neg
                        print(str(n), end='')
                break
            else:
                print("Error: AST badly constructed")
                break
            

def generate(ast):
    print("----Pretty AST----")
    iterate(ast)
    os.system('gcc python_comp.s -o out')
    os.remove("python_comp.s")
    print("\n\n\n==========NOTA==================>Ejecute los siguientes comandos para ver el resultado del compilador: \n1: ./out \n2: echo $?")

generate(parse(lex()))