from tokenizer import *

"""
<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <unary_op> <exp> | <int>
<unary_op> ::= "!" | "~" | "-"
"""

def unOp(tokens):    
    un = []
    print(tokens)
    for i in tokens:
        l=i.split(":")
        if l[1] == "-" or l[1] == "~" or l[1] == "!":
            un.append(l[1])
            print(un)
            return un
    

def expresion(tokens):
    exp = []
    for i in tokens:
        l=i.split(":")
        if l[0] ==  "INT":
            exp.append(l[1])
            tokens.remove(i)
        elif l[0] == "Negation" or l[0] == "Bitwise" or l[0] == "Logic_Neg":
            exp.append(unOp(tokens))

       # elif l[0] == "!" or "~" or "-":
            
    return exp

def statement(tokens):
    sta = []
    for i in tokens:
        l=i.split(":")
        if l[0] ==  "Keyword" and l[1] == "return":
            sta.append(l[1])
            sta.append(expresion(tokens))
        elif l[0] ==  "Semicolon":
            sta.append(l[1])
            pass
    return sta

def func(tokens):
    aidi = []
    for i in tokens:
        l=i.split(":")
        if l[0] ==  "ID":
            aidi.append(l[1])
        elif l[0] ==  "OpenParen":
            aidi.append(l[1])
            pass
        elif l[0] ==  "CloseParen":
            aidi.append(l[1])
            pass
        elif l[0] ==  "OpenBrace":
            aidi.append(l[1])
            aidi.append(statement(tokens))
            pass
        elif l[0] ==  "CloseBrace":
            aidi.append(l[1])
            pass
    return aidi

def programa(tokens):
    fun = []
    for i in tokens:
        l=i.split(":")
        if l[0] ==  "Keyword" and l[1] == "int":
            fun.append(l[1])
            tokens.remove(i)
        else:
            fun.append(func(tokens))
            break
    return fun        



def parser(tokens):
    ast=programa(tokens)
    return ast




    
print(parser(tokenizer('tarea1.c')))