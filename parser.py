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
    l=tokens.pop(0).split(":")
    if l[1] == "-" or l[1] == "~" or l[1] == "!":
        un.append(l[1])
        un.append(expresion(tokens))
        return un
    

def expresion(tokens):
    exp = []
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
        g=tokens[0].split(":")
        if g[1] == ";":
            return "Error: no hay valor de retorno"
        else:
            sta.append(l[1])
            sta.append(expresion(tokens))
    l=tokens[0].split(":")
    if l[0] ==  "Semicolon":
        tokens.pop(0)
    return sta
    

def func(tokens):
    aidi = []
    l=tokens.pop(0).split(":")
    if l[0] ==  "ID":
        aidi.append(l[1])
    l=tokens[0].split(":")
    if l[0] ==  "OpenParen":
        tokens.pop(0)
    l=tokens[0].split(":")    
    if l[0] ==  "CloseParen":
        tokens.pop(0)
    l=tokens[0].split(":")
    if l[0] ==  "OpenBrace":
        tokens.pop(0)
        aidi.append(statement(tokens))
    l=tokens[0].split(":")
    if l[0] ==  "CloseBrace":
        tokens.pop(0)
    return aidi
    

def programa(tokens):
    fun = []
    l=tokens.pop(0).split(":")
    if l[0] ==  "Keyword" and l[1] == "int":
        fun.append(l[1])
        fun.append(func(tokens))
    elif l[0] != "Keyword":
        return("Error en keyword")
    return fun      



def parser(tokens):
    ast=programa(tokens)
    return ast




    
print(parser(tokenizer('tester.c')))