let program_text = {|
  int main(){ 
    return 3;
  }
  |};

Lexer.lex(program_text)
|> Token.printTokenList
|> Parser.parse_program
|> Ast.printAST
|> Generator.generate_code;
