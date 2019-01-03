import re

def tokenizer(file):

	tokenss=[]
	#diccionario de simbolos
	symbols = {'(':'OpenParen', ')': 'CloseParen', '{': 'OpenBrace', '}': 'CloseBrace', ';': 'Semicolon','-':'Negation','~':'Bitwise','!':'Logic Neg'}

	#set de palabras reservadas del lenguaje C
	key={'auto','break','case','char','const','continue','default','do','double','else','enum','extern','float',
            'for','if','inline','int','long','register','restrict','return','sizeof','static','struct','switch',
            'typedef','union','unsigned','void','volatile','while'}

	
	#Abre el archivo tarea1.c y reemplaza todos los saltos de linea y tabs por cadena vacia
	with open(file) as fp:
		for cnt, line in enumerate(fp):
			line = line.replace("\n", "  ")
			for x in symbols:
				line = line.replace(x, ' '+symbols[x]+':'+x)
			for y in key:
				line = line.replace(y,' Keyword'+':'+y)
			tokens = [item for item in line.split(" ") if len(item) != 0]
			tokenss.append(tokens)
			
			for i in tokens:
				if ":" not in i:
					digito=re.search(r'[0-9]+',i)
					if digito:
						tokens[tokens.index(i)]='INT:'+i
					chain=re.search(r'[a-zA-Z]+',i)
					if chain:
						tokens[tokens.index(i)]='ID:'+i
	tokensf = [val for sublist in tokenss for val in sublist]
			

			
			

			
		    
	"""


	El primer for etiqueta los simbolos que se encuentren en el programa.

	El segundo for etiqueta las keywords encontradas en el programa.

	Tercer for busca las palabras que aun no estan etiquetadas, y con expresiones regulares
	se etiquetan numeros y id's.
	"""
	return tokensf
	

print(tokenizer('tarea1.c'))