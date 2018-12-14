let rec parse_factor = tokenList: (Ast.factor, list(Token.token)) => {
    let [token, ...remainingTokens] = tokenList; /*Sacamos siguiente token que debe de ser el numero o UnOp*/
    /*Revisamos que e token sea un operador unario*/
    if((token |> Token.identificador) == "Negation" || (token |> Token.identificador) == "Bitwise" || (token |> Token.identificador) == "LogNeg"){
        let (fac, remainingTokens) = parse_factor(remainingTokens); /*Como es un operador unario mandamos a parsear el siguiente elemento que debe de ser un factor*/
        if(Ast.identi_factor(fac) == true){ /*Revisa que el nodo recibido sea correcto*/
            (Ast.UnOp(token, fac), remainingTokens); /*Devolvemos el nodo*/
        }else{
            (Ast.Err_fac("Error, falta una constante u operador unario"), remainingTokens);
        };
    }else{ /*En caso de que el token no sea una operacion unaria, debe de ser una constante*/
        if((token |> Token.identificador) == "Constant"){ /*Comprobamos que el token sea una constante*/
            let number = int_of_string(token |> Token.extrac); /*Almacenamos el valor de la constante*/ 
            (Ast.Const(number), remainingTokens); /*Devolvemos el nodo constant*/ 
        }else{
            (Ast.Err_fac("Error, falta una constante u operador unario"),tokenList); /*En caso de error, devuelve un nodo error*/
        };
    };
    };

let parse_termino = tokenList : (Ast.termino, list(Token.token)) =>{
    let (fac1,tokenList) = parse_factor(tokenList); /*Mandamos a llamar al parse_factor*/
    if(Ast.identi_factor(fac1) == true){ /*Revisa que el nodo recibido sea correcto*/
        let [token, ...r] = tokenList; /*Hacemos un pop a la lista*/
        if((token |> Token.identificador) == "Multiplication" || (token |> Token.identificador) == "Division") { /*Revisa si es alguno de los operadores * o / */
            let oper = token; /*Guarda el token de la operación en una variable*/
            let (fac2,r) = parse_factor(r); /*Como entro al if debido a que es una operación binaria se tiene que mandar a parsear el segundo termino*/
            if(Ast.identi_factor(fac2) == true){ /*Revisa que el nodo recibido sea correcto*/
                (Ast.BinOp(oper,fac1, fac2),r); /*Devuelve el nodo de la exp del tipo operacion binaria*/
            }else{
                (Ast.Err_ter(Ast.ext_fac_err(fac1)), r); /*En caso de que el nodo que nos devolvió el parse_factor este mal devuelve un nodo error*/
            };
            
        }else{
            (Ast.Ter(fac1),tokenList); /*En caso de que el token que seguía del primer termino no sea un operador, devuelve unicamente el factor 1*/
        };
    }else{
        (Ast.Err_ter(Ast.ext_fac_err(fac1)), tokenList); /*En caso de que el nodo que nos devolvió el parse_factor este mal devuelve un nodo error*/
    };
    };

let parse_exp = tokenList : (Ast.exp, list(Token.token)) => {
    let (ter1,tokenList) = parse_termino(tokenList); /*Mandamos a llamar al parse_termino*/
    if(Ast.identi_termino(ter1) == true){ /*Revisa que el nodo recibido sea correcto*/
        let [token, ...r] = tokenList; /*Hacemos un pop a la lista*/
        if((token |> Token.identificador) == "Addition" || (token |> Token.identificador) == "Negation") { /*Revisa si es alguno de los operadores + o -*/
            let oper = token; /*Guarda el token de la operación en una variable*/
            let (ter2,r) = parse_termino(r); /*Como entro al if debido a que es una operación binaria se tiene que mandar a parsear el segundo termino*/
            if(Ast.identi_termino(ter2) == true){ /*Revisa que el nodo recibido sea correcto*/
                (Ast.BinOp(oper, ter1, ter2), r); /*Devuelve el nodo de la exp del tipo operacion binaria*/
            }else{
                (Ast.Err_exp(Ast.ext_ter_err(ter2)), r); /*En caso de que el nodo que nos devolvió el parse_termino este mal devuelve un nodo error*/
            };
        }else{
            (Ast.Expr(ter1), tokenList); /*En caso de que el token que seguía del primer termino no sea un operador, devuelve unicamente el termino 1*/
        };
    }else{
        (Ast.Err_exp(Ast.ext_ter_err(ter1)), tokenList); /*En caso de que el nodo que nos devolvió el parse_termino este mal devuelve un nodo error*/
    };
    };

