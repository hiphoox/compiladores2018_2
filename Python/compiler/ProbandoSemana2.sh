#!/bin/bash
echo '\-------------Pruebas primer semana--------------/'
echo '***Válidas***'
for i in "bitwise" "bitwise_zero" "neg" "nested_ops" "nested_ops_2" "not_five" "not_zero"
do
	python3 main.py ../test_codes/stage_2/valid/$i.c
done


echo '***Inválidas***'
for i in "missing_const" "missing_semicolon" "nested_missing_const" "wrong_order" 
do
	python3 main.py ../test_codes/stage_2/invalid/$i.c
done

