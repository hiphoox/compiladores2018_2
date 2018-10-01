from tokenizer import *


def expresion(tokens):
    exp = []
    for i in tokens:
        l=i.split(":")
        if l[0] ==  "INT":
            exp.append(l[1])
            tokens.remove(i)
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
            pass
        elif l[0] ==  "CloseBrace":
            aidi.append(l[1])
            pass
        else:
            aidi.append(statement(tokens))
            break
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