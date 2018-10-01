open Lex 
open Parse
open Gen

let toks = Lex.lex "int main() { return 2; }" 
(*tok_to_strign => funcion para  hacer que de vuelve los token como una Lista de String*)
let tok_strs = List.map Lex.tok_to_string toks
let _ = List.iter (Printf.printf "%s ," ) tok_strs
let ast = Parse.parse toks


let toks1 = Lex.lex "int main() { return -9; }" 
(*tok_to_strign => funcion para  hacer que de vuelve los token como una Lista de String*)
let tok_strs1 = List.map Lex.tok_to_string toks1
let _ = List.iter (Printf.printf "%s ," ) tok_strs1
let ast = Parse.parse toks1



let toks2 = Lex.lex "int main() { return -210; }" 
(*tok_to_strign => funcion para  hacer que de vuelve los token como una Lista de String*)
let tok_strs2 = List.map Lex.tok_to_string toks2
let _ = List.iter (Printf.printf "%s ," ) tok_strs2
let ast = Parse.parse toks2




let _ = Gen.generate ast






