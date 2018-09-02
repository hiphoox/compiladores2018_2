from tokenizer import tokenizer
def parser(tokens):
    def expresion(tokens):
        a = [int(item) for item in tokens.split(',') if item.isdigit()]
        return a


parser(tokenizer('tarea1.c'))
