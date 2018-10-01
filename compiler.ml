open Lexer;;

let toks = Lexer.lexer "int main() { return 2; }"

let rec map l f =
	match l with
	[] -> []
	|h::t -> f h::map t f

let prinToken t = Lexer.token_to_string t

let result = map toks prinToken