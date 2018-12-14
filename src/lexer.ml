(* Mauricio Esparza, lexer para idetificar C*)
let token_to_string t =
	match t with 
	| Tokens.OpenBrace -> "{"
	| Tokens.CloseBrace -> "}"
	| Tokens.OpenParen -> "("
	| Tokens.CloseParen -> ")"
	| Tokens.Semicolon -> ";"
	| Tokens.IntKeyword -> "INT" 
	| Tokens.MainKeyword -> "MAIN"
	| Tokens.ReturnKeyword -> "RETURN"
	| Tokens.Error -> "TOKEN NO RECONOCIDO, ERROR"
	| Tokens.Int i -> Printf.sprintf "INT<%d>" i
	| Tokens.Id s -> Printf.sprintf "ID<%s>" s

let print_toklist tl =
	List.iter (fun x -> let s = token_to_string x in print_string s; print_newline ()) tl;;

(*val string_to_charlist_inner : string -> int -> char list = <fun>
Recibe un string y un índice para devolver la cadena en formato de char list*)
let rec string_to_charlist_inner s i =
if (String.length s) = i then [] else s.[i]::string_to_charlist_inner s (i+1)

(*val string_to_charlist : string -> char list
Método para llamar a string_to_charlist_inner y no equivocarse en el índice*)
let string_to_charlist s = string_to_charlist_inner s 0

(*val clean_charlist : char list -> char list = <fun>
recibe una cadena y quita los espacios en blanco antes de un caracter*)
let rec clean_charlist cl =
	match cl with
	[] -> []
	|' '::t -> clean_charlist t
	|h::t -> cl;;

(*val get_charlist_word : char list -> char list = <fun>
recibe una char list y regresa la primer char list antes de espacio en blanco*)
let rec get_charlist_word cl =
	match cl with
	[] -> []
	|h::t -> if h = ' ' then [] else [h]@get_charlist_word t;;

(* val is_other_token : char -> bool = <fun>
identifica si un caracter es un token*)
let is_other_token c =
	match c with
	'(' -> true
	|')' -> true
	|'}' -> true
	|'{' -> true
	|';' -> true
	|_ -> false

(* val isolate_punctuation : char list -> char list = <fun>
separa los parentesis, corchetes y punto y coma de las otras palabras*)
let rec isolate_punctuation cl =
	match cl with
	[] -> []
	|h::t -> if is_other_token h 
			 then [' ']@[h]@isolate_punctuation t 
			 else [h]@isolate_punctuation t

(*val drop : int -> a' list -> a' list = <fun>
quita los primeros n elementos de una a' list*)
let rec drop n l=
	if n = 0 then l else
		match l with
		[] -> []
		|h::t -> drop (n-1) t

(*val wordList_inner : char list -> int -> char list list = <fun>
Regresa una lista de listas de chars que estaban en la primer lista separadas por un espacio*)
let rec wordList_inner cl i=
	let cl = drop i (clean_charlist cl) in
	match cl with
	[] -> []
	|_ -> get_charlist_word (clean_charlist cl)::wordList_inner cl (List.length (get_charlist_word (clean_charlist cl)))

(* val wordList : char list -> char list = <fun>
Función para llamar sin campo de error a la función wordList*)
let wordList cl = wordList_inner cl 0

(* val string_of_chars : char list -> string = <fun> 
toma una lista de caracteres y la devuelve en forma de string *)
let string_of_chars chars =
	let buf = Buffer.create 16 in
	List.iter (Buffer.add_char buf) chars;
	Buffer.contents buf

(* val int_token : char -> token = <fun>
Recibe un char y, de ser un entero, regresa su token
*)
let cmplx_token c =
	try 
		if int_of_string (string_of_chars c) >= 0 
			then Tokens.Int (int_of_string (string_of_chars c)) 
		else Tokens.Id (string_of_chars c)
	with 
		Failure "int_of_string" -> Tokens.Id (string_of_chars c)
 
(*trampas sucias y mañosas
val kwd_compare : char list -> token = <fun>
Recibe una char list y regresa su equivalente Token.
En caso de no encontrar un similar, devuelve el token Error. Sustituir lo más pronto posible por "raise token_not_found", xfas.
*)
let kwd_compare kwd =
	match kwd with
	|'i'::'n'::'t'::[] -> Tokens.IntKeyword
	|'m'::'a'::'i'::'n'::[] -> Tokens.MainKeyword
	|'r'::'e'::'t'::'u'::'r'::'n'::[] -> Tokens.ReturnKeyword
	| _ -> cmplx_token kwd

(* val lex : char list list -> token list *)
let rec lex words = (*words = [['i';'n';'t'];['m';'a';'i';'n'];['('];[')'];usw.]*)
	match words with
	|[] -> []
	|['(']::rest -> Tokens.OpenParen::(lex rest)
	|[')']::rest -> Tokens.CloseParen::(lex rest)
	|['{']::rest -> Tokens.OpenBrace::(lex rest)
	|['}']::rest -> Tokens.CloseBrace::(lex rest)
	|[';']::rest -> Tokens.Semicolon::(lex rest)
	|c::rest -> kwd_compare c::(lex rest)

(* val errores : token list -> bool = <fun>
recibe una lista de tokens y dice si contiene o no errores de lexer*)
let rec errores tl =
	match tl with
	[]->false
	|h::t -> if h = Tokens.Error then true else errores t

(* val map : a' list -> <fun> -> a' list = <fun>
función que recibe una 'a list y una función y la aplica a cada elemento de una lista*)
let rec map l f =
	match l with
	[] -> []
	|h::t -> f h::map t f

(* val lexer : string -> int -> token list = <fun>
Recibe una cadena con código a tokenizar y regresa su lista de tokens*)
let lexer input line=
let input = String.trim input in
let toks = lex (wordList (isolate_punctuation (string_to_charlist input))) in
if errores toks then (print_string "Error en la línea: ";print_int line;print_newline ();toks) else toks

(* val toks_from_channel : in_channel -> token list = <fun>
Recibe un canal de entrada y recorre el archivo para devolver su lista de tokens*)
let toks_from_channel in_channel =
	let toks = ref [] in
	let lines = ref 0 in
		try
			while true do
				let line = input_line in_channel in
				lines := !lines +1;
				toks := (!toks)@(lexer line !lines)
			done;
			[Tokens.Error]
		with
		| End_of_file -> !toks

(* val toks_from_filename : string -> token list = <fun>
Recibe el nombre de un archivo y, de existir, regresa su lista de tokens*)
let toks_from_filename filename =
	let ch = open_in filename in
		let toks = toks_from_channel ch in
			close_in ch;
			toks