
(*Funcion de mapeo*)
let rec map f l = 
  match l with 
      [] -> []
    |h::t -> f h :: map f t




let string_list_to_string l = String.concat "" l


(*obtiene las lineas de un archivo y devuelve un string*)
(* channel -> string *)
let read_file filename =
  let lines = ref [] in
  let chan = open_in filename in
    try
      while true; do
        lines := input_line chan :: !lines
      done; !lines
    with End_of_file ->
        close_in chan; 
        List.rev !lines

let filename = Array.get Sys.argv 1

let _ = 
  let token_list = ref [] in
  let string_list = read_file filename in
  let strg = string_list_to_string string_list in
  token_list := Lexer.lex (strg); !token_list;
  map (print_string) (map (Lexer.token_to_string) (List.rev !token_list))


(*map (print_string) (map (Lexer.token_to_string) ( ))*)

