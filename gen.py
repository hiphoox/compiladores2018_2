import re
from parser import parser
from tokenizer import *


new_l=[]


            
def get_node(ast):
    ast_d = ast
    e = ast[0]
    
    if isinstance(e, list):
        get_node(e)
    elif e != "return":
        gen_code(e)
        get_node(ast[1:])
    if len(e) == 2 and isinstance(e[1],list):
        gen_code(e[1][0])
            #pop_node(ast,ast_d)
            #print(ast_d)

def gen_code(node):
    dig = re.search(r'[0-9]+',node)
    chain=re.search(r'[a-zA-Z]+',node)
    if dig:
        print(' movl  ${}, {}eax\n'.format(node, "%"))
    if chain and node != "return" and node != "int":
        print(' .globl _{}'.format(node)+'\n'+' :_{}\n'.format(node))
    if node == "return":
        print(" ret")
print("\n")
print("-------------------------- assembly instructions ------------------")
get_node((parser(openFile('tester.c'))))