#Definicion de las funciones que usaremos para el lexer
#Realiza la busqueda del simbolo correspondiente
def simbols(code_section):
	if code_section == '(':
		return 'openParentesis'
	if code_section == ')':
		return 'closeParentesis'
	if code_section == '{':
		return 'openBrace'
	if code_section == '}':
		return 'closeBrace'
	if code_section == ';':
		return 'semiColon'

#Realiza la busqueda del simbolo correspondiente
def operators(code_section):
	if code_section == '-':
		return 'minus'
	if code_section == '!':
		return 'logicalNegation'
	if code_section == '~':
		return 'bitwiseComplement'
	if code_section == '+':
		return 'addition'
	if code_section == '*':
		return 'multiplication'
	if code_section == '/':
		return 'division'

#Realiza la busqueda del keyWord correspondiente
def keyWords(code_section):
	if code_section == 'int':
		return 'intKeyWord'
	if code_section == 'return':
		return 'returnKeyWord'




#Definicion de los nodos que usaremos para el AST
#Clase que define un nodo de tipo Prog(Programa)
class Prog:
    def __init__(self, fun):
        self.fun = fun

#Clase que define un nodo de tipo Fun(Funcion)
class Fun:
    def __init__(self, id, statement):
        self.id = id
        self.statement = statement

#Clase que define un nodo de tipo Return(Return)
class Return:
    def __init__(self, exp):
        self.exp = exp

#Clase que define un nodo de tipo UnOp(UnaryOperator)
class UnOp:
	def __init__(self, op, inner_exp):
		self.op = op
		self.inner_exp = inner_exp

#Clase contenedora de un entero
class Integer:
	def __init__(self, code_section):
		self.int = int(code_section)

#Clase contenedora de un identificador
class Identifier:
	def __init__(self, funName):
		self.funName = funName

class Operator:
	def __init__(self, operator):
		self.operator = operators(operator)

class BinOp:
	def __init__(self, operator, op1, op2):
		self.operator = operator
		self.op1 = op1
		self.op2 = op2