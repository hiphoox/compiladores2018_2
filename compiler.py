import lexer, parser, generate

import os

from sys import*

def open_file( file ):
	data = open( file, "r" ).read()
	return data

data = open_file( argv[1] )

l = []
lexer.lex(data,l)

p = []
parser.parseProg(l,p)

g = []
generate.gen(p,g)ec

if len( argv ) == 3:
	if argv[2] == "-l":
		print( l )
		exit()

	if argv[2] == "-p":
		print( p )
		exit()

	if argv[2] == "-g":
		for item in g:
			print item
		exit()

f = open( "assembly.s","w" )
for item in g:
	f.write( item )
f.close() 

os.system( "gcc -m64 assembly.s -o out" )		

os.system( "rm assembly.s" )
