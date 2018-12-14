g = []
	
def writeGlobl( ast, asmProg = g ):
    if ast[0] == "Program":
        asmProg.append("\t.globl main\n")
        return asmProg
 
def writeMain( ast, asmProg = g ):
    if ast[0] == "main":
        asmProg.append( "main:\n")
        return asmProg
        
def writeRet( ast, asmProg = g):
    if ast[0] == "Return":
        m = writeMov(ast[1:], asmProg)
        asmProg.append("\tret\n")
        return asmProg

def writeNeg( ast, asmProg = g ):
	if ast[0] == "-":
		asmProg.append("neg\t%eax\n")
		return asmProg

def writeMov( ast, asmProg = g ):
    if ( isinstance(ast[0], int) ):
        asmProg.append("\tmovl\t$"+str(ast[0])+", %eax\n") 
        return asmProg

def gen( ast, asm = g ):
    if ast:
        if writeGlobl(ast, asm):
            gen( ast[1:], asm  )
        
        if writeMain(ast, asm):
            gen( ast[1:], asm )
        
        if writeRet(ast, asm):
            gen( ast[1:],asm)

        if writeNeg( ast, asm ):
        	gen( ast[1:],asm )
    else:
        return asm
