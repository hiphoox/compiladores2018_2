
# coding: utf-8

# In[21]:


#Pichardo González Jenny Alejandra
#Compiladores - Grupo 3

tokens = ['OpenBrace', 'CloseBrace', 'OpenParent', 'CloseParent', 'Semicolon', 'IntKeyword',
         'ReturnKeyword', 'Int']

class token(): {
    OpenBrace = "{"
    CloseBrace = "}"
    OpenParent = "("
    CloseParent = ")"    
    Semicolon = ";"
    IntKeyword = "int"
    ReturnKeyword = "return"
}
    
def lex:
    archivo = open("return2.c", "r")
    for linea in archivo:
        linea = linea.strip()
        for elemento in linea:
            if (elemento == "{"):
                return token.OpenBrace.name
            elif (elemento == "}"):
                return token.CloseBrace.name
            elif (elemento == "("):
                return token.OpenParent.name
            elif (elemento == ")"):
                return token.CloseParent.name
            elif (elemento == ";"):
                return token.Semicolon.name
            elif (elemento == "int"):
                return token.IntKeyword.name
            elif (elemento == "return"):
                return token.ReturnKeyword.name
            else tokens.append(elemento)
            
lex()

print (tokens)
return tokens

