#Serrano Sanchez Bryant Ricardo
#Compiladores - Lexer

from sys import *

#read content from file
def open_file(file):
	data = open(file,"r").read()
	return data


def lex(content):
	token = ""
	flag_s = 0
	string = ""
	lexer = []
	#save the content as list
	content = list(content)

	
	for char in content:
		token += char
		#not erase a space, tab or line jump when inside a string
		if token == " " and flag_s != 1:
			#print("found a white space")
			token = ""

		elif token == '\t' and flag_s != 1:
			#print("found a tab")
			token = ""

		elif token == '\n' and flag_s != 1:
			#print("found a jump line")
			token = ""
		
		#case of an open or close brace
		elif token == "{":
			new_item = []
			new_item.append("openBrace")
			new_item.append(token)
			

			lexer.append(new_item)
			

			token = ""

		elif token == "}":
			new_item = []
			new_item.append("closeBrace")
			new_item.append(token)

			lexer.append(new_item)


			token = ""

		#case of an open or close parenthesis
		elif token == "(":
			new_item = []
			new_item.append("openParenthesis")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == ")":
			new_item = []
			new_item.append("closeParenthesis")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""		

		#case of a semicolon
		elif token == ";":
			new_item = []
			new_item.append("semicolon")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""			

		#case of declaring an int type
		elif token == "int":
			new_item = []
			new_item.append("INT KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		#case of declaring a returning value
		elif token == "return":
			new_item = []
			new_item.append("RETURN KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""


		#case in use of an int type variable(0-9)
		elif token == "0":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""


		elif token == "1":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "2":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "3":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "4":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "5":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "6":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = "" 

		elif token == "7":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""

		elif token == "8":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = "" 

		elif token == "9":
			new_item = []
			new_item.append("ID INT")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""


		#case of using main keyword
		elif token == "main":
			new_item = []
			new_item.append("MAIN KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""


		#case of using print keyword
		elif token == "print":
			new_item = []
			new_item.append("PRINT KEYWORD")
			new_item.append(token)
			lexer.append(new_item)
			
			token = ""


		#case of declaring a string type
		elif token == "\"":
			if flag_s == 0:
				flag_s = 1
			elif flag_s == 1:
				new_item.append("ID STRING")
				new_item.append(string)
				lexer.append(new_item)
				
				
				string = ""
				flag_s = 0

		elif flag_s == 1:
			string += char
			token = ""

	#tagging tokens
	print(lexer)
	
def run():
    #file's name goes as second parameter in command line
	data = open_file(argv[1])
	lex(data)

run() 


