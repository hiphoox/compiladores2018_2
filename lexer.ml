(*----------Funciones no relacionadas con el programa principal---------*)

(*Recibe una linea (string) y regresa una lista de tokens*)
let string_to_char_list s =
  let rec exp i l =
    if i < 0 then l else exp (i - 1) (s.[i] :: l) in
    exp (String.length s - 1) []


(*Recibe una lista de chars y regresa una string compuesta de los chars*)
let char_list_to_string char_list = 
  String.concat ("") (List.map (String.make 1) char_list)




(*--------------Declaracion de expresiones regulares--------------------*)

let int_regexp = Str.regexp_case_fold "\\(\\([0-9]+\\)\\|\\(0x[0-9a-f]+\\)\\)\\(\\b.*\\)"

let id_regexp = Str.regexp "\\([A-Za-z_][A-Za-z0-9_]*\\)\\(\\b.*\\)"




(*--------------------------Funciones principales-----------------------*)
let get_id id_string = 
  let open TokenTypes in
    match id_string with
      |"return" -> ReturnKeyword
      |"int" -> IntKeyword
      |_ -> Id id_string


(*tokeniza cadenas de numeros o keywords, recibe una cadena y revisa si
  hay match con la expresion regular (int, char o keyword)*)
(*(string -> (token,string)*)
let lex_especial strg (*string*) = 
  if Str.string_match int_regexp strg 0 (*match expresion regular y cadena*)
  then 
    (*regresa la n subcadena que hace match con la ultima cadena utilizada
      en String_match match*)
    let int_string = Str.matched_group 1 strg in
    let int_value = int_of_string int_string in  (*convierte string a numero*)
    let rest = Str.matched_group 4 strg in
      (TokenTypes.Int int_value), rest 
      (*devuelve el token y el resto de la cadena (tupla), el 
        4 es para solo regresar hasta el 4 grupo encontrado (ver expresion
        regular)*)
  else 
  if Str.string_match id_regexp strg 0 (*ID*)
  then
    let id_string = Str.matched_group 1 strg in
    let rest = Str.matched_group 2 strg in
    let token = get_id id_string in
      token, rest
  else
    failwith ("Caracter invalido ->|"^strg^"|")


(*crea un lista de tokens, si el token es tipo numero o keyword se procesa
  de manera especial*)
let rec lex_numbers_ids char_list =
  let str = String.trim (char_list_to_string (char_list)) in
  let token, rest = lex_especial str in
    token::(lex_rest (string_to_char_list rest))


(*recibe una lista de chars y realiza el match para devolver el tipo de 
  token*)
(*char list -> unit*)
and lex_rest char_list = 
  let open TokenTypes in
    match char_list with
      | [] -> []
      | '{'::rest -> OpenBrace::(lex_rest rest)
      | '}'::rest -> CloseBrace::(lex_rest rest)
      | '('::rest -> OpenParen::(lex_rest rest)
      | ')'::rest -> CloseParen::(lex_rest rest)
      | ';'::rest -> Semicolon::(lex_rest rest)
      |otherChar::tail ->
          if ((Char.equal ' ' otherChar) || (Char.equal '\r' otherChar)) then lex_rest tail
          else lex_numbers_ids char_list


(*tokeniza los caracteres de una cadena de texto*)
(*string -> unit*)
let lex linea =
  let linea_trim = String.trim linea in
    lex_rest (string_to_char_list linea_trim)

(* recibe un token y lo imprime*)
(*token -> string*)
let token_to_string t =
  let open TokenTypes in
    match t with
      | OpenBrace -> "{ "
      | CloseBrace -> "} "
      | OpenParen -> "( "
      | CloseParen -> ") "
      | Semicolon -> "; "
      | IntKeyword -> "INT "
      | ReturnKeyword -> "RETURN "
      | Int i -> Printf.sprintf "INT<%d> " i
      | Id id -> Printf.sprintf "ID<%s> " id
