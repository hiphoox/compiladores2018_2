#calls modules from anytree to reed tree from parser
from anytree import Node, RenderTree, PreOrderIter
import re

g = []

size = 256

def writeGlobl( ast, asm ):
    asm.append( "\t.globl main\n" )
    return ast[1:], asm
 
def writeFun( ast, asm ):
    asm.append( "main:\n")
    return ast[1:], asm
        
def writeRet( ast, asm ):
	asm.append( "\tret\n" )
	return ast[1:], asm

def writeNeg( ast, asm ):
	r = re.compile('.*movl')
	
	if filter( r.match, asm ):	

		asm.insert( asm.index( filter( r.match, asm )[-1] ) + 1, "\tneg \t%eax\n" )	
	
	return ast[1:], asm

def writeNot( ast, asm ):
	r = re.compile('.*movl')
	
	if filter( r.match, asm ):	

		asm.insert( asm.index( filter( r.match, asm )[-1] ) + 1, "\tcmpl\t$0, %eax\n\n \tmovl\t$0, %eax\n\n \tsete\t%al\n" )	
	

	return ast[1:], asm

def writeMov( ast, asm ):
    asm.append( "\tmovl\t$"+str(ast[0])+", %eax\n" ) 
    return ast[1:], asm

def writeSum( ast, asm ):
	l = []
	l.append(ast[1])
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\taddl \t%ecx, %eax\n" )
	
	return rest, asm

def writeMult( ast, asm ):
	l = []
	l.append(ast[1])
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\timul \t%ecx, %eax\n" )
	
	return rest, asm

def writeMinus( ast, asm ):
	l = []
	l.append(ast[1])
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%dst\n" )

	asm.append( "\tsubl \t%src, %dst\n" )
	asm.append( "\tmovl \t%dst, %eax\n" )
	
	return rest, asm

def writeDiv( ast, asm ):
	l = []
	l.append(ast[1])
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tmovl \t%eax, %dst\n" )
	asm.append( "\tmovl \t$0, %edx\n" )
	asm.append( "\tpop \t%eax\n" )
	asm.append( "\tidivl dst\n" )
	
	return rest, asm

def writeLogicEqual( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\tcmpl \t%eax, %ecx\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsete \t%al\n" )

	return rest, asm

def writeLogicNotEqual( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\tcmpl \t%eax, %ecx\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsetne \t%al\n" )

	return rest, asm
	
def writeLogicGreaterThenOrEqual( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\tcmpl \t%eax, %ecx\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsetge \t%al\n" )

	return rest, asm

def writeLogicLessThenOrEqual( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\tcmpl \t%eax, %ecx\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsetle \t%al\n" )

	return rest, asm

def writeLogicLessThen( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\tcmpl \t%eax, %ecx\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsetl \t%al\n" )

	return rest, asm

def writeLogicGreaterThen( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\tcmpl \t%eax, %ecx\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsetg \t%al\n" )

	return rest, asm

def writeLogicOr( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\torl \t%ecx, %eax\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsetne \t%al\n" )

	return rest, asm

def writeLogicAnd( ast, asm ):
	l = []
	l.append( ast[1] )
	rest, asm = writeGen( l, asm )
	asm.append( "\tpush \t%eax\n" )
	rest, asm = writeGen( ast[2:], asm )
	asm.append( "\tpop \t%ecx\n" )
	asm.append( "\tcmpl \t$0, %ecx\n" )
	asm.append( "\tsetne \t%cl\n" )
	asm.append( "\tcmpl \t$0, %eax\n" )
	asm.append( "\tmovl \t$0, %eax\n" )
	asm.append( "\tsetne \t%al\n" )
	asm.append( "\tandb \t%cl, %al\n" )

	return rest, asm

def writeFunction( ast, asm ):
	asm.append( "\tpush \t%ebp\n" )
	asm.append( "\tmovl \t%esp, %ebp\n" )
	rest, asm = writeGen( ast[1:], asm )
	asm.append( "\tmovl \t%ebp, %esp\n" )
	asm.append( "\tpop \t%ebp\n" )

	return rest, asm

variableMap = {}

def writeVariableD( ast, asm ):
	
	rest, asm = writeGen( ast[1:], asm )
	
	r = re.compile('.*eax')
	
	if filter( r.match, asm ):	

		asm.insert( asm.index( filter( r.match, asm )[-1] ) + 1, "\tpushl \t%eax\n" )	
	
	else:
		asm.append( "\tmovl \t$0, %eax\n" )
		asm.append("\tpushl \t%eax\n")

	variableMap[ast[0][4:]] = size - (len(variableMap)*4)


	return rest, asm


def writeGen( ast, asm = g ):
	if ast:
		if ast[0] == "Program":
			rest, asm = writeGlobl( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "Return":
			rest, asm = writeRet( ast, asm )
			writeGen( rest, asm )

		elif isinstance( ast[0], int ):
			rest, asm = writeMov( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "neg":
			rest, asm = writeNeg( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "!":
			rest, asm = writeNot( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "+":
			rest, asm = writeSum( ast, asm )
			writeGen( rest, asm )
		
		elif ast[0] == "*":
			rest, asm = writeMult( ast, asm )
			writeGen( rest, asm )
		
		elif ast[0] == "-":
			rest, asm = writeMinus( ast, asm )
			writeGen( rest, asm )	
		
		elif ast[0] == "/":
			rest, asm = writeDiv( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "==":
			rest, asm = writeLogicEqual( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "!=":
			rest, asm = writeLogicNotEqual( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "<":
			rest, asm = writeLogicLessThen( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == ">":
			rest, asm = writeLogicGreaterThen( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == ">=":
			rest, asm = writeLogicGreaterThenOrEqual( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "<=":
			rest, asm = writeLogicLessThenOrEqual( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "||":
			rest, asm = writeLogicOr( ast, asm )
			writeGen( rest, asm )

		elif ast[0] == "&&":
			rest, asm = writeLogicAnd( ast, asm )
			writeGen( rest, asm )

		elif str( ast[0] ).startswith("Function"):
			rest, asm = writeFunction( ast, asm )
			writeGen( rest, asm )

		elif str( ast[0] ).startswith("int:"):
			rest, asm = writeVariableD( ast, asm )
			writeGen( rest, asm )

		else:
			writeGen( ast[1:], asm )
		
	return [], asm 


def gen( ast, asmProg = g ):
	t = [node.name for node in PreOrderIter( ast )]
	
	g = writeGen( t, asmProg )[1]
	
	if "\tret\n" in g:
		g.append("\tret\n")
		g.remove("\tret\n")

	return g
