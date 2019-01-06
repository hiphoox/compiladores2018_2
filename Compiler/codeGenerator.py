from wrappers import Prog
from wrappers import Fun
from wrappers import Return
from wrappers import UnOp
from wrappers import Integer
from wrappers import Operator 
from wrappers import BinOp

#Regresa la cadena correspondiente al nodo BinOp
def binOp(_binOp):#Checar esta funcion porque no esta regresando el codigo como corresponde.
	if _binOp:
		if _binOp.operator.operator == 'addition' or _binOp.operator.operator == 'minus':
			return returN(Return(_binOp.op1)) + '\n\tpush ' + chr(37) + 'eax' + returN(Return(_binOp.op2)) + '\n\tpop ' + chr(37) + 'ecx\n\taddl ' + chr(37) + 'ecx, ' + chr(37) + 'eax'
		if _binOp.operator.operator == 'multiplication' or _binOp.operator.operator == 'division':
			return returN(Return(_binOp.op1)) + '\n\tpush ' + chr(37) + 'eax' + returN(Return(_binOp.op2)) + '\n\tpop ' + chr(37) + 'ecx\n\timul ' + chr(37) + 'ecx, ' + chr(37) + 'eax'

#Regresa la cadena correspondiente al nodo UnOp.
def unOp(_unOp):
	if _unOp:
		if _unOp.op.operator == 'minus':
			return returN(Return(_unOp.inner_exp)) + '\n\tneg    ' + chr(37) + 'eax'
		if _unOp.op.operator == 'bitwiseComplement':
			return returN(Return(_unOp.inner_exp)) + '\n\tneg    ' + chr(37) + 'eax'
		if _unOp.op.operator == 'logicalNegation':
			return returN(Return(_unOp.inner_exp)) + '\n\tcmpl   $0, ' + chr(37) + 'eax  \n\tmovl   $0, ' + chr(37) + 'eax \n\tsete   ' + chr(37) + 'al'

#Regresa la cadena correspondiente al nodo Integer.
def integer(_integer):
	if _integer:
		return '\n\tmov $%s,' %(_integer.int) + chr(37) + 'eax'

#Regresa la cadena correspondiente al nodo Return.
def returN(_return):
	if _return:
		if type(_return.exp) is BinOp:
			return binOp(_return.exp)
		if type(_return.exp) is UnOp:
			return unOp(_return.exp)
		if type(_return.exp) is Integer:
			return integer(_return.exp)

#Regresa la cadena correspondiente al nodo Fun.
def function(_function):
	if _function:
		return '.globl ' + _function.id.funName + '\n' + _function.id.funName + ':' + returN(_function.statement)

#Regresa la cadena correspondiente al nodo Prog
def program(_program):
	if _program:
		return function(_program.fun) + '\nret'

#Funcion encargada de generar el archivo assembly.s
def code_generator(_ast):
	assembly_file = open('assembly.s','w+')
	print('\nassembly.s:\n\n' + program(_ast))
	assembly_file.write(program(_ast))
	assembly_file.close()
