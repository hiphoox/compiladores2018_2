let program_text = {|
  int   main    (  )  {   return100 ; }|};

Lexer.lex(program_text)
|> Token.printTokenList