from lex import lex
from parser import parcer
from codeGenerator import codeGenerator

def compiler():
	file = "valid/multi_digit.c"

	_tokens = lex(file)
	if not _tokens:
		print("Error lexico")
		return 0

	_ast = parcer(_tokens)
	if not _ast:
		print("Error sintactico")
		return 0

	codeGenerator(_ast)

compiler()