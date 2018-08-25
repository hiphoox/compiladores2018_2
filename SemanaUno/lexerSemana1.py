from enum import Enum

otros=['{','}','[',']','(',')',';','.']

class Token(Enum):
	CorcheteIzq="{"
	CorcheteDer="}"
	ParentesisIzq="("
	ParentesisDer=")"
	PuntoYComa=";"
	ReturnReservado="return"
	IntReservado="int"


tokens=[]
temp2=[]
temporal=[]
asciis=[]
j=0
k=0

def junta(temp,temp2):
	juntaLetra=""
	for x in range(0, len(temp2)):
		for y in range(0,len(temp2[x])):
			juntaLetra=juntaLetra+temp2[x][y]
			
		temporal.append(juntaLetra)
		juntaLetra=""

def esLetra(i,tam,texto):
	juntaLetra=""
	temp=[]
	while texto[i].isalpha() or texto[i].isdigit() or texto[i]=='_':
		
		temp.append(texto[i])
		i+=1
	temp2.append(temp)
	junta(temp,temp2)	

def creaListaTokens(texto):
	tam=len(texto)
	cant=len(otros)
	juntaLetra=""
	for a in range(0,tam):
		asciis.append(int(ord(texto[a])))

	n=0
	i=0

	juntaLetra=""
	i=0
	while i<tam:
		if texto[i].isdigit():

			while texto[i].isdigit():
				n=10*n+asciis[i]-48
				i+=1

			temporal.append(n)
			n=0

		if texto[i].isalpha()==True:
			temp=[]
			while texto[i].isalpha() or texto[i].isdigit() or texto[i]=='_':
				
				temp.append(texto[i])
				i+=1
			temp2.append(temp)
			junta(temp,temp2)
			temp2[:]=[]

		if texto[i] in otros:
			temporal.append(texto[i])
					
		i+=1

	return idToken(temporal)


def idToken(temporal):
	temp3=[]
	for elemento in temporal:
	
		if elemento=="{":
			temp3.append(Token.CorcheteIzq.name)
			temp3.append(Token.CorcheteIzq.value)
			tokens.append(temp3)
			temp3=[]
		elif elemento=="}":
			temp3.append(Token.CorcheteDer.name)
			temp3.append(Token.CorcheteDer.value)
			tokens.append(temp3)
			temp3=[]
		elif elemento=="(":
			temp3.append(Token.ParentesisIzq.name)
			temp3.append(Token.ParentesisIzq.value)
			tokens.append(temp3)
			temp3=[]
		elif elemento==")":
			temp3.append(Token.ParentesisDer.name)
			temp3.append(Token.ParentesisDer.value)
			tokens.append(temp3)
			temp3=[]
		elif elemento==";":
			temp3.append(Token.PuntoYComa.name)
			temp3.append(Token.PuntoYComa.value)
			tokens.append(temp3)
			temp3=[]
		elif elemento=="return":
			temp3.append(Token.ReturnReservado.name)
			temp3.append(Token.ReturnReservado.value)
			tokens.append(temp3)
			temp3=[]
		elif elemento=="int":
			temp3.append(Token.IntReservado.name)
			temp3.append(Token.IntReservado.value)
			tokens.append(temp3)
			temp3=[]
		else:
			if type(elemento)==str:
				temp3.append("iD")
				temp3.append(elemento)
				tokens.append(temp3)
				temp3=[]
			else:
				temp3.append(type(elemento))
				temp3.append(elemento)
				tokens.append(temp3)
				temp3=[]

	return tokens	