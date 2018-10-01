open Ast

module Gen : sig
    val generate : AST.prog -> unit
end =
struct



    let generate prog =

        (* abrimos el archivo que tendra nuestro ensamblador *) 
        let chan = open_out "assembly.s" in

        (* imprimimos siempre el  .globl _main entodos los archivos *)
        let _ = Printf.fprintf chan "    .globl _main\n" in

        (*Generamos el codigo de ensamblador*)
        let generate_statement = function
        | AST.Return -> Printf.fprintf chan "ret"
        | AST.ReturnVal(AST.Const(AST.Int i)) -> 
            Printf.fprintf chan "    movl    $%d, %%eax\n" i;
            Printf.fprintf chan "    ret"
        | _ -> failwith("Expression not supported Error 6") in

        let generate_statements statements = List.iter generate_statement statements in

        (*funcion principal para generar el codigo del programa asamblador*)
        let generate_fun f = 
            match f with
            | AST.FunDecl(fun_type, AST.ID(fun_name), fun_params, AST.Body(statements)) ->
                let _ = Printf.fprintf chan "_%s:\n" fun_name in
                generate_statements statements in
        match prog with
        | AST.Prog f ->  
            let _ = generate_fun f in
            close_out chan
end
