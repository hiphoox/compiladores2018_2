// Generated by BUCKLESCRIPT VERSION 4.0.14, PLEASE EDIT WITH CARE
'use strict';

var Block = require("bs-platform/lib/js/block.js");
var Belt_List = require("bs-platform/lib/js/belt_List.js");
var Belt_Array = require("bs-platform/lib/js/belt_Array.js");
var Caml_array = require("bs-platform/lib/js/caml_array.js");
var Caml_format = require("bs-platform/lib/js/caml_format.js");
var Caml_option = require("bs-platform/lib/js/caml_option.js");

var special_chars_regexp = (/^({|}|\(|\)|-|~|!|\+|\*|\/|;)/);

var const_regex = (/\d+/);

var id_regexp = (/\w+/);

function startsWith(program) {
  var match = program.match(special_chars_regexp);
  if (match !== null) {
    return /* tuple */[
            Caml_array.caml_array_get(match, 0),
            program.substring(1)
          ];
  } else {
    return /* tuple */[
            "None",
            program
          ];
  }
}

function getId(program) {
  var match = program.match(id_regexp);
  if (match !== null) {
    return /* tuple */[
            /* Id */Block.__(0, [Caml_array.caml_array_get(match, 0)]),
            program.substring(Caml_array.caml_array_get(match, 0).length)
          ];
  } else {
    return /* tuple */[
            /* Invalid */13,
            ""
          ];
  }
}

function getConstant(program) {
  var match = program.match(const_regex);
  if (match !== null) {
    return /* tuple */[
            /* Constant */Block.__(1, [Caml_format.caml_int_of_string(Caml_array.caml_array_get(match, 0))]),
            program.substring(Caml_array.caml_array_get(match, 0).length)
          ];
  } else {
    return /* tuple */[
            /* Invalid */13,
            ""
          ];
  }
}

function getReturn(program) {
  var return_size = "return".length;
  return /* tuple */[
          /* ReturnKeyword */5,
          program.substring(return_size)
        ];
}

function getInt(program) {
  var int_size = "Int".length;
  return /* tuple */[
          /* IntKeyword */6,
          program.substring(int_size)
        ];
}

function getComplexTokens(program) {
  if (program.startsWith("int")) {
    return getInt(program);
  } else if (program.startsWith("return")) {
    return getReturn(program);
  } else if (Caml_option.null_to_opt(program.match(const_regex)) !== undefined) {
    return getConstant(program);
  } else {
    return getId(program);
  }
}

function lexRawTokens(input) {
  if (input.length === 0) {
    return /* [] */0;
  } else {
    var match = startsWith(input);
    var match$1;
    switch (match[0]) {
      case "!" : 
          match$1 = /* tuple */[
            /* LogNeg */9,
            match[1]
          ];
          break;
      case "(" : 
          match$1 = /* tuple */[
            /* OpenParen */2,
            match[1]
          ];
          break;
      case ")" : 
          match$1 = /* tuple */[
            /* CloseParen */3,
            match[1]
          ];
          break;
      case "*" : 
          match$1 = /* tuple */[
            /* Multiplication */11,
            match[1]
          ];
          break;
      case "+" : 
          match$1 = /* tuple */[
            /* Addition */10,
            match[1]
          ];
          break;
      case "-" : 
          match$1 = /* tuple */[
            /* Negation */7,
            match[1]
          ];
          break;
      case "/" : 
          match$1 = /* tuple */[
            /* Division */12,
            match[1]
          ];
          break;
      case ";" : 
          match$1 = /* tuple */[
            /* Semicolon */4,
            match[1]
          ];
          break;
      case "{" : 
          match$1 = /* tuple */[
            /* OpenBrace */0,
            match[1]
          ];
          break;
      case "}" : 
          match$1 = /* tuple */[
            /* CloseBrace */1,
            match[1]
          ];
          break;
      case "~" : 
          match$1 = /* tuple */[
            /* Bitwise */8,
            match[1]
          ];
          break;
      default:
        match$1 = getComplexTokens(match[1]);
    }
    var remainingTokens = lexRawTokens(match$1[1]);
    return /* :: */[
            match$1[0],
            remainingTokens
          ];
  }
}

function lexCollection(acummulator, program) {
  return Belt_List.concat(acummulator, lexRawTokens(program));
}

function lex(program_text) {
  var trimmed_program = program_text.trim();
  var re = (/\s+/);
  var program = trimmed_program.split(re);
  return Belt_Array.reduce(program, /* [] */0, lexCollection);
}

exports.special_chars_regexp = special_chars_regexp;
exports.const_regex = const_regex;
exports.id_regexp = id_regexp;
exports.startsWith = startsWith;
exports.getId = getId;
exports.getConstant = getConstant;
exports.getReturn = getReturn;
exports.getInt = getInt;
exports.getComplexTokens = getComplexTokens;
exports.lexRawTokens = lexRawTokens;
exports.lexCollection = lexCollection;
exports.lex = lex;
/* special_chars_regexp Not a pure module */
