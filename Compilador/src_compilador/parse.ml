 open Lex
 open Ast

 module Parse : sig
    val parse : Lex.token list -> AST.prog
end =
struct
   

    (*Funcion para definir el numero de el  return *)
    let parse_exp = function
        | (Lex.Int i)::rest -> (AST.Const(AST.Int(i)), rest)
        | tok::rest -> failwith("Unrecognized token "^(Lex.tok_to_string tok)^" in parse_exp Erro 4")
        | [] -> failwith("should we add a return_exp instead?")
    
    (*Funcion para checar cada uno de los tokens de el cuerpo de la funcion*)
    let rec parse_statement_list tokens =
        match tokens with
        | Lex.Semicolon::rest -> parse_statement_list rest
        | Lex.ReturnKeyword::Lex.Semicolon::rest -> 
            let other_statements, rest = parse_statement_list rest in
                AST.Return::other_statements, rest
        | Lex.ReturnKeyword::rest ->
            let exp, rest = parse_exp rest in
                let other_statements, rest = parse_statement_list rest in
                    AST.ReturnVal(exp)::other_statements, rest
        | _ -> ([], tokens) (* Retorna lo que no esta en la lista de tokens *)

    (*funcion para checar si efectiva mente hay cuerpo de la funcion*)
    let parse_fun_body tokens = 
        let statements, rest = parse_statement_list tokens in
        match rest with
        | Lex.CloseBrace::[] -> AST.Body(statements)
        | _ -> failwith("Expected closing brace Error 5")

     (*Funcion para detectar parametros de la funcion puede ser principal*)
    let rec parse_fun_params = function
        | Lex.CloseParen::rest -> ([], rest)
        | Lex.IntKeyword::(Lex.Id name)::rest -> 
            let other_params, rest = parse_fun_params rest in
                (AST.Param(AST.IntType, AST.ID(name))::other_params, rest)
        | Lex.CharKeyword::(Lex.Id name)::rest -> 
            let other_params, rest = parse_fun_params rest in
                (AST.Param(AST.CharType, AST.ID(name))::other_params, rest)
        | _ -> failwith("Parse error in parse_fun_params Error 3")

    (*Primer paso ver si es un int o char*)
    (*Checa si tiene nombre la funcion por ahorita no se fija si es un main*)
    (*Pasa el resto*)
    let parse_fun tokens =
        let fun_type, fun_name, rest = 
            match tokens with
            | Lex.IntKeyword::(Lex.Id name)::Lex.OpenParen::rest -> (AST.IntType, AST.ID(name), rest)
            | Lex.CharKeyword::(Lex.Id name)::Lex.OpenParen::rest -> (AST.CharType, AST.ID(name), rest)
            | _ -> failwith("Parse error in parse_fun: bad function type or name  Error 1") in
        
        let fun_params, rest = parse_fun_params rest in
        let fun_body = 
            match rest with
            | Lex.OpenBrace::rest -> parse_fun_body rest
            | _ -> failwith("Expected brace to open function body Error 2") in
        AST.FunDecl(fun_type, fun_name, fun_params, fun_body) (*Arbol ya generado pata la funcion*)

    (*funcion principal o que llamamos para parsear*)
    let parse tokens = AST.Prog(parse_fun tokens)
end