from lex import lex
from parser import parcer

file = "return_2.c"
_tokens = lex(file)
_ast = parcer(_tokens)