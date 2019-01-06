from lex import funcLeeArchivo
from codeGenerator import code_generator
from parse import parcer

def compiler(file):
	_tokenList = []
	_ast = []

	_tokenList = funcLeeArchivo(file)
	print('Lista de tokens:\n')
	print(_tokenList)

	if not _tokenList:
		return False

	print('\nAST:\n')
	_ast = parcer(_tokenList)
	if not _ast:
		print('Error sintactico.')
		return False

	code_generator(_ast)

"""
valid_files = ['valid/multi_digit.c','valid/newlines.c','valid/no_newlines.c','valid/spaces.c','valid/return_0.c','valid/return_2.c','valid/bitwise_zero.c','valid/bitwise.c','valid/neg.c','valid/nested_ops_2.c','valid/nested_ops.c','valid/not_five.c','valid/not_zero.c','valid/associativity.c','valid/associativity_2.c','valid/add.c','valid/div.c','valid/mult.c','valid/unop_parens.c','valid/unop_add.c','valid/sub_neg.c','valid/sub.c','valid/precedence.c','valid/parens.c']
invalid_files = ['invalid/no_brace.c','invalid/no_space.c','invalid/wrong_case.c','invalid/no_semicolon.c','invalid/missing_paren.c','invalid/missing_retval.c','invalid/missing_const.c','invalid/nested_missing_const.c','invalid/wrong_order.c','invalid/missing_first_op.c','invalid/missing_second_op.c','invalid/no_semicolon_2.c','invalid/malformed_paren.c']

print('Valid files:')
for x in valid_files:
	print('\n' + x)
	compiler(x)

print('\n\n\n\n')
print('Invalid files:')
for x in invalid_files:
	print('\n' + x)
	compiler(x)
"""
compiler('valid/add.c')