from lex import lex
from parser import parcer

def compiler():
	file = "return_2.c"
	_tokens = lex(file)
	if not _tokens:
		print("Error lexico")
		return 0
	_ast = parcer(_tokens)
	if not _ast:
		print("Error sintactico")
		return 0
	print(_ast)
compiler()