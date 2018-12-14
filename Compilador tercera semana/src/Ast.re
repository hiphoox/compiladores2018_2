type factor = 
  | UnOp(Token.token, factor)
  | Err_fac(string)
  | Const(int);
type termino = 
  | Ter(factor)
  | Err_ter(string)
  | BinOp(Token.token, factor, factor);

type exp = 
  | Expr(termino)
  | Err_exp(string)
  | BinOp(Token.token,termino, termino)
  
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
  switch (t) {
  | Prog(fun_decl) => true
  | Err_prog(string) => false
  };
  };

let identi_fun_decl = (t: fun_decl) => { /*Para identificar que el nodo sea de tipo fun_decl*/
  switch (t) {
  | Err_fun(string) => false
  | Fun(string, statement) => true
  };
  };

let identi_statement = (t: statement) => { /*Para identificar que el nodo sea de tipo statement*/
  switch (t) {
  | Assign(string,exp) => true
  | Return(exp) => true
  | Err_state(string) => false
  };
  };

let identi_exp = (t: exp) => { /*Para identificar que el nodo sea de tipo exp*/
  switch (t) {
  | Expr(termino) => true
  | Err_exp(string) => false
  | BinOp(token, ter1, ter2) => true
  };
  };
let identi_termino = (t : termino) => {
  switch(t){
  | Ter(factor) => true
  | Err_ter(string) => false
  | BinOp(token, fac1, fac2) => true
  };
  };
let identi_factor = (t : factor) => {
    switch(t){
    | UnOp(token, factor) => true
    | Err_fac(string) => false
    | Const(int) => true
    };
    };

let ext_prog = (t: prog) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Prog(fun_decl) => fun_decl
  };
  };

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
  };

let ext_fun_err = (t: fun_decl) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Err_fun(string) => string
  };
  };

let ext_state_err = (t: statement) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Err_state(string) => string
  };
  };

let ext_exp_err = (t: exp) =>{ /*Para extraer el nodo fun_decl de prog*/
  switch(t){
  | Err_exp(string) => string
  };
  };
let ext_ter_err = (t: termino)=>{
  switch(t){
  | Err_ter(string) => string
  };
  };
let ext_fac_err = (t: factor)=>{
    switch(t){
    | Err_fac(string) => string
    };
    };

let printAST = ast => {
  Js.log("AST del parser aqui");
  Js.log(ast);
  ast;
  };