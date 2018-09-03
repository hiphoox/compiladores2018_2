import re

asg={"int":"INT","rint":"INT", "main":"MAIN", "return":"RETURN", "(":"Opare", ")":"CPare", "{":"Obrace", "}":"Cbrace", ";":"SEMICOLON"}
tkns=[]
patron=re.compile('[(){};]')
patron2=re.compile('\W+')
patron3=re.compile('\d')
def scanner():
    f=open("return_2.c", "r")
    for linea in f:
        linea=linea.strip(" ").rstrip(" ")
        palabra=patron.findall(linea)
        for i in palabra:
            if asg.has_key(i):
                tkns.append(asg[i])
        palabra=patron2.split(linea)
        for i in palabra:
            if asg.has_key(i):
                tkns.append(asg[i])
        palabra=patron3.findall(linea)
        if len(palabra) != 0:
            for i in palabra:
                tkns.append(asg["rint"]+"<"+i+">")
    f.close()
            
scanner()
print(tkns)

