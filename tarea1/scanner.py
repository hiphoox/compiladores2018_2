import re                                   #importamos re para usar expresiones regulares funcion match(Patrón, Cadena)
from enum import Enum       

class Llave(Enum):                                          # Enum de los elementos que se pueden presentar en la cadena
	LlaveAbre =  "{"
	LlaveCierrra = "}"
	AbreParentesis = "("
	CierraParentesis = ")"
	Puntoycoma = ";"
	IntKey = "INT"                                  #por el momento solo usamos el identificador de enteros porque sera el que se use
	ReturnKeyword = "RETURN"

def Separacion(cadena,Lista_tokens):
    cadena=cadena.strip()                                           ##funcion que elimina los espacion del inicio y fin de la cadena
    #print(cadena)
    id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', cadena)  #funcion de expresiones regulares que esta buscando palabras en los rangos seleccionados
    #print(id)
    numero = re.match('[0-9]',cadena)                      #funcion de expresiones regulares que busca en la cadena los numeros o variables
    if(len(cadena)==0):
        return
    if(id):
        Lista_tokens.append([Key([id.group(0)]),id.group(0)])    #group() devolverá la parte de la cadena donde se halló la coincidencia.
        Separacion(cadena.lstrip(id.group(0)),Lista_tokens)        #Vamos a cortar de la cadena la parte que ya hemos identificacdo como numero
    elif(numero):
        Lista_tokens.append(['int',numero.group(0)])
        Separacion(cadena.lstrip(numero.group(0)),Lista_tokens)
    else:
        tokenEspecial = TokensEspeciales(cadena)            #si no es id o variable, verificamos si es un carcter especial
        if(tokenEspecial != False):
            Lista_tokens.append([Llave[tokenEspecial].value])
            Separacion(cadena.lstrip(Llave[tokenEspecial].value),Lista_tokens) #Vamos a cortar de la cadena la parte que ya hemos identificacdo como caracter especial
        
            
                           
def TokensEspeciales(cadena):
    if(cadena[0]=="{"):
        return Llave.LlaveAbre.name  #regresamos el nombre si es llave que abre
    elif(cadena[0] == "}"):
    	return Llave.LlaveCierrra.name
    elif(cadena[0] == "("):
    	return Llave.AbreParentesis.name
    elif(cadena[0] == ")"):
    	return Llave.CierraParentesis.name
    elif(cadena[0] == ";"):
    	return Llave.Puntoycoma.name
    else:
        return False              #si no es ningun caracter especial regresamos False

def Key (llave):
    llave=llave[0]
    if(llave =='return'):
        return Llave.ReturnKeyword.name
    elif(llave == 'int'):
        return Llave.IntKey.name
    else:
        return 'Id'



cadena = ("int main() { return 2; }")
#print(cadena)
Lista_tokens=[]
Separacion(cadena,Lista_tokens)
print(Lista_tokens)
