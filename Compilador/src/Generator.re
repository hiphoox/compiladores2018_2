let rec generate_exp = ast_exp =>
  switch (ast_exp) {
  | Ast.Const(value) =>
    let decimal = string_of_int(value);
    let return_statement = "    movl    " ++ decimal ++ ", %eax";
    Js.log(return_statement);
  | Ast.UnOp(ope, exp) => 
    if(ope == "LogNeg"){
      let return_unop = "    cmpl   $0, %eax" ++  "\n    movl   $0, %eax"  ++  "\n    sete   %al ";
      generate_exp(exp);
      Js.log(return_unop);
    }else{
      let return_unop = "    " ++ Words.tradu(ope) ++ "    %eax";
      generate_exp(exp);
      Js.log(return_unop);
    };
  
  };

let visit_statement = (name : string) => {
  let return_statement = "    " ++ Words.tradu(name);
  Js.log(return_statement);
};

let generate_statement = ast => {
  if(Ast.identi_statement(ast) == true){ /*Revisa que el nodo sea del tipo statement*/
    let name_state = Ast.ext_name_statement(ast);
    let node_exp = Ast.ext_statement(ast);
    generate_exp(node_exp);
    visit_statement(name_state);
  };
};

let gen_function_code = ast => {
  if(Ast.identi_prog(ast) == true){ /*Reviso que el nodo sea del tipo Prog*/
    let node_prog = Ast.ext_prog(ast);
    if(Ast.identi_fun_decl(node_prog) == true){ /*Reviso que el nodo sea del tipo fun_decl*/
      let functionName = Ast.ext_name_fun_decl(node_prog);
      let node_statement = Ast.ext_fun_decl(node_prog);
      Js.log("_" ++ functionName ++ ":");
      generate_statement(node_statement);
    };
  };
};

let generate_code = ast => {
  if(Ast.identi_prog(ast) ==true){
    Js.log("    .globl _main");
    gen_function_code(ast);
  }else{
    Ast.ext_prog_err(ast) |> Js.log;
  };
};
