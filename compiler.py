import lexer
import parser
import generate

#import os to write in terminal
import os

#to read document from terminal
from sys import*

#function to open file
def open_file( file ):
	data = open( file,"r" ).read()
	return data

#stores data from second argument in terminal
data = open_file( argv[1] ).strip()

#x for lexer
x1 = lexer.Lexer( data )
x = x1.lex( data )

#y for parser
y = parser.parse_program( x )

#z for generate
z = generate.write_asm( y )

#condition if there's a flag 
if len( argv ) == 3:
	#-l for lexer (list of tokens)
	if argv[2] == "-l":
		print x
		exit()
	#-p for parser (AST)
	if argv[2] == "-p":
		parser.printT(y)
		exit()
	#-g for generate (.s code)
	if argv[2] == "-g":
		print z
		exit()

#write assembly code
f = open( "assembly.s","w" )
f.write(z)
f.close()

#creates assembly executabe
os.system("gcc -m64 assembly.s -o out")

#erase assembly file
os.system("rm assembly.s")