type operator = 
  | Negation
  | Bitwise
  | LogNeg;
type exp =
  | UnOp(operator,exp)
  | Const(int); 
type statement =
  | Assign(string,exp)
  | Return(exp);
type fun_decl =
  | Fun(string, statement);
type prog =
  | Prog(fun_decl);

let identi_prog = (t: prog) => { /*Para identificar que el nodo sea de tipo prog*/
  let result =
    switch (t) {
    | Prog(fun_decl) => true
    };
    result;
};

let identi_fun_decl = (t: fun_decl) => { /*Para identificar que el nodo sea de tipo fun_decl*/
  let result =
    switch (t) {
    | Fun(string, statement) => true
    };
    result;
};

let identi_statement = (t: statement) => { /*Para identificar que el nodo sea de tipo statement*/
  let result =
    switch (t) {
    | Assign(string,exp) => true
    | Return(exp) => true
    };
    result;
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

let printAST = ast => {
  Js.log("AST del parser aqui \n");
  ast;
};type operator = 
  | Negation
  | Bitwise
  | LogNeg;

type exp =
  | UnOp(operator,exp)
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
