import re
from parser import parser
from tokenizer import *


new_l=[]


            


def get_node(ast):
    ast_d = ast
    for i in ast_d:
        if isinstance(i, list):
            
            get_node(i)
        else:
            gen_code(i)
        if len(ast_d) == 1:
            gen_code(ast_d[0])
            #pop_node(ast,ast_d)
            #print(ast_d)

def gen_code(node):
    dig = re.search(r'[0-9]+',node)
    chain=re.search(r'[a-zA-Z]+',node)
    if dig:
        print(' movl  ${}, {}eax\n'.format(node, "%"))
    if chain and node != "return" and node != "int":
        print(' .globl _{}\n'.format(node))
    return 
print("\n")
print("-------------------------- assembly instructions ------------------")
get_node((parser(tokenizer('tester.c'))))