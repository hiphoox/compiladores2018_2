#!/bin/bash
echo '\-------------Pruebas primer semana--------------/'
echo '***Válidas***'
for i in "multi_digit" "newlines" "no_newlines" "return_0" "return_2" "spaces"
do
	python3 main.py ../test_codes/stage_1/valid/$i.c
done


echo '***Inválidas***'
for i in "missing_paren" "missing_retval" "no_brace" "no_semicolon" "no_space" "wrong_case"
do
	python3 main.py ../test_codes/stage_1/invalid/$i.c
done

