import re
import os

from c_classes import *

def lex():
    tokens=[]
    word=""
    l=open("valid_return_2.c", "r").read().replace(" ","").replace("\n", "")
    for letter in l:
        word=word+letter
        word=word.strip("()\{\};")
        if(word=="int"):
            tokens.append(Int_kw())
            word=""
        elif(word=="main"):
            tokens.append(Id_kw("main"))
            word=""
        elif(word=="return"):
            tokens.append(Ret_kw())
            word=""
        elif(letter not in "int" and letter not in "return" and letter not in "main"):
            single_numero_searched=re.search(r'[0-9]',letter)
            if  single_numero_searched:
                numero_searched=re.search(r'[0-9]+\;',l)
                if  numero_searched:
                    if (Literal_num(numero_searched.group(0).strip(';')) not in tokens):
                        tokens.append(Literal_num(numero_searched.group(0).strip(';')))
                        break
            else:
                tok=re.search(r'[\{ | \} | \( | \) | \; | \- | \~ | \! ]',letter)
                if tok:
                    if (tok.group(0) == "{"):
                        tokens.append(Open_brace())
                    elif (tok.group(0) == "}"):
                        tokens.append(Close_brace())
                    elif (tok.group(0) == "("):
                        tokens.append(Open_paren())
                    elif (tok.group(0) == ")"):
                        tokens.append(Close_paren())
                    elif (tok.group(0) == ";"):
                        tokens.append(Semicolon())
                    elif (tok.group(0) == "-"):
                        tokens.append(Negation())
                    elif (tok.group(0) == "~"):
                        tokens.append(BitwiseComplement())
                    elif (tok.group(0) == "!"):
                        tokens.append(LogicalNegation())


    print("----- TOKENS -----")
    print(tokens)
    print()
    return tokens