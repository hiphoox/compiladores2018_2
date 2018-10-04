(* A token in a C progrm *)
type token =
    | IntKeyword
    | ReturnKeyword
    | Int of int
    | Id of string
    | OpenParen
    | CloseParen
    | OpenBrace
    | CloseBrace
    | Semicolon
