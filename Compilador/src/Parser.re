let parse_constant = tokenList: Ast.exp => Ast.Const(2);

let parse_statement = tokenList: Ast.statement => {
  let constant = parse_constant(tokenList);
  Ast.Return(constant);
};

let parse_function = tokenList: Ast.fun_decl => {
  let [token, ...remainingTokens] = tokenList; /*Sacamos el primer elemento de la lista de tokens que en este caso será el identificador "Int"*/
  
  if((token |> Token.identificador) != "IntKeyword"){ /*Comprobamos que el token sea intkeyword*/
    Js.log("Error, falta int");
  };

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que será un id*/
  if(token |> Token.identificador != "Id"){ /*Verificamos que sea realmente un id*/
    Js.log("Error, falta identificador");
  };

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista*/
  if(token |> Token.identificador != "OpenParen"){
    Js.log("Error, falta (");
  };

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista*/
  if(token |> Token.identificador != "CloseParen"){
    Js.log("Error, falta )");
  };

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista*/
  if(token |> Token.identificador != "OpenBrace"){
    Js.log("Error, falta {");
  };
  
  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista*/
  remainingTokens |> Token.printTokenList;
  token |> Token.identificador |> Js.log; /*Identificamos el token*/



  /*let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista*/
  if(token |> Token.identificador != "CloseBrace"){
    Js.log("Error, falta }");
  };*/




  /*Solo falta identificar los demás token (){} y ver como hacer pop en la lista*/




  
  let return = parse_statement(tokenList);
  Ast.Fun("main", return);
};

let parse_program = tokenList: option(Ast.prog) => {
  let func_decl = parse_function(tokenList);
  Some(Ast.Prog(func_decl));
};