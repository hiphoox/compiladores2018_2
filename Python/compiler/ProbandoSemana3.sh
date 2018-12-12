#!/bin/bash
echo '\-------------Pruebas primer semana--------------/'
echo '***Válidas***'
for i in "add" "associativity" "associativity_2" "div" "mult" "parens" "precedence" "sub" "sub_neg" "unop_add" "unop_parens"
do
	python3 main.py ../test_codes/stage_3/valid/$i.c
done


echo '***Inválidas***'
for i in "malformed_paren" "missing_first_op" "missing_second_op" "no_semicolon" 
do
	python3 main.py ../test_codes/stage_3/invalid/$i.c
done

