from lex import lex
from parser import parcer
from codeGenerator import codeGenerator

def compiler(file):
	_tokens = lex(file)
	if _tokens:
		_ast = parcer(_tokens)
		if _ast:
			codeGenerator(_ast)
			print('Completed compilation!')
		else:
			print('Error sintactico!')
	else:
		print('Error sintactico!')

valid_files = ['valid/multi_digit.c','valid/newlines.c','valid/no_newlines.c','valid/spaces.c']
invalid_files = ['invalid/no_brace.c','invalid/no_space.c','invalid/wrong_case.c']
print('Valid files:')
for x in valid_files:
	compiler(x)
print('\n')
print('Invalid files:')
for x in invalid_files:
	compiler(x)