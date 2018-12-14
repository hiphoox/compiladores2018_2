class ErrorLexico(RuntimeError):
	informacion = ''
	def __init__(self, informacion):
		self.informacion =  'Error lexico, token no admitido:  ' + informacion

class ErrorSintactico(RuntimeError):
	def __init__(self, token_inesperado,esperado):
		self.informacion = 'Error sintáctico, token inesperado ' + token_inesperado + ' Se esperaba ' + esperado
