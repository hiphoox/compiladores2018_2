type token =  /*Definimos los token*/
  | OpenBrace
  | CloseBrace
  | OpenParen
  | CloseParen
  | Semicolon
  | ReturnKeyword
  | IntKeyword
  | Negation
  | Bitwise
  | LogNeg
  | Addition
  | Multiplication
  | Division
  | Id(string)
  | Constant(int)
  | Invalid;

let tokenToString = (acummulator, t: token): string => { /*Identificamos los token para imprimir la lista*/
  let result =
    switch (t) {
    | OpenBrace => "OpenBrace"
    | CloseBrace => "CloseBrace"
    | OpenParen => "OpenParen"
    | CloseParen => "CloseParen"
    | Semicolon => "Semicolon"
    | ReturnKeyword => "ReturnKeyword"
    | IntKeyword => "IntKeyword"
    | Negation => "Negation"
    | Bitwise => "Bitwise"
    | LogNeg => "LogNeg"
    | Addition => "Addition"
    | Multiplication => "Multiplication"
    | Division => "Division"
    | Id(n) => "(Id: " ++ n ++ ")"
    | Constant(n) => "(Constant: " ++ string_of_int(n) ++ ")"
    | Invalid => "Invalid Token"
    };
  acummulator ++ " " ++ result ++ ",";
};

let tokenListToString = tokensList => { /*Convierte la lista de token en string*/
  let comma_regexp = [%re "/,$/"];
  let stringList = Belt.List.reduce(tokensList, "[", tokenToString);
  Js.String.replaceByRe(comma_regexp, " ]", stringList);
};

let printTokenList = tokenList => { /*Imprime la lista de token*/
  tokenList |> tokenListToString |> Js.log;
  tokenList;
};

let identificador = (t: token) => { /*Para identificar los token en la comparación*/
  let result =
    switch (t) {
    | OpenBrace => "OpenBrace"
    | CloseBrace => "CloseBrace"
    | OpenParen => "OpenParen"
    | CloseParen => "CloseParen"
    | Semicolon => "Semicolon"
    | ReturnKeyword => "ReturnKeyword"
    | IntKeyword => "IntKeyword"
    | Negation => "Negation"
    | Bitwise => "Bitwise"
    | LogNeg => "LogNeg"
    | Addition => "Addition"
    | Multiplication => "Multiplication"
    | Division => "Division"
    | Id(n) => "Id"
    | Constant(n) => "Constant"
    | Invalid => "Invalid Token"
    };
    result;
};

let extrac = (t: token) => { /*Extraemos los valores que tengan el id y/o constant*/
  let result =
    switch (t) {
    | Id(n) => n
    | Constant(n) => string_of_int(n)
    | Invalid => "Invalid Token"
    };
    result;
};