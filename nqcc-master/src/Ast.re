type exp =
  | Const(int);
type statement =
  | Return(exp);
type fun_decl =
  | Fun(string, statement);
type prog =
  | Prog(fun_decl);

let printAST = prog => {
  Js.log("AST del parser aqui \n");
  prog;
};