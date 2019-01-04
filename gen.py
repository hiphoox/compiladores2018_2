from parser import parser
from tokenizer import *

def gen_code(ast):
    return ast

gen_code((parser(tokenizer('tester.c'))))