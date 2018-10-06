open Lex 
open Parse
open Gen




let toks2 = Lex.lex "int main() { return -210; }" 
(*tok_to_strign => funcion para  hacer que de vuelve los token como una Lista de String*)
let tok_strs2 = List.map Lex.tok_to_string toks2
let _ = List.iter (Printf.printf "%s ," ) tok_strs2
let ast = Parse.parse toks2




let _ = Gen.generate ast






