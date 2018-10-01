(* Gramatica:
 * program -> function-definition
 * function-definition -> type id ( argument_list ) fun_body
 * argument_list -> type id | type id argument_list
 * fun_body -> { statement_list }
 * statement_list -> statement | statement statement_list
 * statement -> return | return exp
 * exp -> int
 *)
 
module AST =
    struct
        type const = 
            | Int of int
            | Char of char
            | String of string
        type type_def = 
            | IntType
            | CharType
        type exp = Const of const
        type statement = 
            | Return
            | ReturnVal of exp (* should we add a return_exp instead? *)
        type id = ID of string
        type fun_param = Param of type_def * id
        type fun_body = Body of statement list
        type fun_decl = FunDecl of type_def * id * fun_param list * fun_body
        type prog = Prog of fun_decl
    end