let parse_statement = tokenList: (Ast.statement, list(Token.token)) => {  /*Recibe la lista de token y devueleve el token y la lista modificada*/
    let [token, ...remainingTokens] = tokenList; /*Sacamos siguiente token que debe de ser el return*/
    if((token |> Token.identificador) == "ReturnKeyword"){ /*Comprobamos que el token sea return*/
        let var = token |> Token.identificador; /*Almacenamos la palabra return en una variable*/
        let (exp, remainingTokens ) = parse_exp(remainingTokens); /*El elemento es una exp, por lo que se pasa al parse_exp*/
        if(Ast.identi_exp(exp) == true){ /*Revisa que el nodo recibido sea correcto*/
            let [token, ...remainingTokens] = remainingTokens; /*Sacamos siguiente token que debe de ser ";"*/
            if((token |> Token.identificador) == "Semicolon"){ /*Revisa que efectivamente sea el ; que venga*/
                (Ast.Assign(var,exp), remainingTokens); /*Devuelve el nodo junto con lo que queda de la lista*/
            }else{
                (Ast.Err_state("Error, falta ;"),remainingTokens); /*En caso de que falte el ; devolver el nodo error*/
            };
        }else{
            (Ast.Err_state(Ast.ext_exp_err(exp)), remainingTokens); /*En caso de que el nodo que nos devolvió el parse_exp este mal devuelve un nodo error*/
        };
    }else{
        (Ast.Err_state("Error, falta return"),remainingTokens);/*En caso de que el token que viene no sea el return se devuelve un nodo error*/
    };
  };
  
let parse_function = tokenList: Ast.fun_decl => {
    let [token, ...remainingTokens] = tokenList; /*Sacamos el primer elemento de la lista de tokens que en este caso será el identificador "Int"*/
    if((token |> Token.identificador) == "IntKeyword"){ /*Comprobamos que el token sea Intkeyword*/
        let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que será un id*/
        if((token |> Token.identificador) == "Id"){ /*Comprobamos que el token sea un Id*/
            let idName = token |> Token.extrac; /*Obtenemos el nombre del id*/
            let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que será "("*/
            if(token |> Token.identificador == "OpenParen"){ /*Comprobamos que el token sea un (*/
                let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que debe de ser ")"*/
                if(token |> Token.identificador == "CloseParen"){ /*Comprobamos que el token sea un )*/
                    let [token, ...remainingTokens] = remainingTokens; /*Sacamos el siguiente elemento de la lista que debe de ser  "{"*/
                    if(token |> Token.identificador == "OpenBrace"){ /*Comprobamos que el token sea un {*/
                        let (return, remainingTokens) = parse_statement(remainingTokens); /*Como lo que sigue en la lista es el return se pasa al parse_statement*/
                        if(Ast.identi_statement(return) == true){ /*Revisamos que el nodo devuelto no tenga error*/
                            let [token, ...remainingTokens] = remainingTokens;/*Sacamos el siguiente elemento de la lista que debe de ser }*/
                            if(token |> Token.identificador == "CloseBrace"){ /*En teoría debe de revisar que lo que sigue es el "}"*/
                                Ast.Fun(idName, return); /*Devuelve el nodo de funcion*/
                            }else{
                                Ast.Err_fun("Error, falta }"); /*En caso de que falte }, se crea un nodo error y se devuelve*/
                            };
                        }else{
                            Ast.Err_fun(Ast.ext_state_err(return)); /*En caso de que el nodo devuelto por el parse_statement tenga error, crea otro nodo error que será devuelto*/
                        };
                    }else{ /*Lo demás nos nodos error en caso de que se presente alguno*/
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
    let func_decl = parse_function(tokenList); /*Mandamos a llamar a la función que parsea las funciones*/
    if(Ast.identi_fun_decl(func_decl) ==true){ /*Revisamos que el nodo devuelto no sea de un error*/
        Ast.Prog(func_decl); /*Devuelve el AST de manera correcta*/
    }else{
        Js.log(Ast.ext_fun_err(func_decl)); /*En caso de error nos dice qcual fue el error*/
        Ast.Err_prog("Error en el parser"); /*Al final devuelve un nodo error que el generador revisará si es válido el Ast o no */
    };
  };