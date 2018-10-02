#!/bin/bash

for i in "multi_digit" "newlines" "no_newlines" "return_0" "return_2" "spaces"
do
	python3 main.py ../lexer_test/$i.c
done

