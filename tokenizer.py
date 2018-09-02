def tokenizer(file):
	tokens = {'(':'OpenParen', ')': 'CloseParen', '{': 'OpenBrace', '}': 'CloseBrace', ';': 'Semicolon'}
	#las key words se pueden leer de un archivo
	key={'auto','break','case','char','const','continue','default','do','double','else','enum','extern','float',
            'for','if','inline','int','long','register','restrict','return','sizeof','static','struct','switch',
            'typedef','union','unsigned','void','volatile','while'}
	program = open(file, 'r').read().replace("\n", "").replace("\t", "")
	for x in tokens:
	    program = program.replace(x, ' '+tokens[x]+'<'+x+'>'+' ')
        for y in key:
            program = program.replace(y,' Keyword'+'<'+y+'> ')
	return [item+'' for item in program.split(" ") if len(item) != 0]

tokenizer('tarea1.c')

