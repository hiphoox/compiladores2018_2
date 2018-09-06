def tokenizer (programa):
    aux = ''        
    kw = {'int', 'main', 'return', '(', ')', '{', '}', ';'}
    wp = {'(', ')', '{', '}', ';'}
    tokens = []
    archivo = open(programa, 'r')
    while (1):
        linea = archivo.readline()
        if not linea: break
        x = 0
        while x < len(linea):
            if (linea[x] != ' ' and linea[x].isdigit() == False):
                aux = aux + linea[x]
                if aux in kw:
                    if aux not in wp:
                        tokens.append(aux.upper()+'<>')
                    else:
                        tokens.append(aux)
                    aux = ''
            if (linea[x] == '\n'):
                tokens.append('\n')
                aux = ''
            if (linea[x] == '\t'):
                aux = ''
            if linea[x].isdigit():
                while (linea[x].isdigit() or linea[x] == '.'):
                    aux = aux + linea[x]
                    x = x + 1
                tipo = type(aux)
                if str(tipo).find('int'):
                    tokens.append('INT<'+ aux +'>')
                aux = ''
                x-=1
            x+=1
    return tokens

    
print(tokenizer('return2.c'))