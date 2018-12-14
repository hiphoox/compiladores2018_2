import re

def tokenizerV2 (programa):
    archivo = open(programa, 'r')
    tokens = []
    TK = {'int': 'INT KEYWORD', 'main': 'ID<main>', 'return': 'RETURN KEYWORD'}
    WP = {'(':'OPENPARENTHESIS', ')': 'CLOSEPARENTHESIS', '{':'OPENBRACE', '}':'CLOSEBRACE', ';':'SEMICOLON'}
    OpUn = {'-':'MINUS', '~':'BITWOP', '!':'LOGICNEGOP'}
    OpBin = {'+':'PLUS', '*':'MULTIPLICATION', "/":'DIVISION'}

    while (1):
        
        codigo = archivo.readline()
        if not codigo: break
        codigo.strip()
        
        while len(codigo) != 0:
           
            if (len(codigo) == 0):
                break
            else:
                if(codigo[0] in WP):
                    tokens.append(WP[codigo[0]])
                    codigo = codigo[1:len(codigo)]

                elif (codigo[0] in ['\t', '\n', ' ']):
                    codigo = codigo[1:len(codigo)]
                elif (codigo[0] in OpUn):
                    tokens.append(OpUn[codigo[0]])
                    codigo = codigo[1:len(codigo)]
                elif (codigo[0] in OpBin):
                    tokens.append(OpBin[codigo[0]])
                    codigo = codigo[1:len(codigo)]  
                else:
                    Id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', codigo)
                    if(Id):
                        if (Id.group(0) in TK):
                            tokens.append(TK[Id.group(0)])
                            length = len(Id.group(0))
                            codigo = codigo[length:len(codigo)]
                            #codigo.replace(Id.group(0),'')
                        
                        else:
                            tokens.append('ID<'+Id.group(0)+'>')
                            length = len(Id.group(0))
                            codigo = codigo[length:len(codigo)]
                            #codigo.replace(Id.group(0), '')
                    else:
                        num = re.match('[0-9]+', codigo)
                        if (num):
                            tokens.append('INT<'+ num.group(0) +'>')
                            lenght = len(str(num.group(0)))
                            codigo = codigo[lenght:len(codigo)]
                 
    return tokens
