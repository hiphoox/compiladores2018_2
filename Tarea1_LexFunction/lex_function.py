import re

def lex():
    tokens=[]
    word=""
    file=open("return_2.c", "r")
    for line in file:
        l=line.replace(" ", "").strip("\n")
        _l=l
        for letter in l:
            word=word+letter
            word=word.strip("()\{\};")
            if(word=="int"):
                tokens.append("INT<"+word+">")
                word=""
            elif(word=="main"):
                tokens.append("ID<"+word+">")
                word=""
            elif(word=="return"):
                tokens.append(word)
                word=""
            elif(letter not in "int" and letter not in "return" and letter not in "main"):
                tokens.append(letter)
    print(tokens)
    return tokens
            
    
            
        

lex()