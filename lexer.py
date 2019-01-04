#use re module for regular expressions
import re 

#list by default
t = []

#set of regular expressions
c  = '[-\*/(){};~\+]|&&|==|<=|>=|<|>|!=|!|[|]{2}|=' 	#single character
n  = '\d+'							#number
w  = '\w+'							#word

#list of reserved words
reserved = ["int","return"]

#dictionay to tag single tokens
tag = {	'(':"OpenPa",	')':"ClosePa",	'{':"OpenBr",	'}':"CloseBr",
		';':"SemiC",	'-':"Minus",	'+':"Plus",		'/':"Div",
		'*':"Mult",		'~':"BitwiseComplement",		'!':"LogicalNegation",
		'<':"LessThen",	'>':"GreaterThen",'&&':'AND',	'||':"OR",
		'==':"Equal",	'!=':"NotEqual",'<=':"LessThenOrEqual",'>=':"GreaterThenOrEqual",
		'=':"Assignment"		
		}

def startsWith( program ):
	if program and re.match( c, program ): 
		a = re.match( c, program)
		return a.group(), program[len( a.group() ):] 
	else: return ( "None",program )

def getDoubleChar( program ):
	if program and re.match( cc, program ):
		a = re.match( cc,program )
		return ( tag[a.group()], program[2:] )

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
			if token == "Invalid":
				token = input[0]
			l.append( token )

		if len( remainingProgram ) != 0: lexRawTokens( remainingProgram, l )
		return l

#lex function to remove break lines and empty spaces
def lex( program_text,l = t ):

	if not program_text:
		print("Lexer Error: Nothin to tokenize")
		exit()

	program = re.split( '\s', program_text.strip() )

	for item in program:
		a = lexRawTokens( item, l )
		for token in l:
			if str(token) in program_text: 
				print("Lexer Error in position "+str(program_text.index(token))+". Invalid Token: "+token)
				exit()
	return l
