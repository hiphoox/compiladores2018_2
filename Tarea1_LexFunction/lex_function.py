import re

def lex():
    tokens=[]
    word=""
    file=open("return_2.c", "r")
    for line in file:
        l=line.replace(" ", "").strip("\n")
        numero_searched=re.search(r'[0-9]+\;',l)
        if  numero_searched:
            tokens.append(numero_searched.group(0).strip(';'))

    print(tokens)
    return tokens
            
    
            
        

lex()