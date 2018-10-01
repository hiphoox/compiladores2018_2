(* Mauricio Esparza, lexer para idetificar C*)

(* val lexer : string -> token list = <fun>*)
let lexer input =
let input = String.trim input in
lex (worderlist (partidor (nuke input)))

(* val lex : char list list -> token list *)
let rec lex words = (*words = [['i';'n';'t'];['m';'a';'i';'n'];['('];[')'];usw.]*)
	let open Tokens in
	match words with
	|[] -> []
	|['(']::rest -> OpenParen::(lex rest)
	|[')']::rest -> CloseParen::(lex rest)
	|['{']::rest -> OpenBrace::(lex rest)
	|['}']::rest -> CloseBrace::(lex rest)
	|[';']::rest -> Semicolon::(lex rest)
	|c::rest -> kwd_compare c::(lex rest)

(*trampas sucias y mañosas*)
let kwd_compare kwd =
	let open Tokens in
	match kwd with
	|'i'::'n'::'t'::[] -> IntKeyword
	|'m'::'a'::'i'::'n'::[] -> MainKeyword
	|'r'::'e'::'t'::'u'::'r'::'n'::[] -> ReturnKeyword
	|'2'::[] -> Int 2
	|_ -> Error

(*val string_of_charl : char list -> string = <fun>*)
let string_of_charl cl =
	let buf = Buffer.create 16 in
	List.iter (Buffer.add_char buf) cl;
	Buffer.contents buf

(* val worderlist : char list -> char list = <fun>
Función para llamar sin campo de error a la función Worderlist*)
let worderlist cl = worderlist_inner cl 0

(*val worderlist_inner : char list -> int -> char list list = <fun>
Regresa una lista de listas de chars que estaban en la primer lista separadas por un espacio en blanco*)
let rec worderlist_inner cl i=
	let cl = drop i (limpiador cl) in
	match cl with
	[] -> []
	|_ -> separador (limpiador cl)::worderlist_inner cl (List.length (separador (limpiador cl)))

(*val drop : int -> a' list -> a' list = <fun>
quita los primeros n elementos de una a' list*)
let rec drop n l=
	if n = 0 then l else
		match l with
		[] -> []
		|h::t -> drop (n-1) t

(* val partidor cl : char list -> char list = <fun>
separa los parentesis, corchetes y punto y coma de las otras palabras*)
let rec partidor cl =
	match cl with
	[] -> []
	|h::t -> if isOtherToken h 
			 then [' ']@[h]@partidor t 
			 else [h]@partidor t

(* val isOtherToken : char -> bool = <fun>
identifica si un caracter es un token*)
let isOtherToken c =
	match c with
	'(' -> true
	|')' -> true
	|'}' -> true
	|'{' -> true
	|';' -> true
	|_ -> false

(*val separador : char list -> char list = <fun>
recibe una char list y regresa la primer char list antes de espacio en blanco*)
let rec separador cl =
	match cl with
	[] -> []
	|h::t -> if h = ' ' then [] else [h]@separador t;;
 
 (*val limpiador : char list -> char list = <fun>
 recibe una cadena y quita los espacios en blanco antes de un caracter*)
let rec limpiador cl =
	match cl with
	[] -> []
	|' '::t -> limpiador t
	|h::t -> cl;;

let rec nuke_inner s i =
	if (String.length s) = i then [] else s.[i]::nuke_inner s (i+1)

let nuke s = nuke_inner s 0

let token_to_string t =
	let open Tokens in 
	match t with 
	| OpenBrace -> "{"
	| CloseBrace -> "}"
	| OpenParen -> "("
	| CloseParen -> ")"
	| Semicolon -> ";"
	| IntKeyword -> "INT" 
	| MainKeyword -> "MAIN"
	| ReturnKeyword -> "RETURN"
	| Error -> "TOKEN NO RECONOCIDO, ERROR"
	| Int i -> Printf.sprintf "INT<%d>" i 