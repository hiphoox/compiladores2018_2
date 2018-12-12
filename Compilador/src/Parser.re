let parse_constant = tokenList: (Ast.exp, list(Token.token)) =>{ /*Recibe la lista de token y devueleve el token y la lista modificada*/
  
  let [token, ...remainingTokens] = tokenList; /*Sacamos siguiente token que debe de ser el numero*/
  if((token |> Token.identificador) != "Constant"){ /*Comprobamos que el token sea una constante*/
    Js.log("Error, falta una constante");
  };

  let number = int_of_string(token |> Token.extrac); /*Almacenamos el valor de la constante*/

  (Ast.Const(number), remainingTokens); /*Devolvemos el nodo constant*/
};

let parse_statement = tokenList: (Ast.statement, list(Token.token)) => {  /*Recibe la lista de token y devueleve el token y la lista modificada*/
 
  let [token, ...remainingTokens] = tokenList; /*Sacamos siguiente token que debe de ser el return*/
  if((token |> Token.identificador) != "ReturnKeyword"){ /*Comprobamos que el token sea return*/
    Js.log("Error, falta return");
  };

  /*El elemento es el número, por lo que se pasa al parse_constant*/
  let (constant, remainingTokens ) = parse_constant(remainingTokens);

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos siguiente token que debe de ser ";"*/
  if((token |> Token.identificador) != "Semicolon"){
    Js.log("Error, falta ;");
  };
  (Ast.Return(constant), remainingTokens);
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
  let idName = token |> Token.extrac; /*Obtenemos el nombre del id*/

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que será "("*/
  if(token |> Token.identificador != "OpenParen"){
    Js.log("Error, falta (");
  };

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que debe de ser ")"*/
  if(token |> Token.identificador != "CloseParen"){
    Js.log("Error, falta )");
  };

  let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que debe de ser  "{"*/
  if(token |> Token.identificador != "OpenBrace"){
    Js.log("Error, falta {");
  };
  
  /*Como lo que sigue en la lista es el return se sigue al parse_statement*/
  let (return, remainingTokens) = parse_statement(remainingTokens); 

  let [token, ...remainingTokens] = remainingTokens;/*Sacamos el siguiente elemento de la lista*/
  if(token |> Token.identificador != "CloseBrace"){ /*En teoría debe de revisar que lo que sigue es el "}"*/
    Js.log("Error, falta }");
  };

  Ast.Fun(idName, return);
};

let parse_program = tokenList: option(Ast.prog) => {
  let func_decl = parse_function(tokenList);
  Some(Ast.Prog(func_decl));
};
