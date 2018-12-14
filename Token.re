type token =
  | OpenBrace
  | CloseBrace
  | OpenParen
  | CloseParen
  | Semicolon
  | Keyword(string)
  | Id(string)
  | Constant(int)
  | Minus
  | Mult
  | Div
  | Plus
  | BitwiseComplement /* ~ */
  | LogicalNegation /* ! */
  | Invalid;

let tokenToString = (acummulator, t: token): string => {
  let result =
    switch (t) {
    | OpenBrace => "OpenBrance"
    | CloseBrace => "CloseBrace"
    | OpenParen => "OpenParen"
    | CloseParen => "CloseParen"
    | Semicolon => "Semicolon"
    | Keyword(n) => "(KW: "++n++")"
    | Id(n) => "(Id: " ++ n ++ ")"
    | Constant(n) => "(Constant: " ++ string_of_int(n) ++ ")"
    | Minus => "Subtraction"
    | Mult => "Multiplication"
    | Div => "Division"
    | Plus => "Addition"
    | BitwiseComplement => "BitwiseComplement"
    | LogicalNegation => "LogicalNegation"
    | Invalid => "Invalid Token"
    };
  acummulator ++ " " ++ result ++ ",";
};

let tokenListToString = tokensList => {
  let comma_regexp = [%re "/,$/"];
  let stringList = Belt.List.reduce(tokensList, "[", tokenToString);
  Js.String.replaceByRe(comma_regexp, " ]", stringList);
};

let printTokenList = tokenList => {
  tokenList |> tokenListToString |> Js.log;
  tokenList;
};