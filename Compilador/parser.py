"""
program = Program(function_declaration)
function_declaration = Function(string, statement) //string is the function name
statement = Return(exp)
exp = Constant(int) 
"""

# TOKENS ESPERADOS: ['INT KEYWORD', 'MAIN ID', 'OPENPARENTHESIS', 'CLOSEPARENTHESIS', 
#                      'OPENBRACE', 'RETURN KEYWORD', 'INT<2563>', 'SEMICOLON', 'CLOSEBRACE']
def statement (tokensS, contFunciones, programa):
    if (tokensS[0].find("INT") == 0):
        ast = "Correcto"
        s = []
        s.append(tokensS.pop(0)) 
        programa.append(s)
    else:
        ast = "Incorrecto"
        return ast, tokensS, []

    if (tokensS[0] == "SEMICOLON"):
            tokensS.pop(0)
            return (ast, tokensS, programa)
    else:
        ast = "Incorrecto"
        return (ast, tokensS, [])

def funcion (tokensF, contFunciones, programa):
    contFunciones += 1
    if (tokensF[0] == 'RETURN KEYWORD'):
        idRet = tokensF.pop(0)
        (ast, tokensF, programa) = statement(tokensF, contFunciones, programa)
    else:
        return (("Fallo funcion"), tokensF, [])

    if (ast == 'Incorrecto' or tokensF[0] != "CLOSEBRACE"):
        ast = "Fallo funcion"
        return (ast, tokensF, [])
    elif (ast == "Correcto" and tokensF[0] == "CLOSEBRACE"):
        tokensF.pop(0)
        programa[contFunciones-1].insert(0, idRet)
        ast = "Funcion correcta"
        return (ast, tokensF, programa)


def parser(tokensP):
    contFunciones = 0
    programa = []
    #while len(tokensP) != 0:
    if (tokensP[0] == 'INT KEYWORD'):
            tokensP.pop(0)
    else:
        return "Error sintaxis", []
    if (tokensP[0] == 'MAIN ID'):
            f_Id = tokensP.pop(0)
    else:
        return "Error sintaxis", []
    if (tokensP[0] == 'OPENPARENTHESIS'):
            tokensP.pop(0)
            if (tokensP[0] == 'CLOSEPARENTHESIS'):
                tokensP.pop(0)
            else:
                return "Error sintaxis", []
    else:
        return "Error sintaxis", []
    if (tokensP[0] == 'OPENBRACE'):
            tokensP.pop(0)
            (ast, tokensP, programa) = funcion(tokensP, contFunciones, programa)
            if (len(tokensP) != 0):
                return "Error sintaxis", []
    else:
            return "Error sintaxis", []

    if (ast == "Fallo funcion" or len(tokensP) != 0):
        ast = "Error sintaxis"
        programa = []
    elif (ast == "Funcion correcta" and len(tokensP) == 0):
        programa[contFunciones-1].insert(0, f_Id)       
        ast = "Programa compilado"

    return ast, programa
