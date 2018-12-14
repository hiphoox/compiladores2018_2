let special_chars_regexp = [%re "/^({|}|\\(|\\)|;)/"];
let const_regex = [%re "/^[0-9]+/"];
let id_regexp = [%re "/\\w+/"];

let startsWith = program =>
  switch (Js.String.match(special_chars_regexp, program)) {
  | Some(value) => (value[0], Js.String.substringToEnd(~from=1, program))
  | None => ("None", program)
  };

let getId = program =>
  switch (Js.String.match(id_regexp, program)) {
  | Some(value) => 
    if(value[0] == "return" || value[0] == "int"){
      (
      Token.Keyword(program),
      Js.String.substringToEnd(~from=Js.String.length(program), program),
      )
    }
    else{
      (
      Token.Id(value[0]),
      Js.String.substringToEnd(~from=Js.String.length(value[0]), program),
      )
    };  
  | None => (Invalid, "")
  };

let getConstant = program =>
  switch (Js.String.match(const_regex, program)) {
  | Some(value) => (
      Token.Constant(int_of_string(value[0])),
      Js.String.substringToEnd(~from=Js.String.length(value[0]), program),
    )
  | None => (Invalid, "")
  };

let getComplexTokens = program =>
  if (Js.String.match(const_regex, program) != None ) {
    getConstant(program);
  } else {
    getId(program);
  };

let rec lexRawTokens = input =>
  if (Js.String.length(input) == 0) {
    [];
  } else {
    let (token, remainingProgram) =
      switch (startsWith(input)) {
      | ("{", rest) => (Token.OpenBrace, rest)
      | ("}", rest) => (Token.CloseBrace, rest)
      | ("(", rest) => (Token.OpenParen, rest)
      | (")", rest) => (Token.CloseParen, rest)
      | (";", rest) => (Token.Semicolon, rest)
      | (_, rest) => getComplexTokens(rest)
      };
    let remainingTokens = lexRawTokens(remainingProgram);
      [token, ...remainingTokens];
  };

let lexCollection = (acummulator, program) =>
  Belt.List.concat(acummulator, lexRawTokens(program));

let lex = program_text => {
  /*Removing all break lines and empty spaces*/
  let trimmed_program = Js.String.trim(program_text);
  let re = [%re "/\\s+/"];
  let program = Js.String.splitByRe(re, trimmed_program);
  /* Invoking the lexer for each element of the collection */
  Belt.Array.reduce(program, [], lexCollection);
};


let program_text = {|
  int main(){return3;}
  |};

lex(program_text)
|> Token.printTokenList