type token =
  | OpenBrace
  | CloseBrace
  | OpenParen
  | CloseParen
  | Semicolon
  | ReturnKeyword
  | Id(string)
  | Constant(int)
  | Invalid;

let tokenToString = (acummulator, t: token): string => {
  let result =
    switch (t) {
    | OpenBrace => "OpenBrance"
    | CloseBrace => "CloseBrace"
    | OpenParen => "OpenParen"
    | CloseParen => "CloseParen"
    | Semicolon => "Semicolon"
    | ReturnKeyword => "ReturnKeyword"
    | Id(n) => "(Id: " ++ n ++ ")"
    | Constant(n) => "(Constant: " ++ string_of_int(n) ++ ")"
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