import re
from clases import *


def tokenizer(line,tokens):	
	if line != "":
				symbol = re.compile('\(|\)|\{|\}|\;|\+|\-|\~|\!|\*|\/')
				word1 = re.compile('[a-zA-Z]+')
				integers = re.compile('[0-9]+')

				token = symbol.search(line)
				if token and token.start() == 0:
					line = line.replace(token.group(),'',1)
					tokens.append(symbolss(token.group())+':'+token.group())
				token = word1.search(line)
				if token and token.start() == 0:
					line = line.replace(token.group(),'',1)
					tokens.append(words(token.group())+':'+token.group())
				token = word1.search(line)
				if token and token.start() == 0:
					line = line.replace(token.group(),'',1)
					tokens.append(words(token.group())+':'+token.group())
				token = integers.search(line)
				if token and token.start() == 0:
					line = line.replace(token.group(),'',1)
					tokens.append('INT:'+token.group())
				
				tokenizer(line.strip(),tokens)
def openFile(file):
	tokens=[]
	with open(file) as fp:
		for cnt, line in enumerate(fp):
			line = line.replace("\n", "  ").replace("-","- ").replace("~","~ ").replace("!","! ").strip()
			tokenizer(line,tokens)	
		return tokens
print("\n")	
print("--------------------------------------------------Tokens-----------------------------------------------")
print(openFile('tester.c'))
print("\n")