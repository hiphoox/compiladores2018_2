from enum import Enum, unique 
import re 

class Token(Enum): 
        OpenBrace =  "{" 
        CloseBrace = "}" 
        OpenParen = "(" 
        CloseParen = ")" 
        Semicolon = ";" 
        IntKeyword = "INT" 
        CharKeyword = "CHAR" 
        ReturnKeyword = "RETURN" 
        IntofInt = 0 
        Addition = "+"
        Subtraction = "-"
        Division = "/"
        Multiplication = "*"



def Lex(file):
    cadena = open(file,"r").read()
    lista = re.findall('int|main|return|[0-9]+|[^0-9]|', cadena) 
    print(lista)  #el + es digitos 
    lista.pop() 

    for token in lista: 
        if token == ' ': 
            lista.remove(token)  #['int', ' ', 'main', '(', ')', '{', 'return', '0', ';', '}', ''] 
    print(lista) #Token.CloseBrace.name 

    lista2 =[] 
    for token in lista: 
        if token == '{': 
            lista2.append(Token.OpenBrace.name) 
        elif token == ')': 
            lista2.append(Token.CloseParen.name) 
        elif token == '(': 
            lista2.append(Token.OpenParen.name) 
        elif token == '}': 
            lista2.append(Token.CloseBrace.name) 
        elif token == ';': 
            lista2.append(Token.Semicolon.name) 
        elif token == 'int': 
            lista2.append(Token.IntKeyword.name) 
        elif token == '+': 
            lista2.append(Token.Addition.name) 
        elif token == '-': 
            lista2.append(Token.Subtraction.name) 
        elif token == '*': 
            lista2.append(Token.Multiplication.name) 
        elif token == '/': 
            lista2.append(Token.Division.name) 
        elif token == 'main': 
            lista2.append(Token.CharKeyword.name) 
        elif token == 'return': 
            lista2.append(Token.ReturnKeyword.name) 
        elif re.match('[0-9]+', token):
            fin=re.match('[0-9]+', token)
            #print(fin.group(0))
            lista2.append(fin.group(0))
        #else: 
         #   print("Error")
    return lista2