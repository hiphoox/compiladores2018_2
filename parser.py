from tokenizer import tokenizer

def expresion(tokens):
    exp = [item for item in tokens if item.isdigit()]
    for i in exp:
        tokens.remove(i)
    return exp

def statement(tokens):
    sta = [item for item in tokens if item.split("<")[0]=="Keyword" ]
    return sta
    

def parser(tokens):
    ast=[]    
    ast.append(expresion(tokens))
    ast.append(statement(tokens))
    print(tokens)
    return ast
    
print(parser(tokenizer('tarea1.c')))
