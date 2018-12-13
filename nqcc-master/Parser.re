let parse_constant = tokenList: Ast.exp => Ast.Const(2);

let parse_statement = tokenList: Ast.statement => {
  let constant = parse_constant(tokenList);
  Ast.Return(constant);
};

let parse_function = tokenList: Ast.fun_decl => {
  let [token, ...remainingTokens] = tokenList;
  let return = parse_statement(tokenList);
  Ast.Fun("main", return);
};

let parse_program = tokenList: option(Ast.prog) => {
  let func_decl = parse_function(tokenList);
  Some(Ast.Prog(func_decl));
};