type operator = 
  | Negation
  | Bitwise
  | LogNeg;
type exp =
  | UnOp(operator,exp)
  | Const(int)
  | Err_exp(string); 
type statement =
  | Assign(string,exp)
  | Return(exp)
  | Err_state(string);
type fun_decl =
  | Err_fun(string)
  | Fun(string, statement);
type prog =
  | Prog(fun_decl)
  | Err_prog(string);

let identi_prog = (t: prog) => { /*Para identificar que el nodo sea de tipo prog*/
  let result =
    switch (t) {
    | Prog(fun_decl) => true
    | Err_prog(string) => false
    };
    result;
};

let identi_fun_decl = (t: fun_decl) => { /*Para identificar que el nodo sea de tipo fun_decl*/
  let result =
    switch (t) {
    | Err_fun(string) => false
    | Fun(string, statement) => true
    };
    result;
};

let identi_statement = (t: statement) => { /*Para identificar que el nodo sea de tipo statement*/
  let result =
    switch (t) {
    | Assign(string,exp) => true
    | Return(exp) => true
    | Err_state(string) => false
    };
    result;
};

let identi_exp = (t: exp) => { /*Para identificar que el nodo sea de tipo statement*/
  switch (t) {
  | Const(int) => true
  | Err_exp(string) => false
  | UnOp(operator,exp) => true
  };
};

let ext_prog = (t: prog) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Prog(fun_decl) => fun_decl
  };
}

let ext_name_fun_decl = (t: fun_decl) =>{ /*Para extraer el nombre de la fun*/
  switch(t){
    | Fun(string, statement) => string
    };
};

let ext_fun_decl = (t: fun_decl) =>{/*Para extraer el nodo statement de fun_decl*/
  switch(t){
    | Fun(string, statement) => statement
    };
};

let ext_name_statement = (t: statement) =>{
  switch(t){
  | Assign(string,exp) => string
  | Return(exp) => "ReturnKeyword"
    };
};

let ext_statement = (t: statement) =>{
  switch(t){
  | Assign(string,exp) => exp
  | Return(exp) => exp
    };
};

let ext_prog_err = (t: prog) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Err_prog(string) => string
  };
}

let ext_fun_err = (t: fun_decl) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Err_fun(string) => string
  };
}

let ext_state_err = (t: statement) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Err_state(string) => string
  };
}

let ext_exp_err = (t: exp) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Err_exp(string) => string
  };
}

let printAST = ast => {
  Js.log("AST del parser aqui \n");
  ast;
};
