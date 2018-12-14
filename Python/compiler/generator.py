def genera(ast,nodos = []):
	if(type(ast)!=bool):
		if(len(ast)==2 and type(ast[1]) != list):  #hoja de ast
			cons = ast[1] 
			return cons
		elif(len(ast)==2):  #nodo solo con un hijo
			expr = genera(ast[1])
			if(ast[0] == 'return' and type(expr) != list):
				return  'return' + expr 
			return expr
		elif(len(ast)==3): #nodo con dos hijos
			term1 = ast[1] if type(ast[1]) != list else genera(ast[1])	
			op = ast[0][1]
			term2 = ast[2] if type(ast[2]) != list else genera(ast[2])
			return this_is_my_op(term1,op,term2)
		return nodos


def this_is_my_op(op1,sign,op3):
	#print(str(op1) + sign + str(op3))
	return '('+str(op1) + sign + str(op3)+')'
