import re
from specialToken import specialToken
from keywords import keywords
from number import number

def lexer(renglon,lista_token):
	list = []
	renglon = renglon.strip()
	while(len(renglon) != 0):
		renglon = renglon.strip()
		id = re.match('\\(*[A-Za-z][A-Za-z0-9_]*\\)*', renglon) #Revisamos el elemento que vamos a etiquetar
		numero = re.match('[0-9]',renglon) #Revisamos si no es un número
		if(id): #Si es un elemento id/keyword creará un objeto keyword y lo etiqueta
			tok = keywords(id.group(0))
			if(tok.name != "Error"):
				lista_token.append([tok.elemento, tok.name])
				list.append(tok)
				renglon = renglon.lstrip(tok.elemento)
			else:
				print("Elemento no válido: " + tok.elemento)
				lista_token = []
				return lista_token
			#renglon = renglon.lstrip(id.group(0)) #Quitamos el elemento que acabamos de etiquetar
		elif(numero): #En caso de que no sea un id pero si un número, lo etiqueta, de momento solo tomamos en cuenta enteros
			tok = number(int(numero.group(0)))
			if(tok.name != "Error"):
				lista_token.append([tok.elemento, tok.name])
				list.append(tok)
				renglon = renglon.lstrip(numero.group(0))
			else:
				print("Elemento no válido: " + str(tok.numero))
				lista_token = []
				return lista_token				
		else: #En caso de que no sea ninguno de los dos anteriores lo podemos catalogar como token especial, por lo que lo verifica
			tok = specialToken(renglon[0])
			if(tok.name != "Error"): 
				lista_token.append([tok.elemento,tok.name])
				list.append(tok)
				renglon = renglon.lstrip(tok.elemento)
			else:
				print("Elemento no válido: " + tok.elemento)
				lista_token = []
				return lista_token
	print (lista_token)
	return list
