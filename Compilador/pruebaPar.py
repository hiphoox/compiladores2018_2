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
    if len(tokensS) != 0:
        if tokensS[0] != 'SEMICOLON' or tokensS[0] != 'CLOSEBRACE':
            operador, tokensS = parse_exp(tokensS)
            programa.insert(0,operador) 
        else:
            ast = "Incorrecto"
            return (ast, tokensS, [])
    else:
        ast = "Incorrecto"
        return (ast, tokensS, [])

    if operador == 'error':
        ast = "Incorrecto"
        return (ast, tokensS, [])
    elif (tokensS[0] == "SEMICOLON"):
        tokensS.pop(0)
        if (len(operador) == 0):
            ast = 'Incorrecto'
            return (ast, tokensS, [])
        else:
            ast = 'Correcto'
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
        programa.append(idRet)
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
        programa.append(f_Id)
        ast = "Programa compilado"

    return ast, programa



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
    #print tokensFac
    next = tokensFac.pop(0)
    #print next
    if next == 'OPENPARENTHESIS':
        # <factor> ::= "(" <exp> ")"
        #print tokensFac
        exp = parse_exp (tokensFac) # Mandamos la expresion dentro del parentesis
        print (tokensFac)
        if tokensFac.pop(0) != 'CLOSEPARENTHESIS':
            print ("Validacion parentesis")
            return []
        return exp, tokensFac
    
    elif next in ['LOGICNEGOP', 'NEGOP', 'BITWOP']:
        # <factor> ::= <unary_op> <factor>
        op = convert_to_op (next)
        factor = parse_factor(tokensFac)
        return UnOp(op, factor), tokensFac

    elif next.find("INT") == 0:
        # <factor> ::= <int>
        #print next
        return next, tokensFac
    else:
        #print "Sintax error operadores"
        return "error",[]


def parse_term(tokensTerm):
    #print ("toksTerm ANTES: " + str(tokensTerm))
    term, tokensTerm = parse_factor(tokensTerm)
    #print (term)
    #print ("toksTerm DESPUES: " + str(tokensTerm))
    next = ''
    if len(tokensTerm) != 0:
        next = tokensTerm[0]
    #print ("Next, term: " + next + ", " + str(term))
    while next == 'MULTIPLICATION' or next == 'DIVISION':
        op = convert_to_op(tokensTerm.pop(0))
        next_term, tokensTerm = parse_factor(tokensTerm)
        #print op, term, next_term
        #print tokensTerm
        term = BinOp(op, term, next_term)
        #print ("Term: " + str(term))
        if len(tokensTerm) == 0:
            break
        elif tokensTerm[0] == 'SEMICOLON':
            break
        next = tokensTerm[0]
        
    #print "LISTA AST TERM"
    return term, tokensTerm

def parse_exp(tokensExp):
    #print ("TokExp ANTES: " + str(tokensExp))
    term, tokensExp = parse_term(tokensExp)
    next = ''
    if len(tokensExp) != 0: 
        next = tokensExp[0]
    #print ("Next, term: " + next + ", " + str(term))
    #print ("TokExp DESPUES: " + str(tokensExp))
    #print next, term, next
    while next == 'PLUS' or next == 'MINUS':
        #print ("TokensExp[0] = " + str(tokensExp[0]))
        op = convert_to_op(tokensExp.pop(0))
        next_term, tokensExp = parse_term(tokensExp)
        term = BinOp(op, term, next_term)
        #print ("Termino " + str(term))
        #print ("TokensExp: " + str(tokensExp))
        if tokensExp[0] == 'SEMICOLON':
            break
        break
    
    return term, tokensExp



"""
ESTRUCTURA:
<program> ::= <function>
<function> ::= "int" <id> "(" ")" "{" <statement> "}"
<statement> ::= "return" <exp> ";"
<exp> ::= <term> { ("+" | "-") <term> }
<term> ::= <factor> { ("*" | "/") <factor> }
<factor> ::= "(" <exp> ")" | <unary_op> <factor> | <int>
"""


