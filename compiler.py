import lexer, parser, generate

import os

from sys import*

def open_file( file ):
	data = open( file, "r" ).read()
	return data

data = open_file( argv[1] )

l = []
lexer.lex(data,l)

if "-w" in argv:
	print( data )
	exit()

if "-l" in argv:
	print( l )
	exit()

p = parser.parseProg(l)

if "-p" in argv:
	parser.printT( p )
	exit()

g = generate.gen(p)

if "-g" in argv:
	for item in g:
		print( item )
	exit()

f = open( "assembly.s","w" )

for item in g:
	f.write( item )
f.close() 

os.system( "gcc -m64 assembly.s -o out" )		

os.system( "rm assembly.s" )

"""	./out	
	echo $? 
"""
