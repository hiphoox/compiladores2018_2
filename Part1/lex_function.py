import re
import os

class Int_kw:
    def __init__(self):
        self.kw = "int"

class Id_kw:
    def __init__(self, id):
        self.id = id

class Open_paren:
    def __init__(self):
        self.paren = "("

class Close_paren:
    def __init__(self):
        self.paren = ")"
    
class Open_brace:
    def __init__(self):
        self.brace = "{"

class Close_brace:
    def __init__(self):
        self.brace = "}"

class Ret_kw:
    def __init__(self):
        self.kw = "return"

class Literal_num:
    def __init__(self, num):
        self.num = num

class Semicolon:
    def __init__(self):
        self.semi = ";"


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
            else:
                tok=re.search(r'[\{ | \} | \( | \) | \;]',letter)
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


    print("----- TOKENS -----")
    print(tokens)
    print()
    return tokens