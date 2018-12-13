let rec parse_constant = tokenList: (Ast.exp, list(Token.token)) =>{
    let [token, ...remainingTokens] = tokenList; /*Sacamos siguiente token que debe de ser el numero o UnOp*/
    if((token |> Token.identificador) == "Negation" || (token |> Token.identificador) == "Bitwise" || (token |> Token.identificador) == "LogNeg"){
        let (exp, remainingTokens) = parse_constant(remainingTokens);
        (Ast.UnOp(token |> Token.identificador, exp), remainingTokens);
    }else{
        if((token |> Token.identificador) == "Constant"){ /*Comprobamos que el token sea una constante*/
            let number = int_of_string(token |> Token.extrac); /*Almacenamos el valor de la constante*/ 
            (Ast.Const(number), remainingTokens); /*Devolvemos el nodo constant*/ 
        }else{
            (Ast.Err_exp("Error, falta una constante"),remainingTokens);
        };
    };
  };
  
let parse_statement = tokenList: (Ast.statement, list(Token.token)) => {  /*Recibe la lista de token y devueleve el token y la lista modificada*/
    let [token, ...remainingTokens] = tokenList; /*Sacamos siguiente token que debe de ser el return*/
    if((token |> Token.identificador) == "ReturnKeyword"){ /*Comprobamos que el token sea return*/
        let var = token |> Token.identificador;
        let (constant, remainingTokens ) = parse_constant(remainingTokens); /*El elemento es el número, por lo que se pasa al parse_constant*/
        if(Ast.identi_exp(constant) == true){
            let [token, ...remainingTokens] = remainingTokens; /*Sacamos siguiente token que debe de ser ";"*/
            if((token |> Token.identificador) == "Semicolon"){
                (Ast.Assign(var,constant), remainingTokens);
            }else{
                (Ast.Err_state("Error, falta ;"),remainingTokens);    
            };
        }else{
            (Ast.Err_state(Ast.ext_exp_err(constant)), remainingTokens);
        };
    }else{
        (Ast.Err_state("Error, falta return"),remainingTokens);
    };
  };
  
let parse_function = tokenList: Ast.fun_decl => {
    let [token, ...remainingTokens] = tokenList; /*Sacamos el primer elemento de la lista de tokens que en este caso será el identificador "Int"*/
    if((token |> Token.identificador) == "IntKeyword"){ /*Comprobamos que el token sea intkeyword*/
        let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que será un id*/
        if((token |> Token.identificador) == "Id"){ /*Comprobamos que el token sea intkeyword*/
            let idName = token |> Token.extrac; /*Obtenemos el nombre del id*/
            let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que será "("*/
            if(token |> Token.identificador == "OpenParen"){
                let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que debe de ser ")"*/
                if(token |> Token.identificador == "CloseParen"){
                    let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que debe de ser  "{"*/
                    if(token |> Token.identificador == "OpenBrace"){
                        let (return, remainingTokens) = parse_statement(remainingTokens); /*Como lo que sigue en la lista es el return se sigue al parse_statement*/
                        if(Ast.identi_statement(return) == true){ /*Revisamos que el nodo devuelto no tenga error*/
                            let [token, ...remainingTokens] = remainingTokens;/*Sacamos el siguiente elemento de la lista*/
                            if(token |> Token.identificador == "CloseBrace"){ /*En teoría debe de revisar que lo que sigue es el "}"*/
                                Ast.Fun(idName, return);
                            }else{
                                Ast.Err_fun("Error, falta }");        
                            };
                        }else{
                            Ast.Err_fun(Ast.ext_state_err(return));
                        };
                    }else{ 
                        Ast.Err_fun("Error, falta {");    
                    };
                }else{
                    Ast.Err_fun("Error, falta )");
                };
            }else{ 
                Ast.Err_fun("Error, falta (");
            };
          }else{
            Ast.Err_fun("Error, falta identificador");
          };
      }else{
        Ast.Err_fun("Error, falta int");
      };
  };
  
let parse_program = tokenList: Ast.prog => {
    let func_decl = parse_function(tokenList);
    if(Ast.identi_fun_decl(func_decl) ==true){
        Js.log("Paso el parser")
        Ast.Prog(func_decl);
    }else{
        let message = Ast.ext_fun_err(func_decl);
        Js.log(message);
        Ast.Err_prog("Error en el parser");
    };
  };
