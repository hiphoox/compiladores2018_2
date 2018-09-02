from tokenizer import tokenizer
def parser(tokens):    
    return [item for item in tokens if item.isdigit()]

print(parser(tokenizer('tarea1.c')))
