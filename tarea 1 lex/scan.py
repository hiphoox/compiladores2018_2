import re

def lexer():
    space=""
    tok=[]
    abrir = open("return_2.c",'r')
    for leer in abrir:
        separar=leer.replace(" " , "").strip("\n")
        for x in separar:
            space=space+x
            space=space.strip("()\{\};")
            if(space=="int"):
                tok.append("Int keyword -"+space+"-")
                space=""
            elif(space=="main"):
                tok.append("id-"+space+"-")
                space=""
            elif(space=="return"):
                tok.append(space)
                space=""
            elif(space=="{"):
                tok.append("open brace--"+space+"--")
                space=""
            elif(space=="}"):
                tok.append("close brace--"+space+"--")
                word=""
            elif(space ==";"):
                tok.append("Semicolon--"+space+"--")
                space=""
            elif(x not in "int" and x not in "return" and x not in "main"):
                tok.append(x)
        print(tok)
        return(tok)

lexer()