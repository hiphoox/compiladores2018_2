#import re

f = open ('archivo.txt','r')
mensaje = f.readlines()
ren = len(mensaje)
print(mensaje)
print('Longitud: ' + str(ren))
f.close()

tkns = {}
auxTok = ''
auxPosT = 0

for i in range(ren):
  for j in range(len(mensaje[i])):

    print(mensaje[i])
    print(mensaje[i][j])

    if (mensaje[i][j] != ' ') and (mensaje[i][j] != '\n'):
      auxTok = auxTok + mensaje[i][j]

    if (auxTok == 'int') and (mensaje[i][j+1] == ' '):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit
    
    if (auxTok == 'main') and ((mensaje[i][j+1] == ' ') or (mensaje[i][j+1] == '(')):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit

    if (auxTok == '('):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit

    if (auxTok == ')'):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit

    if (auxTok == '{'):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit

    if (auxTok == '}'):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit

    if (auxTok == 'return') and (mensaje[i][j+1] == ' '):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit

    if (auxTok in ['0','1','2','3','4','5','6','7','8','9']) and ((mensaje[i][j+1] == ' ') or (mensaje[i][j+1] == ';')):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit

    if (auxTok == ';'):
      print(auxTok)
      tkns[auxPosT] = auxTok
      auxPosT = auxPosT + 1
      auxTok = ''
      print(tkns)
      exit