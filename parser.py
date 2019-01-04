#to install the anytree module run: $ pip install anytree
from anytree import Node, RenderTree

unaryOp     =   ["Minus","LogicalNegation","BitwiseComplement"]
binaryOp    =   ["Plus","Minus","Mult","Div","Assignment"] 

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

def parseUnaryOp( listTokens ):
    if( listTokens[0] == "LogicalNegation" ):
        Ln = addT( "!" )
        return Ln, listTokens[1:]

    if( listTokens[0] == "Minus" ):
        Mi = addT( "neg" )
        return Mi, listTokens[1:]
    
    if( listTokens[0] == "BitwiseComplement" ):
        Mi = addT( "neg" )
        return Mi, listTokens[1:] 

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

    if listTokens[0] == "Assignment":
        Div = addT( "=" )
        return Div, listTokens[1:]

def parseLogicalOp( listTokens ):
    if listTokens[0] == "LessThen":
        LessT = addT( "<" )
        return LessT, listTokens[1:]

    if listTokens[0] == "GreaterThen":
        GreaterT = addT( ">" )
        return GreaterT, listTokens[1:]

    if listTokens[0] == "GreaterThenOrEqual":
        GreaterTE = addT( ">=" )
        return GreaterTE, listTokens[1:]
    
    if listTokens[0] == "LessThenOrEqual":
        GreaterT = addT( "<=" )
        return GreaterT, listTokens[1:]

    if listTokens[0] == "NotEqual":
        NotE = addT( "!=" )
        return NotE, listTokens[1:]

    if listTokens[0] == "Equal":
        Equal = addT( "==" )
        return Equal, listTokens[1:]

    if listTokens[0] == "AND":
        And = addT( "&&" )
        return And, listTokens[1:]

    if listTokens[0] == "OR":
        Or = addT( "||" )
        return Or, listTokens[1:]

#Parse factor
def parseFactor( listTokens ):

    #"(" <exp> ")"
    if listTokens[0] == "OpenPa":
        node, rest = parseExp( listTokens[1:] )
        if rest[0] != "ClosePa":
            print("Parse Error: Missing token ')' in factor")
            exit()

        return node, rest[1:]

    # <unary_op> <factor>
    if listTokens[0] in unaryOp:

        node, rest = parseUnaryOp( listTokens )
        factor, rest = parseFactor( rest )

        node.parent = factor

        return factor, rest

    #<int>
    if listTokens[0][0] == "Const" : 
    
        Cte = addT( int( listTokens[0][1] ) )
        
        return Cte, listTokens[1:]

    #<id>
    if listTokens[0][0] == "ID" : 
    
        Id = addT( listTokens[0][1] ) 
        
        return Id, listTokens[1:]


            

def parseTerm( listTokens ):

    if not listTokens:
        print("Parser Error: Missing Term")
        exit()
    
    #<factor>
    leftFact, rest = parseFactor( listTokens )

    #{ ("*"|"/") <factor> }
    if rest[0] == "Mult" or rest[0] == "Div":
        node, rest = parseBinOp( rest )
        rightFact, rest = parseFactor( rest )

        leftFact.parent = node
        rightFact.parent = node
                
        return node, rest

    return leftFact, rest

def parseAdditiveExp( listTokens ):

    if not listTokens:
        print("Parser Error: Missing plus or minus operand")
        exit()

    #<term>
    leftTerm, rest = parseTerm( listTokens )

    #{ ("+"|"-") <term> }
    if rest[0] == "Plus" or rest[0] == "Minus":
        node, rest = parseBinOp( rest )
        rightTerm, rest = parseTerm( rest )

        leftTerm.parent = node
        rightTerm.parent = node
        
        return node, rest
    
    return leftTerm, rest

def parseRelationalExp( listTokens ):

    if not listTokens:
        print("Parser Error: Missing plus or minus operand")
        exit()

    #<additiveExp>
    leftAdditiveExp, rest = parseAdditiveExp( listTokens )

    #{ ("<"|">"|"<="|">=") <additiveExp> }
    if rest[0] == "LessThen" or rest[0] == "GreaterThen" or rest[0] == "LessThenOrEqual" or rest[0] == "GreaterThenOrEqual":
        node, rest = parseLogicalOp( rest )
        rightAdditiveExp, rest = parseAdditiveExp( rest )

        leftAdditiveExp.parent = node
        rightAdditiveExp.parent = node
        
        return node, rest
    
    return leftAdditiveExp, rest

