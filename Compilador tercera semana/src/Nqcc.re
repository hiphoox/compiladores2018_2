let program_text = {|
  int main(){ 
    return ---!!~~~~6 ;
  }
  |};

Lexer.lex(program_text)
|> Token.printTokenList
|> Parser.parse_program
|> Ast.printAST
|> Generator.generate_code;