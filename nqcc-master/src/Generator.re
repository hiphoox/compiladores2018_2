/*
 postorder(node)
   if (node = null)
     return
   postorder(node.left)
   postorder(node.right)
   visit(node)
   */

let generate_exp = ast_exp =>
  switch (ast_exp) {
  | Ast.Const(value) =>
    let decimal = string_of_int(value);
    let return_statement = "    movl    " ++ decimal ++ ", %eax";
    Js.log(return_statement);
  };

let visit_statement = () => {
  let return_statement = "    ret";
  Js.log(return_statement);
};

let generate_statement = () => {
  generate_exp(Ast.Const(2));
  visit_statement();
};

let gen_function_code = () => {
  let functionName = "main";
  Js.log("_" ++ functionName ++ ":");
  generate_statement();
};

let generate_code = ast => {
  Js.log("    .globl _main");
  gen_function_code();
};