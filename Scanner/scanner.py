
# coding: utf-8

# In[ ]:

tkn=[]
def compilador():
    archivo=open('C:/Users/Gerardo/Documents/Compiladores/return_2.txt','r')
    for linea in archivo:
        palabra=""
        for i in linea:
            if i != " ":
                j=str(i)
                palabra += j
            else:
                tkn.append(palabra)
                palabra=""
    archivo.close()        
compilador()
print (tkn)

