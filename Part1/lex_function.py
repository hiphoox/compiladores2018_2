import re
import os
from enum import Enum

#class Token(Enum):
#    OpenBrace="{",
#    CloseBrace="}",
#    OpenParen="(",
#    CloseParen=")",
#    Semicolon=";",
#    IntId="int",


def lex():
    tokens=[]
    word=""
    l=open("valid_return_2.c", "r").read().replace(" ","").replace("\n", "")
    for letter in l:
        word=word+letter
        word=word.strip("()\{\};")
        if(word=="int"):
            tokens.append("INT_ID<"+word+">")
            word=""
        elif(word=="main"):
            tokens.append("ID<"+word+">")
            word=""
        elif(word=="return"):
            tokens.append(word.upper())
            word=""
        elif(letter not in "int" and letter not in "return" and letter not in "main"):
            single_numero_searched=re.search(r'[0-9]',letter)
            if  single_numero_searched:
                numero_searched=re.search(r'[0-9]+\;',l)
                if  numero_searched:
                    if ("INT<"+numero_searched.group(0).strip(';')+">" not in tokens):
                        tokens.append("INT<{}>".format(numero_searched.group(0).strip(';')))
            else:
                tok=re.search(r'[\{ | \} | \( | \) | \;]',letter)
                if tok:
                    tokens.append(tok.group(0))


#    for line in file:
#        l=line.replace(" ", "").strip("\n")
#        int_searched=re.search(r'int',l)
#        if  int_searched:
#            tokens.append("INT<"+int_searched.group(0)+">")
#        fun_name_searched=re.search(r'int[a-z]+\(',l)
#        if  fun_name_searched:
#            tokens.append("ID<"+int_searched.group(0)+">".strip("int("))
#        for letter in line:
#            if(letter=="{" or letter="}" or letter"(" or letter")" or ";")
#            numero_searched=re.search(r'[0-9]+\;',l)
#            if  numero_searched:
#                tokens.append(numero_searched.group(0).strip(';'))

    print(tokens)
    return tokens
            
