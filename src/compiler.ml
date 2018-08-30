open Lexer

let toks = Lexer.lexer "int main() { return 2; }"
let toks_strs = List.map Lexer.token_to_string toks
let _ List.iter (Printf.printf "%s, ") toks_strs
