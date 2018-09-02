from tokenizer import tokenizer

def expresion(tokens):
    a = [item for item in tokens if item.isdigit()]
    for i in a:
        tokens.remove(i)
    return a


def parser(tokens):
    ast=[]    
    ast.append(expresion(tokens))
    print(tokens)
    return ast
#def statement(tokens):
    
print(parser(tokenizer('tarea1.c')))
