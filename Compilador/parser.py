#program = Program(function_declaration)
#function_declaration = Function(string, statement) //string is the function name
#statement = Return(exp)
#exp = Constant(int)

"""
<exp> ::= <term> { ("+" | "-") <term> }
<term> ::= <factor> { ("*" | "/") <factor> }
<factor> ::= "(" <exp> ")" | <unary_op> <factor> | <int>
"""

# TOKENS ESPERADOS: ['INT KEYWORD', 'MAIN ID', 'OPENPARENTHESIS', 'CLOSEPARENTHESIS',
#                      'OPENBRACE', 'RETURN KEYWORD', [LOGICNEGOP, NEGOP, BITWOP] , 'INT<#>', 'SEMICOLON', 'CLOSEBRACE']

def statement (tokensS, contFunciones, programa):
    operador = ''
    if (tokensS[0] in ['LOGICNEGOP', 'NEGOP', 'BITWOP']):
        operador = tokensS.pop(0)
        if (tokensS[0].find('INT') == 0):
            ast = "Correcto"
            s = []
            s.append(tokensS.pop(0))
            programa.append(s)
    elif (tokensS[0].find('INT') == 0):
        ast = "Correcto"
        s = []
        s.append(tokensS.pop(0))
        programa.append(s)
    else:
        ast = "Incorrecto"
        return ast, tokensS, []

    if (tokensS[0] == "SEMICOLON"):
        tokensS.pop(0)
        if (len(operador) == 0):
              return (ast, tokensS, programa)
        else:
            programa[contFunciones-1].insert(0, operador)
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


"""
def convert_to_op (operator):
    if (operator == 'PLUS'):
        return '+'
    elif (operator == 'MINUS'):
        return '-'
    elif (operator == 'MULTIPLICATION'):
        return '*'
    elif (operator == 'DIVISION'):
        return '/'
    elif (operator == 'BITWOP'):
        return '~'
    elif (operator == 'LOGICNEGOP'):
        return '!'


def UnOp(op, factor):
    OpUn = [op, factor]
    return OpUn


def BinOp(op, term, next_term):
    OpBin = [op, term, next_term]
    return OpBin


def parse_factor (tokensFac):
    next = tokensFac.pop(0)
    if next == OPENPARENTHESIS:
        # <factor> ::= "(" <exp> ")"
        exp = parse_exp (tokensFac) # Mandamos la expresion dentro del parentesis
        if (tokensFac[0] != 'CLOSEPARENTHESIS'):
            print ("Error verificacion parentesis cerrado")
            #retornar error
        return exp
    
    elif next in ['LOGICNEGOP', 'NEGOP', 'BITWOP']:
        # <factor> ::= <unary_op> <factor>
        op = convert_to_op (next)
        factor = parse_factor(tokensFac)
        return UnOp(op, factor)

    elif next.find("INT") == 0:
        # <factor> ::= <int>
        return tokensFac.pop(0)

    else:
        return "Sintax error"



def parse_term(tokensTerm):
    next = tokensTerm[1]
    term = tokensTerm.pop(0)
    while (next == 'MULTIPLICATION' or next == 'DIVISION'):
        op = convert_to_op(tokensTerm.pop())
        next_term = parse_factor(tokensTerm)
        term = BinOp(op, term, next_term)
        next = tokensTerm[0]
    return "LISTA AST"

def parse_exp(tokensExp):
    next = tokensExp[1]
    term = tokensExp.pop(0)
    while (next == 'PLUS' or next == 'MINUS'):
        op = convert_to_op(tokensExp.pop())
        next_term = parse_term(tokensExp)
        term = BinOp(op, term, next_term)
        next = tokensExp[0]
    return "LISTA AST"
"""


"""
ESTRUCTURA:
<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <term> { ("+" | "-") <term> }
<term> ::= <factor> { ("*" | "/") <factor> }
<factor> ::= "(" <exp> ")" | <unary_op> <factor> | <int>
"""