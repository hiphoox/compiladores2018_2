import re
from specialToken import specialToken
from keywords import keywords

def lexer(renglon,lista_token):
	renglon = renglon.strip()
	while(len(renglon) != 0):
		renglon = renglon.strip()
		id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', renglon) #Revisamos el elemento que vamos a etiquetar
		numero = re.match('[0-9]',renglon) #Revisamos si no es un número
		if(id): #Si es un elemento id/keyword creará un objeto keyword y lo etiqueta
			tok = keywords(id.group(0))
			if(tok.name != "Error"):
				lista_token.append([tok.elemento, tok.name])
				renglon = renglon.lstrip(tok.elemento)
			else:
				print("Elemento no válido: " + tok.elemento)
				lista_token = ["Error"]
				return lista_token
			renglon = renglon.lstrip(id.group(0)) #Quitamos el elemento que acabamos de etiquetar
		elif(numero): #En caso de que no sea un id pero si un número, lo etiqueta, de momento solo tomamos en cuenta enteros
			lista_token.append(['Int',numero.group(0)])
			renglon = renglon.lstrip(numero.group(0))
		else: #En caso de que no sea ninguno de los dos anteriores lo podemos catalogar como token especial, por lo que lo verifica
			tok = specialToken(renglon[0])
			if(tok.name != "Error"): 
				lista_token.append([tok.caracter,tok.name])
				renglon = renglon.lstrip(tok.caracter)
			else:
				print("Elemento no válido: " + tok.caracter)
				lista_token = ["Error"]
				return lista_token
	return lista_token
