
# (1) -> La funcion realiza lo que debe de manera natural.
# (0) -> La funcion realiza lo que debe pero no de manera natual.

def codeGenerator(_ast):
	#Creacion del assembly
	assembly_file = open('assembly.s','w+')

	#Pensar en como recorrer el generador de manera mas natural. (0)
	#While que itera dentro la lista de listas.
	while True:
		instruction = _ast.pop(0)
		if instruction == 'main':
			assembly_file.write('.globl _'+instruction+'\n'+'_'+instruction+':\n')
		elif instruction == 'returnKeyWord':
			x = _ast.pop(0).pop()
			assembly_file.write('  mov $%s, '%(x)+chr(37)+'eax\n  ret\n')
		#Condicion de cierre
		if _ast == []:
			break
		_ast = _ast[0]