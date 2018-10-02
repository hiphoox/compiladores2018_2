import re

def tokenizerV2 (programa):         # Funcion para tokenizar la entrada de código
    archivo = open(programa, 'r')
    tokens = []
    TK = {'int': 'INT KEYWORD', 'main': 'MAIN ID', 'return': 'RETURN KEYWORD'};     # Diccionario con keywords
    WP = {'(':'OPENPARENTHESIS', ')': 'CLOSEPARENTHESIS', '{':'OPENBRACE', '}':'CLOSEBRACE', ';':'SEMICOLON'};  # Diccionarios con wrappers

    while (1):      # Loop que seguirá mientras siga encontrando líneas en el código
        
        codigo = archivo.readline()     # Lectura del código línea por línea
        if not codigo: break            # Condicion de salida de la funcion.
        codigo.strip()
        while len(codigo) != 0:
            Id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', codigo)  # Expresion regular para encontrar texto
            num = re.match('[0-9]+', codigo)    # Expresion regular para encontrar números
            if (len(codigo) == 0):
                break
            if(Id):                             # Si encuentra un 'Id'...
                if (Id.group(0) in TK):         # Hace la verificación si el 'Id' se encuentra en el diccionario de keywords
                    tokens.append(TK[Id.group(0)])      # Si esta busca su definicion y la agrega a la lista de tokens
                    length = len(Id.group(0))           
                    codigo = codigo[length:len(codigo)] # Ocupamos la longitud del Id encontrado para eliminarlo de nuestra variable que tiene la línea
                    #codigo.replace(Id.group(0),'')
                else:
                    tokens.append('ID<'+Id.group(0)+'>')    # Si no encuentra el 'Id' en el diccionario de keywords simplemente lo guarda como 'Id<nombreId>'
                    length = len(Id.group(0))
                    codigo = codigo[length:len(codigo)]     # De igual forma eliminamos el 'Id' de la variable que contiene la línea de código
                    #codigo.replace(Id.group(0), '')

            elif (num):                         # Si lo que encuentra es un número...
                tokens.append('INT<'+ num.group(0) +'>')    # Al momento como sólo acepta 'INT' se le pone el indicador de eso y pone el número encontrado
                lenght = len(str(num.group(0)))
                codigo = codigo[lenght:len(codigo)]         # De igual forma eliminamos el numero de la variable que contiene la linea de codigo

            elif(codigo[0] in WP):              # Si no es ni un 'Id' ni un número verificamos a ver si la primer posicion de la cadena es un Wrapper
                tokens.append(WP[codigo[0]])    # Si lo es lo agregamos a nuestros tokens con su definición en el diccionario de Wrappers
                codigo = codigo[1:len(codigo)]  # Eliminamos el wrapper de la cadena de codigo. 

            elif (codigo[0] in ['\t', '\n', ' ']):  # Si no es ninguno de los casos anteriores verificamos si es un espacio, una tabulación o un espacio...
                codigo = codigo[1:len(codigo)]      # Si es alguno de los tres los eliminamos de nuestra cadena de codigo.
                
    return tokens       # La funcion regresa la lista de tokens bien identificados
