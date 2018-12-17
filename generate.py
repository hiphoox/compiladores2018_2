#calls modules from anytree to reed tree from parser
from anytree import Node, RenderTree, PreOrderIter

g = []
	
def writeGlobl( ast, asmProg ):
    if ast[0] == "Program":
        asmProg.append( "\t.globl main\n" )
        return asmProg, ast[1:]
 
def writeFun( ast, asmProg ):
    if ast[0] == "Function":
        asmProg.append( "main:\n")
        return asmProg, ast[1:]
        
def writeRet( ast, asmProg ):
    if ast[0] == "Return":
    	if "+" in ast: 
    		asmProg, rest = writeSum( ast[2:], asmProg )
    	if "*" in ast:
    		asmProg, rest = writeMult( ast[2:], asmProg )
    	if isinstance( ast[1], int ): 
    		asmProg, rest = writeMov( ast[1:], asmProg )
        if "-" in ast or "!" in ast: 
        	asmProg = writeNeg( ast[2], asmProg )
        asmProg.append( "\tret\n" )
        return asmProg

def writeMov( ast, asmProg ):
    asmProg.append( "\tmovl\t$"+str(ast[0])+", %eax\n" ) 
    return asmProg, ast[1:]

def writeNeg( ast, asmProg ):
	asmProg.append( "\tneg\t%eax\n" )
	return asmProg

def writeSum( ast, asmProg ):
	
	asmProg, rest = writeMov( ast, asmProg )
	asmProg.append( "\tpush \t%eax\n" )
	asmProg, rest = writeMov( rest, asmProg )
	asmProg.append( "\tpop \t%ecx\n" )
	asmProg.append( "\taddl \t%ecx, %eax\n" )
	
	return asmProg, "None"

def writeMult( ast, asmProg ):
	
	asmProg, rest = writeMov( ast, asmProg )
	asmProg.append( "\tpush \t%eax\n" )
	asmProg, rest = writeMov( rest, asmProg )
	asmProg.append( "\tpop \t%ecx\n" )
	asmProg.append( "\timul \t%ecx, %eax\n" )
	
	return asmProg, "None"

def writeGen( ast, asmProg = g ):
	if ast:
		if writeGlobl( ast,asmProg ): writeGen( ast[1:],asmProg )
		if writeFun( ast, asmProg ): writeGen( ast[1:],asmProg )
		if writeRet( ast, asmProg ): writeGen( ast[1:],asmProg )
	return asmProg 


def gen( ast ):
	t = [node.name for node in PreOrderIter( ast )]
	
	g = writeGen(t)
	
	return g
