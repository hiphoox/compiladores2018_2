open Lex 
open Parse
open Gen

let toks = Lex.lex "char holaa() { return -210; }" 
(*tok_to_strign => funcion para  hacer que de vuelve los token como una Lista de String*)
let tok_strs = List.map Lex.tok_to_string toks
let _ = List.iter (Printf.printf "%s ," ) tok_strs
let ast = Parse.parse toks
let _ = Gen.generate ast






