
# coding: utf-8

# In[ ]:

tkns=[]
def scanner():
    f=open("return_2.c", "r")
    for linea in f:
        palabra=""
        linea=linea.strip(" ").rstrip(" ")
        for j in linea:
            if j == "(" or j == ")" or j == "{" or j== "}" or j==";" or j=="2":
                if palabra != "":
                    tkns.append(palabra)
                tkns.append(j)
                palabra=""
            elif j != " ":
                palabra+=j
            else:
                tkns.append(palabra)
                palabra=""
    f.close()
scanner()
print(tkns)

