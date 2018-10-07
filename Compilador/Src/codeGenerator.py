def codeGenerator(ast):
	file_assembly = open('assembly.s','w+')
	file_assembly.write('.globl _'+'main'+'\n'+'_'+'main'+':\n')
	file_assembly.write('  mov $%s, '%(ast)+chr(37)+'eax\n  ret\n')
