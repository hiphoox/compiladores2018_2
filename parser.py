AST = []
#program,function,statement,expression

def parseUnaryOp( listTokens, ast = AST ):
    if( listTokens[0] == "LogicalNegation" ):
        ast.insert( 0, "!" )

    return listTokens[1:]

def parseExp( listTokens, ast = AST ):
    if( not listTokens ):
        print("Error: Mising expression ")
        exit()

    if listTokens[0][0] == "Const" : 
        ast.insert( 0, listTokens[0][1] )
        return listTokens[1:]
    elif listTokens[0] == "LogicalNegation": 
        unOp = parseUnaryOp( listTokens,ast )
        parseExp( unOp,ast )
        return unOp[1:]

def parseState( listTokens, ast = AST ):
    if( not listTokens ):
        print("Error: no tokens")
        exit()

    if( listTokens[0][0] != "KW" and listTokens[0][1] != "return" ): 
        print("Error: no statement")
        exit()

    exp = parseExp( listTokens[1:], ast )

    if( exp ):
        if( not exp[0] ):
            print("Error: Mising keyword: ';' ")
            exit()

    ast.insert( 0, "Return" )
    
    return exp.pop()

def parseFun( listTokens, ast = AST ):
    if( not listTokens or listTokens[0][0] != "KW" or listTokens[0][1] != "int" ):
        print("Error: Missing keyword: int")
        exit()
    if( listTokens[1][0] != "ID" ):
        print("Error: Mising Function's name" )
        exit()
    if( listTokens[2] != "OpenPa" ):
        print("Error: Mising token: '(' ")
        exit()
    if( listTokens[3] != "ClosePa" ):
        print("Error: Mising token: ')' ")
        exit()
    if( listTokens[4] != "OpenBr" ): 
        print("Error: Mising token: '{' ")
        exit()
    state = parseState( listTokens[5:], ast )
    
    if( state != "CloseBr" ):
        print("Error: Mising token: '}' ")
        exit()

    ast.insert( 0, listTokens[1][1] )

def parseProg( listTokens, ast = AST  ):
    if( not listTokens ): return "Error: Missing Tokens"

    fun = parseFun( listTokens, ast )

    ast.insert( 0, "Program" )

    return ast
