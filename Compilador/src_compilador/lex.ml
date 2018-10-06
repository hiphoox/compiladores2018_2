(*funcion para separar string desde un cierto punto*)
let rec explode_inner s i =
    if (String.length s ) = i then [] else
        s.[i]::explode_inner s (i+1)

let explode s = explode_inner s 0

(*funcion para juntar un arreglo de char*)
let rec implode c =
    let buf = Buffer.create 16 in 
        List.iter (Buffer.add_char buf) c;
        Buffer.contents buf

(*Posible mejora valorando*)
let implode_res c =
    String.sub c 1 ((String.length c) -1)
    (*let a = explode_inner c 1 in 
            implode a*)
    
    


module Lex : sig
    type token = 
        | OpenBrace
        | CloseBrace
        | OpenParen
        | CloseParen
        | Semicolon
        | IntKeyword
        | CharKeyword
        | ReturnKeyword
        | Int of int
        | Id of string
    (* tipos de token *)
    val lex : string -> token list
    val tok_to_string: token -> string
end =

    struct
        type token = 
            | OpenBrace
            | CloseBrace
            | OpenParen
            | CloseParen
            | Semicolon
            | IntKeyword
            | CharKeyword
            | ReturnKeyword
            | Int of int
            | Id of string

        let tok_to_string t =
            match t with
            | OpenBrace -> "{"
            | CloseBrace -> "}"
            | OpenParen -> "("
            | CloseParen -> ")"
            | Semicolon -> ";"
            | IntKeyword -> "INT"
            | CharKeyword -> "CHAR"
            | ReturnKeyword -> "RETURN"
            | Int i -> Printf.sprintf "INT<%d>" i
            | Id id -> Printf.sprintf "ID<%s>" id
        (*Exprecion reular numeros positivos o negativos teniendpo en cuenta los ; juntos*)
        let int_regexp = Str.regexp "\\(-?[0-9]+\\)\\(\\b.*\\)"

        (*Exprecion reular para palabras que empiecen con letras *)
        let id_regexp = Str.regexp "\\([A-Za-z][A-Za-z0-9_]*\\)\\(\\b.*\\)"

        (*Funcion para encontrar el cuerpo del programa sin simbolos*)
        let get_kw_int_or_id input =
            (*busca cadenas con esas expreciones regulares (numeros)*)
            if Str.string_match int_regexp input 0
            then 
                (*Str.matched_group  agarra n considencia con respecto a la exprecion utilizada anterior mente*)
                let int_token = Str.matched_group 1 input in
                let rest = Str.matched_group 2 input in
                    (Int(int_of_string int_token), rest)
            (*busca cadenas con esas expreciones regulares (palabras)*)
            else if Str.string_match id_regexp input 0
            then
                (*Str.matched_group  agarra n considencia con respecto a la exprecion utilizada anterior mente*)
                let id_token_str = Str.matched_group 1 input in
                let rest = Str.matched_group 2 input in
                (*hace match con las palabras clabe que tenemos aqui (return int char )*)
                let id_token = 
                    match id_token_str with
                    | "return" -> ReturnKeyword
                    | "int" -> IntKeyword
                    | "char" -> CharKeyword
                    | _ -> Id(id_token_str) in
                    (id_token, rest)
            else
                (*sino hay considencia con ninguna exprecion entonces marca un error*)
                failwith ("Syntax error: \""^input^ "\" is not valid.")

        (*Funcion principal que quita los simbolos especiales encontrados*)
        let rec lex input = 
            let input = String.trim input in 
                if input = ""
                then []
                else
                    let tok, remaining_program = 
                        match input.[0]::[] with
                        | '{'::rest -> (OpenBrace, implode_res input)
                        | '}'::rest -> (CloseBrace, implode_res input)
                        | '('::rest -> (OpenParen, implode_res input)
                        | ')'::rest -> (CloseParen, implode_res input)
                        | ';'::rest -> (Semicolon, implode_res input)
                        | _ -> get_kw_int_or_id input in
                    tok :: (lex remaining_program)

        
    end