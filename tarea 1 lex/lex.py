

class token:
    OpenBrace =  "{"
    CloseBrace = "}"
    OpenParen = "("
    CloseParen = ")"
    Semicolon = ";"
    IntKeyword = "int"
    ReturnKeyword = "return"
	
def tok(text):
    tokens = text.split()
    tokensr=[]
    print (tokens)
    for elemento in tokens:
        print (elemento)
        """tipo= type(elemento)
        print(tipo)
        esta parte sirve por si requerimos en un futuro que python interprete el tipo de dato"""     
        if (elemento == token.IntKeyword):
               tokensr.append(elemento + "keyword")
        elif (elemento == token.ReturnKeyword):
            tokensr.append(elemento + "keyword")
        else:
            tokensr.append(elemento)
        
    print ('.'.join(tokensr))

    return '.'.join(tokensr)
