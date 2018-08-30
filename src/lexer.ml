(* Mauricio Esparza, lexer para idetificar C*)
(*OCaml se construye de abajo para arriba*)
(*Nora usa explode, yo uso nuke porque explode no existe en mi OCaml*)

(*Necesitas una función que guarde en una lista a todo caracter que esté antes de un espacio
* Ya que encuentres un espacio, le das implode, lo comparas con tus kwds.
* Nota pedorra: List.concat es para concatenar listas List.concat a b -> [a; b]
* Una vez que logres hacer eso, pues ya implodeas tus palabras y comparas :3
*)

let kwd_compare kwd =
	let kwd = Lexer.nuke kwd in
	let open Tokens in
	match kwd with
	|"INT" -> IntKeyword
	|"MAIN" -> MainKeyword
	|"RETURN" -> ReturnKeyword
	| _ -> Printf.sprintf "VALOR NO RECONOCIDO"




(*Lex_word_id te regresa una palabra completa dentro del input principal
* i.e., regresa "MainKeyword" de encuentra "main() { return 2; }"
y te regresa "ReturnKeyword" de " return 2; }"
lex_word_id recibe una cadena de caracteres *)
let lex_word_id input_tokens =
	let input_tokens = String.trim input_tokens
	
	


(*ésta funcion de abajo queda pendiente, no sé aún si sí la voy a poder hacer así
* ahora mismo, trabajo con la de arriba
*
*Recibe lista de letras, debe pegarlas y encontrar si se trata de un kwd.
*Debe devolver un token y un resto porque lo llama lex_rest y eso es lo que
*esa función sabe manejar o que más bien, espera recibir
*)
let rec lex_is_keywd input_tokens =
	let input = String.trim (string_of_charl input_tokens) in(*le hacemos trim otra vez por si las moscas xd*)
	let token, rest = lex_word_id input in
	token::(lex_rest (String.nuke rest)) 
	

(* lex_rest recibe una cadena rota en partes, éste pedazo sólo identifica simbolos de 1 caracter *)
and lex_rest words = (*words = [i; n; t; " "; m; a; i; n; " "; usw.]*)
	let open Tokens in
	match words with
	(* Si la partícula es igual a (, ), [ ó ], la separa del resto y regresa su e
	*  equivalente en token junto al resultado de volver a llamar la función con el resto *)
	| [] -> [] (*En algún momento se llega al final de la lista, o sea, lista vacía []*)
	|'('::rest -> OpenParen::(les_rest rest)
	|')'::rest -> CloseParen::(lex_rest rest)
	|'{'::rest -> OpenBrace::(lex_rest rest)
	|'}'::rest -> CloseBrace::(lex_rest rest)
	| c::rest -> if (' ' = c) then lex_rest rest else lex_is_keywd words
(*lex_is_keyw recibe words, que actualmente es una lista de caracteres*)

(* La funcion lexer debe encargarse de separar e identificar cada elemento en la entrada *)
let lexer input =
	let input = String.trim input in (*Deja que la entrada sea ella misma pero recortada en:*)
	lex_rest (String.nuke input) (*Llama a la funcion lex_rest y le pasa el input separado en letras*)

let string_of_charl cl = (*Método casero para sustituir el implode*)
	let buf = BUffer.create 16 in (*HOnestidad ante todo; después de 3 horas de no poder, lo busqué en Stack Overflow*)
	List.iter (Buffer.add_char buf) cl;
	BUffer.contents buf

let nuke s i= (*Metodo casero de string_to_charlist porque explode ya no está en ocaml moderno :( *)
	let str_len = String.length s in
	let i = i + 1 in 			(*La ventaja de éste método es que puedes empezar la cadena en el índice que quieras*)
	if i = str_len then []
	else s.[i] :: nuke s i

(* convierte tokens en sus equivalentes strings *)
let token_to_string t =
	let open Tokens in (*Abre el modulo Tokens.ml para trabajar la siguiente linea*)
	match t with (*Compara la entrada t con los tokens en Tokens.ml*)
	| OpenBrace -> "{"
	| CloseBrace -> "}"
	| OpenParen -> "("
	| CloseParen -> ")"
	| Semicolon -> ";"
	| IntKeyword -> "INT" 
	| MainKeyword -> "MAIN"
	| ReturnKeyword -> "RETURN"
	| Int i -> Printf.sprintf "INT<%d>" i 
(* Llama a la funcion printf dentro del modulo Printf y le pasa los parámetros INT<%d> con d = entrada i
* se usa sprintf porque éste devuelve la cadena, printf la imprime en pantalla, 
* no queremos eso.
* lex.ml de Nora Sandler define cómo trabaja el lexer
*)
