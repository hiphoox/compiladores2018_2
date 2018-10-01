(*Definicion de tokens para identificar un programa en C*)

type token = (*definimos un tipo llamado token*)
	| OpenBrace
	| CloseBrace
	| OpenParen
	| CloseParen
	| Semicolon 
	| IntKeyword (*Para identificar el int de "int main(usw.)"*)
	| MainKeyword (*Para identificar la palabra "main"*)
	| ReturnKeyword (*Identifica el "return"*)
	| Int of int (*Así ubicamos a los números como token tipo Int con un valor int*)
	| Error
	
(*Con todo lo anterior, ya podemos identificar todas las partes de un
* "int main() {return 2;}"
* Referencias para la definicion de tokens tomadas del repositorio de Nora Sandler
* Notas principalmente para justificar que no es una copia y entiendo qué hacen las lineas escritas
*)