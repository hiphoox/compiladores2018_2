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
    l=tokens.pop(0).split(":")
    if l[1] == "-" or l[1] == "~" or l[1] == "!":
        un.append(l[1])
        un.append(expresion(tokens))
        return un
    

def expresion(tokens):
    exp = []
    print(tokens)
    l=tokens[0].split(":")
    if l[0] ==  "INT":
        exp.append(l[1])
        tokens.pop(0)
    else:
        exp.append(unOp(tokens))            
    return exp

def statement(tokens):
    sta = []
    l=tokens.pop(0).split(":")
    if l[0] ==  "Keyword" and l[1] == "return":
        sta.append(l[1])
        sta.append(expresion(tokens))
    l=tokens.pop(0).split(":")
    if l[0] ==  "Semicolon":
        sta.append(l[1])
    return sta
    

def func(tokens):
    aidi = []
    l=tokens.pop(0).split(":")
    if l[0] ==  "ID":
        aidi.append(l[1])
    l=tokens.pop(0).split(":")
    if l[0] ==  "OpenParen":
        aidi.append(l[1])
    l=tokens.pop(0).split(":")
    if l[0] ==  "CloseParen":
        aidi.append(l[1])
    l=tokens.pop(0).split(":")
    if l[0] ==  "OpenBrace":
        aidi.append(l[1])
        aidi.append(statement(tokens))
    l=tokens.pop(0).split(":")
    if l[0] ==  "CloseBrace":
        aidi.append(l[1])
    return aidi
    

def programa(tokens):
    fun = []
    l=tokens.pop(0).split(":")
    if l[0] ==  "Keyword" and l[1] == "int":
        fun.append(l[1])
        fun.append(func(tokens))
    return fun      



def parser(tokens):
    ast=programa(tokens)
    return ast




    
print(parser(tokenizer('tarea1.c')))