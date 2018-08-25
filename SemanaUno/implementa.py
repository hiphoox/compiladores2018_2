import lexerSemana1 as scan

f=open("pruebaLe.c","r")
codigo=f.read()
cadena=codigo
f.close()

tokens=scan.creaListaTokens(cadena)
print("Tokens: ")
print(tokens)