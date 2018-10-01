#!/bin/bash
#for i in `seq 1 6`;
#   do
#      python3 imprimeTokens.py $i.c
#done  

python3 parser.py missing_paren.c
python3 parser.py missing_retval.c
python3 parser.py no_brace.c
python3 parser.py no_semicolon.c
python3 parser.py no_space.c
python3 parser.py wrong_case.c