def parseEqualityExp( listTokens ):

    if not listTokens:
        print("Parser Error: Missing plus or minus operand")
        exit()

    #<relationalExp>
    leftRelationalExp, rest = parseRelationalExp( listTokens )

    #{ ("!="|"==") <relationalExp> }
    if rest[0] == "NotEqual" or rest[0] == "Equal":
        node, rest = parseLogicalOp( rest )
        rightRelationalExp, rest = parseRelationalExp( rest )

        leftRelationalExp.parent = node
        rightRelationalExp.parent = node
        
        return node, rest
    
    return leftRelationalExp, rest

def parseLogicalAndExp( listTokens ):

    if not listTokens:
        print("Parser Error: Missing plus or minus operand")
        exit()

    #<equalityExp>
    leftEqualityExp, rest = parseEqualityExp( listTokens )

    #{ ("&&") <equalityExp> }
    if rest[0] == "AND":
        node, rest = parseLogicalOp( rest )
        rightEqualityExp, rest = parseEqualityExp( rest )

        leftEqualityExp.parent = node
        rightEqualityExp.parent = node
        
        return node, rest

    return leftEqualityExp, rest

def parseLogicalOrExp( listTokens ):

    if not listTokens:
        print("Parser Error: Missing plus or minus operand")
        exit()

    #<logical-and-exp>
    leftLogicalAndExp, rest = parseLogicalAndExp( listTokens )

    #{ ("||") <logical-and-exp> }
    if rest[0] == "OR":
        node, rest = parseLogicalOp( rest )
        rightLogicalAndExp, rest = parseLogicalAndExp( rest )

        leftLogicalAndExp.parent = node
        rightLogicalAndExp.parent = node
        
        return node, rest

    return leftLogicalAndExp, rest


def parseExp( listTokens ):

    if( not listTokens ):
        print("Parser Error: Mising expression ")
        exit()
   
    #<id> "=" 
    if( listTokens[0][0] == "ID" ):
    
        if listTokens[1] in binaryOp:
            eq, rest = parseBinOp( listTokens[1:] )

            if eq:
                name = addT( listTokens[0][1] )
                
                node, rest = parseExp( rest )

                node.parent = eq
                eq.parent = name

                return name, rest

        else:

            node = addT( listTokens[0][1] )

            return node, listTokens[1:]

    else:
        #| <logical-or-exp>
        node, rest = parseLogicalOrExp( listTokens )

        return node, rest


def parseState( listTokens ):

    if( not listTokens ):
        print( "Parser Error: No tokens to parse" )
        exit()

    #"return" <exp> ";"
    if( listTokens[0][0] == "KW" and listTokens[0][1] == "return" ): 
        
        Re = addT( "Return" )
        
        node, rest = parseExp( listTokens[1:] )
        node.parent = Re


        if( rest[0] != "SemiC" ):
            print( "Parser Error: Mising token: ';'" )
            exit()

        
        return Re, rest[1:]

    #| "int" <id> [ = <exp>] ";"
    if( listTokens[0][0] == "KW" and listTokens[0][1] == "int" ):
        
        if( listTokens[1][0] == "ID" ):
            # "int" <id>
            intName = addT( "int:"+listTokens[1][1] )
            rest = listTokens[2:]
            # [ = <exp >] ";"
            if( listTokens[2] == "Assignment" ):
                node , rest = parseExp( listTokens[3:] )

                eq, rest = parseBinOp( listTokens[2:] )
                node, rest = parseExp( rest )

                node.parent = eq
                eq.parent = intName


            if( rest[0] != "SemiC" ):
                print( "Parser Error: Mising token: ';'" )
                exit()
            
            return intName, rest[1:]


        else:
            print( "Parser Error: Missing ID" )
            exit()

                
    #<exp> ";"
    else:
        node, rest = parseExp( listTokens )

        if( rest[0] != "SemiC" ):
            print( "Parser Error: Mising token: ';'" )
            exit()

        return node, rest[1:]
    
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
    
    if listTokens[1][1] != "main": Fun = addT( "Function:"+listTokens[1][1] )   
    else: Fun = addT( "Function" )

    node, rest = parseState( listTokens[5:] )
    node.parent = Fun    
    
    while rest[0] != "CloseBr":
        node, rest = parseState( rest )
        node.parent = Fun

    return Fun

def parseProg( listTokens ):
    if( not listTokens ): return "Parser Error: Missing Tokens"

    node = parseFun( listTokens )
    if node:
        Prog = addT( "Program" )
        node.parent = Prog

    return Prog
