module AST =
    struct
        type const = 
            | Int of int
            | String of string
        type type_def = 
            | IntType
        type exp = Const of const
        type statement = 
            | Return
            | Valor_return of exp 
        type id = ID of string
        type fun_param = Param of type_def * id
        type fun_body = Body of statement list
        type fun_decl = FunDecl of type_def * id * fun_param list * fun_body
        type prog = Prog of fun_decl
    end 