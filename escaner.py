import sys, os, re

tokens=[]

#nombre = raw_input("Ingresa el nombre del archivo con la terminacion del mismo:")
archivo = open("return2.txt", 'r')
for linea in archivo.readlines():

	if (re.search("int",linea)):
		tokens.append(["IntKeyword","int"])
	if (re.search("main",linea)):
		tokens.append(["","main"])
	if (re.search("char",linea)):
		tokens.append(["CharKeyword","char"])
	if (re.search("return",linea)):
		tokens.append(["ReturnKeyWord","return"])

	for char in linea:
		
		if char == '{':
			tokens.append(["OpenBrace",char])
		if char == '}':
			tokens.append(["CloseBrace",char])
		if char == '(':
			tokens.append(["OpenParen",char])
		if char == ')':
			tokens.append(["CloseParen",char])
		if char == ";":
			tokens.append(["Semicolon",char])
		if char =='2':
			tokens.append(["Int",char])
		
		
	
print(tokens)

archivo.close()

