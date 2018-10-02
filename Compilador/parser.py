"""

********** Estructura que debe tener mi código **********
program = Program(function_declaration)
function_declaration = Function(string, statement) //string is the function name
statement = Return(exp)
exp = Constant(int) 

"""

# Lista de tokens esperados: ['INT KEYWORD', 'MAIN ID', 'OPENPARENTHESIS', 'CLOSEPARENTHESIS', 
#					  'OPENBRACE', 'RETURN KEYWORD', 'INT<2563>', 'SEMICOLON', 'CLOSEBRACE']


def statement (tokensS):		# Funcion que verifica los tokens en un statement, recibe los tokens restantes de la función 'función'
	if (tokensS[0].find("INT") == 0): # Verificamos que el valor que se retorna es un entero. El UNICO caso válido de nuestro compilador
					# Se comienza a realizar el AST en este punto
		ast = "Correcto"		# Si se encuentra el entero, activamos una "bandera" que nos diga que es correcto lo que se retornó de valor
		tokensS.pop(0)
	else:
		ast = "Incorrecto"		# Si es cualquier otra cosa retornamos la bandera de "error" junto con los tokens que ya sabemos están mal
		return ast, tokensS

	if (tokensS[0] == "SEMICOLON"):		# Para que el statement este completamente bien verificamos que exista el punto y coma al final
			tokensS.pop(0)
			return (ast, tokensS)		# Si se encuentra se regresa la bandera con el código 'Correcto' y las tokens restantes despues de la verificación
	else:
		ast = "Incorrecto"				# Si no hay punto y coma la bandera la cambiamos a "Incorrecto" e igualmente la regresamos junto con los tokens
		return (ast, tokensS)

def funcion (tokensF):			# Funcion que verifica los tokens en una función, recibe los tokens restantes de la función 'parser'
	if (tokensF[0] == 'RETURN KEYWORD'):	# Verificamos que exista en esa lista la llave del 'return'
		tokensF.pop(0)
		(ast, tokensF) = statement(tokensF)	# Si existe el return mandamos a llamar a la función de 'statement' para verificar que tenga una estructura correcta
	else:
		return (("Fallo funcion"), tokensF)	# Si no está el return se regresa el código de error

	if (ast == 'Incorrecto' or len(tokensF) == 0):		# Si al checar la bandera retornada por 'statement' sale "Incorrecto" o ya no hay tokens en la lista recibida...
		ast = "Fallo funcion"
		return (ast, tokensF)					# Automáticamente nos retornamos al inicio con el código de error en función
	elif (ast == "Correcto" and tokensF[0] == "CLOSEBRACE"):	# Si revisamos la bandera y dice "Correcto" y, además, encontramos el wrapper de cerrar llave...
		tokensF.pop(0)
		ast = "Funcion correcta"	# Decimos que la función se completó de revisar y está correcta por lo que se regresa la cadena "Función correcta"
		return (ast, tokensF)


def parser(tokensP):			# Funcion principal que va haciendo la relación entre tokens. 
	#while len(tokensP) != 0:	# Al tener una estructura ya definida y única por lo pronto se pasará a checar los tokens en orden de aparición esperada
	if (tokensP[0] == 'INT KEYWORD'):	# Verificamos que exista al principio el 'Id' de 'INT' y si está lo sacamos de nuestra lista para seguir verificando
			tokensP.pop(0)				
	else:									# Si no está se manda que hay un error en la sintaxis
			return "ERROR EN SINTAXIS"

	if (tokensP[0] == 'MAIN ID'):	# Verificamos que el siguiente de la lista sea el 'Id' de 'MAIN', si está lo sacamos de la lista
			tokensP.pop(0)
	else:							# Si no está se manda error en sintaxis
			return "ERROR EN SINTAXIS"

	if (tokensP[0] == 'OPENPARENTHESIS'):	# Se verifica que exista el paréntisis abierto
			tokensP.pop(0)								
			if (tokensP[0] == 'CLOSEPARENTHESIS'):		# Si esta el parentesis abierto revisamos que este el parentisis de cerrar
				tokensP.pop(0)
			else:
				return "ERROR EN SINTAXIS"
	else:
			return "ERROR EN SINTAXIS"


	if (tokensP[0] == 'OPENBRACE'):		# Verificamos que haya una llave abierta...
			tokensP.pop(0)
			(ast, tokensP) = funcion(tokensP)	# La llave abierta indica que se esta definiendo una función por lo que mandamos el resto de tokens a la función "funcion"
			if (len(tokensP) != 0):		# Si al verificar los tokens recibidos por la función se encuentran aún más tokens se manda error porque no se esperan más en este punto.
				return "ERROR EN SINTAXIS"
	else:								# Si al verificar no se encuentra la llave abierta se manda el error de sintaxis
			return "ERROR EN SINTAXIS"

	if (ast == "Fallo funcion" or len(tokensP) != 0):		# Al final verificamos la bandera recibida. Si existe un fallo se mandará el código correspondiente.
		ast = "ERROR EN SINTAXIS"							
	elif (ast == "Funcion correcta" and len(tokensP) == 0):	# Si todo lo que se revisó terminó correctamente se manda el código de que la compilación fue un exito.
		ast = "COMPILACION EXITOSA"

	return ast 			# RETORNAMOS EL VALOR DE NUESTRA BANDERA AST (PROXIMAMENTE SE HARÁ QUE 'ast' SEA UNA ESTRUCTURA TIPO ÁRBOL)
