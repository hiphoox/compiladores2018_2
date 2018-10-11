'''Autor: Ramos Estrada Gerardo
Descripcion: Este programa realiza la funcion de escanear un programa 
en lenguaje C y obtener los tokens para mandarlos al parser'''
import os.path
import re
import sys

def scanner():
    tkns={"int":"INTKEYWORD", "main":"ID", "return":"RETURNKEYWORD", "(":"OPENPARE", ")":"CLOSEPARE", "{":"OPENBRACE", "}":"CLOSEBRACE", ";":"SEMICOLON"}
    patron=re.compile('[(){};]')#Expresion regular para reconocer los simbolos
    patron1=re.compile('[a-zA-Z]')#Expresion regular para reconocer los keywords
    patron2=re.compile('\d+')#Expresion regular para reconocer numeros
    tokens=[]
    lineas=0
    if os.path.isfile("return_2.c"):
        archivo=open("return_2.c","r")
        for linea in archivo:
            palabra=""
            linea=linea.strip(" ")
            for caracter in linea:
                if caracter == '\n':
                    lineas+=1
                elif caracter != " ":
                    if patron1.search(caracter) != None:  
                        palabra=palabra+caracter
                        if tkns.has_key(palabra):
                            tokens.append(tkns[palabra])
                            palabra=""
                    elif patron2.search(caracter) != None and palabra == "":
                        tokens.append(caracter)
                    elif patron.search(caracter) != None:
                        tokens.append(tkns[caracter])
                    else:
                        if palabra == "":
                            print("Error en la linea "+str(lineas)+" caracter: "+caracter+" no reconocido")
                            sys.exit()
                        else:
                            print("Error en la linea "+str(lineas)+" invalido: "+palabra+caracter)
                            sys.exit()
                else:
                    palabra=""
                    
        archivo.close()
    else:
        print("El archivo no existe")
    return tokens
