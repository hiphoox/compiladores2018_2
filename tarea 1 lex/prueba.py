import lex
with open("programadec.txt","r") as t:
	text = t.read() 
lex.tok(text)
