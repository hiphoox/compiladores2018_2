'''Autor: Ramos Estrada Gerardo
Descripcion: Este programa realiza la funcion de escanear un programa 
en lenguaje C y obtener los tokens para mandarlos al parser'''
import re

def scanner():
    tkns={"int":"INTKEYWORD","rint":"INT", "main":"ID", "return":"RETURNKEYWORD", "(":"OPENPARE", ")":"CLOSEPARE", "{":"OPENBRACE", "}":"CLOSEBRACE", ";":"SEMICOLON"}
    patron=re.compile('[(){};]')
    patron2=re.compile('\W+')
    patron3=re.compile('\d+')
    tokens=[]
    archivo=open("return_2.c", "r")
    for linea in archivo:
        linea=linea.strip(" ")
        palabra=patron2.split(linea)
        for iterador in palabra:
            if tkns.has_key(iterador):
                tokens.append(tkns[iterador])
        palabra=patron3.findall(linea)
        if len(palabra) != 0:
            for iterador in palabra:
                tokens.append(int(iterador))
        palabra=patron.findall(linea)
        for iterador in palabra:
            if tkns.has_key(iterador):
                tokens.append(tkns[iterador])
    archivo.close()
    return tokens

