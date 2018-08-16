def tokenizer(file):
    lista = []
    provisional = []
    for palabra in [item for item in open(file,"r").read().replace("\n","").split(" ") if item != ""]:
        for letra in palabra:
            if letra in ['{', '}', '(', ')', ';']:
                lista.append(letra)
            else: 
                provisional.append(letra)
        if len(provisional) != 0:
            lista.append("".join(provisional))
        provisional = []
    return lista

print(tokenizer("tarea1.c"))

