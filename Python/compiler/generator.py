def genera(ast,nodos = []):
	if(type(ast)!=bool):
		if(type(ast[0]) != list):
			print(len(ast))
			#print(ast[len(ast)-1])
			if(ast[0] == 'return'):
				nodos.append(ast[0])
				print('yey')
			#else:
				#ast.append(True)
		if(type(ast[1]) != list):
			#print('equis')
			print(ast[1])
			nodos.append(ast[1]) ##llegando a los terminales
			return
		else:
			if(len(ast)==2):  #donde se recursea
				#ast.append(True)
				print(ast)
				genera(ast[1])
			elif(len(ast)==3):
				#ast.append(True)
				genera(ast[1])#donde se recursea
				nodos.append(ast[0][1])
				genera(ast[2])
		return nodos
