#use re module for regular exprew ssions
import re 

#list "l" to stock tokens
l = []

#function to add items into list "l"
def add( a,b ):
	aux = []
	aux.append( a )
	aux.append( b )
	l.append( aux )

#set of regular expressions
c = '[-(){};~!]' 			#single character
n = '\d+'					#number
w = '[a-zA-Z]+\w*'			#word

#list of regular expressions
tokens = [c,n,w]

#list of reserved words
reserved = ["int","return"]

#dictionay to tag tokens
tag = {'(':"OPEN PA",')':"CLOSE PA",'{':"OPEN BR",'}':"CLOSE BR",';':"SEMIC",'-':"Negation",
'~':"Bitwise complement",'!':"Logical Negation",'int':"INT K",'return':"RETURN K",1:"INT",2:"IDENTIFIER"}

class Lexer:

	#unique position error and size for each instance
	def __init__( self,data ):
		self.pos_error = 0
		if len( data ) == 0: 
			print("Error: Nothin to tokenize")
			exit()
		self.size = len( data )

	#function to create list of tagged tokens
	def lex( self,data ):

		#case there's a space, \n or a \t
		if re.match( '\s',data ):

			#update position and size
			self.pos_error = self.pos_error + 1
			self.size = self.size - 1

			#calls function without space, \n or a \t (1 character)
			self.lex( data[1:] )		

		#iterate through list of tokens
		for t in tokens:

			#case there's a match
			if re.match( t,data ):

				#save match in variable
				a = re.match( t,data )

				#case matches a number
				if re.match( n,data ): add( tag[1],a.group() )

				#case matches a word
				elif re.match( w,data ):

					#case matches a word and NOT a reserverd word
					if a.group() not in reserved: add( tag[2],a.group() )

					#case matches a word and it's a keyword (reserved word)
					else: add( tag[a.group()],a.group() )

				#anyother case (single characters tokens)	
				else: add( tag[a.group()],a.group() )

				#update position and size (length of matched word)
				self.pos_error = self.pos_error + len( a.group() )
				self.size = self.size - len( a.group() )

				#after adding to list "l", calls function without the matched word
				self.lex( data[len( a.group()):] )

		#returns list of tokens if it checked the whole string
		if self.size == 0:
			return l 

		#returns error in case an unkown character is found
		else:
			print ("Lexer Error after position "+str( self.pos_error ) )
			exit()
