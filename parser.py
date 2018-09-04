from tokenizer import tokenizer

def expresion(tokens):
    exp = [item for item in tokens if item.isdigit()]
    for i in exp:
        tokens.remove(i)
    return exp

def statement(tokens):
    sta = [item for item in tokens if item[item.find('<')+1:item.find('>')]=="return" or item[item.find('<')+1:item.find('>')]==";"  ]
    for i in sta:
        tokens.remove(i)
    sta.append(expresion(tokens))
    return sta
    

def parser(tokens):
    ast=[]    
    ast.append(statement(tokens))
    print(tokens)
    return ast
    
print(parser(tokenizer('tarea1.c')))
