archivo = open("Hola.txt", "r")
#texto = archivo.read()
tokens = ['(', ')','{','}',';','"','"']
token = ''
palabra = ''
tokensFinal = []

#try:
lines=''

for line in archivo:
	lines+=str(line.strip())

for char in lines:
	for x in tokens:
		if char==x:
			if palabra!='':
				tokensFinal.append(palabra)
				palabra=''
			tokensFinal.append(char)
			char=''
		elif char==' ':
			if palabra!='':
				tokensFinal.append(palabra)
				palabra=''
			char=''
	if char!='':
		palabra+=char


print(tokensFinal)

#except:
#	print("No se pudo cerrar correctamente")