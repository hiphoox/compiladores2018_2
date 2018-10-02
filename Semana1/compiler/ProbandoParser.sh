#!/bin/bash

for i in "missing_paren" "missing_retval" "no_brace" "no_semicolon" "no_space" "wrong_case"
do
	python3 main.py ../parser_test/$i.c
done
