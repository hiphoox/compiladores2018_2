#calls modules from anytree to reed tree from parser
from anytree import Node, RenderTree, PreOrderIter

def check_program( t,c ):
	#creates assembly line for .globl (function name)
	nL = "\t.globl "+t+"\n"
	#returns new line
	return nL+c

def check_function( t,c ):
	#removes last node from tree ("main" node)
	t = t.pop()
	#creates assembly line for main
	nL = t.name+":\n"
	#returns tree(without used node) and new line + code
	return t.name,nL+c

def check_statement( t,c ):
	#removes last node from tree ("return" node)
	n = t.pop()
	#creates assembly line for return
	nL = "\tret\n"
	#returns tree(without used node) and code + new line
	return t,c+nL

#checks "cte" Node to extract value
def check_exp( t ):
	#removes last node from tree ("cte" node)
	n = t.pop()
	#creates assembly line to move value into eax register 
	nL = "\tmovl\t$"+str( n.name )+",%eax\n"
	#returns tree(without used node) and line
	return t,nL


#function to write an .s document
def write_asm( ast ):

	#saves preorder items from tree in t
	t = [node for node in PreOrderIter( ast )]

	#creates code while walks tree from bottom-up
	t,c = check_exp( t )
	t,c = check_statement( t,c )
	t,c = check_function( t,c )
	c = check_program( t,c )

	#returns final assembly code
	return c