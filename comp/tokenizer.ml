let a_lista s = 
    let rec a_lista_rec substr substr_len =
        match substr with
        | "" -> [] | _ -> (String.get substr 0)::a_lista_rec (String.sub substr 1 (substr_len - 1)) (substr_len - 1)
    in
a_lista_rec s (String.length s)
	let rec a_cadena chars =
		match chars with
		| [] -> "" | c::cs -> String.make 1 c ^ a_cadena cs
module Tknzer : sig
    type token = 
        | OpenBrace
        | CloseBrace
        | OpenParen
        | CloseParen
        | Semicolon
        | IntKeyword
        | ReturnKeyword
        | Int of int
        | Id of string
	val t_a_cadena: token -> string
    val tknzer : string -> token list
    
end =
	struct
        type token = 
            | OpenBrace
            | CloseBrace
            | OpenParen
            | CloseParen
            | Semicolon
            | IntKeyword
            | ReturnKeyword
            | Int of int
            | Id of string 
        let trae_int = Str.regexp "\\(-?[0-9]+\\)\\(\\b.*\\)"
        let trae_id = Str.regexp "\\([A-Za-z][A-Za-z0-9_]*\\)\\(\\b.*\\)"
        let identificado input =
             if Str.string_match trae_id input 0
            then
                let id_token_str = Str.matched_group 1 input in
                let rest = Str.matched_group 2 input in
                let id_token = 
                    match id_token_str with
                    | "return" -> ReturnKeyword
                    | "int" -> IntKeyword
                    | _ -> Id(id_token_str)
                in
                    (id_token, rest)
            else if Str.string_match trae_int input 0
            then 
                let int_token = Str.matched_group 1 input in
                let rest = Str.matched_group 2 input in
                    (Int(int_of_string int_token), rest)
            else
                failwith ("Syntax error: \""^input^ "\" caracter no reconocido")
         let rec tknzer input = 
            let input = String.trim input in 
                if String.length input = 0
                then []
                else
                    let tok, remaining_program = 
                        match a_lista input with
                        | '{'::rest -> (OpenBrace, a_cadena rest)
                        | '}'::rest -> (CloseBrace, a_cadena rest)
                        | '('::rest -> (OpenParen, a_cadena rest)
                        | ')'::rest -> (CloseParen, a_cadena rest)
                        | ';'::rest -> (Semicolon, a_cadena rest)
                        | _ -> identificado input
                    in
                    tok :: (tknzer remaining_program)
         let t_a_cadena t =
            let s = 
                match t with
                | OpenBrace -> "{"
                | CloseBrace -> "}"
                | OpenParen -> "("
                | CloseParen -> ")"
                | Semicolon -> ";"
                | IntKeyword -> "INT"
                | ReturnKeyword -> "RETURN"
                | Int i -> Printf.sprintf "INT(%d)" i
                | Id id -> Printf.sprintf "ID(%s)" id
            in
            s
     end
	 
let tokens = Tknzer.tknzer "int main() { return 2; }" 
let cadena_t = List.map Tknzer.t_a_cadena tokens;;
let _ = List.iter (Printf.printf "%s ," ) cadena_t
