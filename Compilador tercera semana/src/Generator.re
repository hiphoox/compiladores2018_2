let rec generate_factor = (ast : Ast.factor, reg : int) =>
  switch(ast){
  | Const(value)=>
    let decimal = string_of_int(value);
    let return_statement = "    movl    " ++ decimal ++ ", " ++ Words.registro(reg);
    Js.log(return_statement);
  | UnOp(ope, factor) =>
    if(ope |> Token.identificador == "LogNeg"){
      let return_unop = "    cmpl   $0, " ++ Words.registro(reg) ++  "\n    movl   $0, " ++ Words.registro(1)  ++  "\n    sete   %al ";
      generate_factor(factor,0);
      Js.log(return_unop);
    }else{
      let return_unop = "    " ++ Words.tradu(ope |> Token.identificador) ++ "    " ++ Words.registro(1);
      generate_factor(factor,0);
      Js.log(return_unop);
    }; 
  };

let rec generate_termino = (ast : Ast.termino) =>
  switch(ast){
  | Ter(fac) =>
    generate_factor(fac,0);
  | BinOp(ope,fac1, fac2) =>
    generate_factor(fac1,0);
    generate_factor(fac2,1);
    let return_termino = ("    " ++  Words.tradu(ope |> Token.identificador) ++ "    " ++ Words.registro(1));
    Js.log(return_termino);
  };

let generate_exp = (ast_exp: Ast.exp) => 
  switch(ast_exp){
  | Ast.BinOp(ope, ter1, ter2) =>
    generate_termino(ter1);
    generate_termino(ter2);
    if( Token.identificador(ope) == "Negation" ){
      let return_unop = "    " ++ Words.tradu(ope |> Token.identificador) ++ "    " ++  Words.registro(1);
      Js.log(return_unop);
    };
    let return_exp = "    add    " ++ Words.registro(0) ++ ", " ++Words.registro(1);
    Js.log(return_exp);
  | Ast.Expr(ter) => 
    generate_termino(ter);
  };

  let visit_statement = (name : string) => {
  let return_statement = "    " ++ Words.tradu(name); /*Imprime la linea de código del return*/
  Js.log(return_statement);
  };

let generate_statement = ast => {
  if(Ast.identi_statement(ast) == true){ /*Revisa que el nodo sea del tipo statement*/
    let name_state = Ast.ext_name_statement(ast); /*Almacena el nombre del token solicitado, en este caso el return*/
    let node_exp = Ast.ext_statement(ast); /*Obtenemos el nodo de tipo exp*/
    generate_exp(node_exp); /*Mandamos al generador de exp*/
    visit_statement(name_state); /*Se encarga de pasar el return a ensamblador*/
  };
  };

let gen_function_code = ast => {
  if(Ast.identi_fun_decl(ast) == true){ /*Reviso que el nodo sea del tipo fun_decl*/
    let functionName = Ast.ext_name_fun_decl(ast); /*Almacena el nombre de la fun*/
    let node_statement = Ast.ext_fun_decl(ast); /*Almacena el nodo statement*/
    Js.log("_" ++ functionName ++ ":"); /*Imprime parte del código*/
    generate_statement(node_statement); /*Lo mandamos al generador de statement*/
  };
  };

let generate_code = ast => {
  if(Ast.identi_prog(ast) ==true){ /*Comprueba que el AST este correcto*/
    let node_prog = Ast.ext_prog(ast); /*Almacenamos el nodo prog*/
    Js.log("    .globl _main"); /*Imprime el encabezado*/
    gen_function_code(node_prog); /*Manda el AST al generador de funciones*/
  }else{
    Ast.ext_prog_err(ast) |> Js.log; /*En caso de que haya un error notificarlo*/
  };
  };