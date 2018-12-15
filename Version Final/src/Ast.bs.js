// Generated by BUCKLESCRIPT VERSION 4.0.14, PLEASE EDIT WITH CARE
'use strict';

var Caml_builtin_exceptions = require("bs-platform/lib/js/caml_builtin_exceptions.js");

function identi_prog(t) {
  if (t.tag) {
    return false;
  } else {
    return true;
  }
}

function identi_fun_decl(t) {
  if (t.tag) {
    return true;
  } else {
    return false;
  }
}

function identi_statement(t) {
  switch (t.tag | 0) {
    case 0 : 
    case 1 : 
        return true;
    case 2 : 
        return false;
    
  }
}

function identi_exp(t) {
  switch (t.tag | 0) {
    case 1 : 
        return false;
    case 0 : 
    case 2 : 
        return true;
    
  }
}

function identi_termino(t) {
  switch (t.tag | 0) {
    case 1 : 
        return false;
    case 0 : 
    case 2 : 
        return true;
    
  }
}

function identi_factor(t) {
  switch (t.tag | 0) {
    case 1 : 
        return false;
    case 0 : 
    case 2 : 
        return true;
    
  }
}

function ext_prog(t) {
  if (t.tag) {
    throw [
          Caml_builtin_exceptions.match_failure,
          /* tuple */[
            "Ast.re",
            70,
            27
          ]
        ];
  } else {
    return t[0];
  }
}

function ext_name_fun_decl(t) {
  if (t.tag) {
    return t[0];
  } else {
    throw [
          Caml_builtin_exceptions.match_failure,
          /* tuple */[
            "Ast.re",
            76,
            40
          ]
        ];
  }
}

function ext_fun_decl(t) {
  if (t.tag) {
    return t[1];
  } else {
    throw [
          Caml_builtin_exceptions.match_failure,
          /* tuple */[
            "Ast.re",
            82,
            35
          ]
        ];
  }
}

function ext_name_statement(t) {
  switch (t.tag | 0) {
    case 0 : 
        return t[0];
    case 1 : 
        return "ReturnKeyword";
    case 2 : 
        throw [
              Caml_builtin_exceptions.match_failure,
              /* tuple */[
                "Ast.re",
                88,
                42
              ]
            ];
    
  }
}

function ext_statement(t) {
  switch (t.tag | 0) {
    case 0 : 
        return t[1];
    case 1 : 
        return t[0];
    case 2 : 
        throw [
              Caml_builtin_exceptions.match_failure,
              /* tuple */[
                "Ast.re",
                95,
                37
              ]
            ];
    
  }
}

function ext_prog_err(t) {
  if (t.tag) {
    return t[0];
  } else {
    throw [
          Caml_builtin_exceptions.match_failure,
          /* tuple */[
            "Ast.re",
            102,
            31
          ]
        ];
  }
}

function ext_fun_err(t) {
  if (t.tag) {
    throw [
          Caml_builtin_exceptions.match_failure,
          /* tuple */[
            "Ast.re",
            108,
            34
          ]
        ];
  } else {
    return t[0];
  }
}

function ext_state_err(t) {
  switch (t.tag | 0) {
    case 0 : 
    case 1 : 
        throw [
              Caml_builtin_exceptions.match_failure,
              /* tuple */[
                "Ast.re",
                114,
                37
              ]
            ];
    case 2 : 
        return t[0];
    
  }
}

function ext_exp_err(t) {
  switch (t.tag | 0) {
    case 1 : 
        return t[0];
    case 0 : 
    case 2 : 
        throw [
              Caml_builtin_exceptions.match_failure,
              /* tuple */[
                "Ast.re",
                120,
                29
              ]
            ];
    
  }
}

function ext_ter_err(t) {
  switch (t.tag | 0) {
    case 1 : 
        return t[0];
    case 0 : 
    case 2 : 
        throw [
              Caml_builtin_exceptions.match_failure,
              /* tuple */[
                "Ast.re",
                125,
                32
              ]
            ];
    
  }
}

function ext_fac_err(t) {
  switch (t.tag | 0) {
    case 1 : 
        return t[0];
    case 0 : 
    case 2 : 
        throw [
              Caml_builtin_exceptions.match_failure,
              /* tuple */[
                "Ast.re",
                130,
                31
              ]
            ];
    
  }
}

function printAST(ast) {
  console.log("AST del parser aqui");
  console.log(ast);
  return ast;
}

exports.identi_prog = identi_prog;
exports.identi_fun_decl = identi_fun_decl;
exports.identi_statement = identi_statement;
exports.identi_exp = identi_exp;
exports.identi_termino = identi_termino;
exports.identi_factor = identi_factor;
exports.ext_prog = ext_prog;
exports.ext_name_fun_decl = ext_name_fun_decl;
exports.ext_fun_decl = ext_fun_decl;
exports.ext_name_statement = ext_name_statement;
exports.ext_statement = ext_statement;
exports.ext_prog_err = ext_prog_err;
exports.ext_fun_err = ext_fun_err;
exports.ext_state_err = ext_state_err;
exports.ext_exp_err = ext_exp_err;
exports.ext_ter_err = ext_ter_err;
exports.ext_fac_err = ext_fac_err;
exports.printAST = printAST;
/* No side effect */
