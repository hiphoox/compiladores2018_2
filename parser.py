#to install the anytree module run: $ pip install anytree
from anytree import Node, RenderTree

unaryOp     =   ["Minus","LogicalNegation"]
binaryOp    =   ["Plus","Minus","Mult","Div"] 

#function to add new node
def addT( name, par = None ):
        #case node doesn't have a parent
        if par == None: aux = Node( name, parent = None )
        #other case; "has a parent"
        else: aux = Node( name, parent = par )
        #return Node aux
        return aux

#function to print Tree with givin root
def printT( root ):
    for pre,fill,node in RenderTree( root ):
        print( "%s%s" % ( pre, node.name ) )


def parseBinOp( listTokens ):
    if listTokens[0] == "Plus":
        Sum = addT( "+" )
        return Sum, listTokens[1:]

    if listTokens[0] == "Minus":
        Minus = addT( "-" )
        return Minus, listTokens[1:]

    if listTokens[0] == "Mult":
        Mult = addT( "*" )
        return Mult, listTokens[1:]

    if listTokens[0] == "Div":
        Div = addT( "/" )
        return Div, listTokens[1:]

def parseUnaryOp( listTokens ):
    if( listTokens[0] == "LogicalNegation" ):
        Ln = addT( "!" )
        return Ln, listTokens[1:]

    if( listTokens[0] == "Minus" ):
        Mi = addT( "-" )
        return Mi, listTokens[1:]
   
def parseExp( listTokens ):

    if( not listTokens ):
        print("Parser Error: Mising expression ")
        exit()
    
    if listTokens[0] in unaryOp: 

        unOp, rest = parseUnaryOp( listTokens )

        node,rest = parseExp( rest )

        if node:
            unOp.parent = node
    
        return node, rest

    if  "Plus" in listTokens[1:] or "Minus" in listTokens[1:] or "Mult" in listTokens[1:] or "Div" in listTokens[1:]:
        
        l = []
        l.append( list( listTokens[0] ) )

        ls, rest = parseExp( l )
        
        binOp, rest = parseBinOp( listTokens[1:] )

        rs, rest = parseExp( rest )

        if ls:
            ls.parent = binOp
        if rs:
            rs.parent = binOp

        return binOp, rest

    if listTokens[0][0] == "Const" : 
    
        Cte = addT( int( listTokens[0][1] ) )
        return Cte, listTokens[1:]

    else:
        print( "Parser Error: Missing Expression")
        exit()

def parseState( listTokens ):
    if( not listTokens ):
        print( "Parser Error: No tokens to parse" )
        exit()

    if( listTokens[0][0] != "KW" and listTokens[0][1] != "return" ): 
        print( "Parser Error: No statement" )
        exit()
    
    node, rest = parseExp( listTokens[1:] )
    
    if( rest[0] != "SemiC" ):
        print( "Parser Error: Mising keyword: ';'" )
        exit()
    
    Re = addT( "Return" )

    node.parent = Re

    return Re, rest[1:]

def parseFun( listTokens ):
    if( not listTokens or listTokens[0][0] != "KW" or listTokens[0][1] != "int" ):
        print( "Parser Error: Missing keyword: int" )
        exit()
    if( listTokens[1][0] != "ID" ):
        print( "Parser Error: Mising Function's name" )
        exit()
    if( listTokens[2] != "OpenPa" ):
        print( "Parser Error: Mising token: '('" )
        exit()
    if( listTokens[3] != "ClosePa" ):
        print( "Parser Error: Mising token: ')' " )
        exit()
    if( listTokens[4] != "OpenBr" ): 
        print( "Parser Error: Mising token: '{' " )
        exit()
        
    node, rest = parseState( listTokens[5:] )
    
    if( rest[0] != "CloseBr" ):
        print( "Parser Error: Mising token: '}' " )
        exit()

    Fun = addT( "Function" )
    node.parent = Fun    
    return Fun

def parseProg( listTokens ):
    if( not listTokens ): return "Parser Error: Missing Tokens"

    node = parseFun( listTokens )
    if node:
        Prog = addT( "Program" )
        node.parent = Prog

    return Prog
