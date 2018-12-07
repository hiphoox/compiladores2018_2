#use re module for regular expressions
import re 

#list by default
t = []

#set of regular expressions
c  = '[-|*|/|(|)|{|}|;|~|!|+]' 	#single character
n  = '\d+'						#number
w  = '\w+'						#word

#list of reserved words
reserved = ["int","return"]

#dictionay to tag single tokens
tag = {	'(':"OpenPa",	')':"ClosePa",	'{':"OpenBr",	'}':"CloseBr",
	';':"SemiC",	'-':"Minus",	'+':"Plus",	'/':"Div",
	'*':"Mult",	'~':"BitwiseComplement",	'!':"LogicalNegation"
	}

def startsWith( program ):
	if program and re.match( c, program ): return ( program[0], program[1:] )
	else: return ( "None",program )

def getId( program ):
	if program and re.match( w, program ):
		a = re.match( w,program )
		if a.group() in reserved : return ( ("KW", a.group() ), program[len( a.group() ):] )
		else: return ( ("ID", a.group() ), program[len( a.group() ):] )
	else: return ( "Invalid", "" )

def getConstant( program ):
	if program and re.match( n, program ):
		a = re.match( n, program )
		return ( ( "Const", a.group() ), program[len( a.group() ):] )

def getComplexTokens( program ):
	if re.match( n, program ): return getConstant( program )
	else: return getId( program )

#recursive function to lex items
def lexRawTokens( input, l ):
	if input:
		token, remainingProgram = startsWith( input )
		if re.match( c, token ): l.append( tag[token] )
		elif token == "None":
			token, remainingProgram = getComplexTokens( remainingProgram )
			l.append( token )
		if len( remainingProgram ) != 0: lexRawTokens( remainingProgram, l )
		return l

#lex function to remove break lines and empty spaces
def lex( program_text,l = t ):
	program = re.split( '\s', program_text.strip() )
	for item in program:
		lexRawTokens( item, l )
	return l
