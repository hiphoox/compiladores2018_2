import re

def tokenizer(file):
	symbols = {'(':'OpenParen', ')': 'CloseParen', '{': 'OpenBrace', '}': 'CloseBrace', ';': 'Semicolon'}
	#las key words se pueden leer de un archivo
	key={'auto','break','case','char','const','continue','default','do','double','else','enum','extern','float',
            'for','if','inline','int','long','register','restrict','return','sizeof','static','struct','switch',
            'typedef','union','unsigned','void','volatile','while'}
	program = open(file, 'r').read().replace("\n", "").replace("\t", "")
	for x in symbols:
	    program = program.replace(x, ' '+symbols[x]+':'+x)
	for y in key:
		program = program.replace(y,' Keyword'+':'+y)	
	tokens = [item+'' for item in program.split(" ") if len(item) != 0]
	for i in tokens:
		if ":" not in i:
			digito=re.search(r'[0-9]+',i)
			if digito:
				tokens[tokens.index(i)]='INT:'+i
			chain=re.search(r'[a-zA-Z]+',i)
			if chain:
				tokens[tokens.index(i)]='ID:'+i
	return tokens

print(tokenizer('tarea1.c'))