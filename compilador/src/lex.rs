extern crate regex;
use self::regex::Regex;


pub enum Token{
    OpenBrace,
    CloseBrace,
    OpenParen,
    CloseParen,
    SemiColon,
    Identifier,
    IntKeyword,
    CharKeyword,
    ReturnKeyword,
    Int,

}




pub fn lex(programa: &str) -> Vec<Token>{
    let tok: Vec<&str> = programa.split(' ').collect();
    let reid = Regex::new(r"[A-Za-z][A-Za-z0-9_]*").unwrap();
    let reint = Regex::new(r"[0-9]*");
    let rechar= Regex::new(r"[[:punct:]]");
    let mut tokf = vec!();
    for x in tok{
      if reid.is_match(x){
          let cap =reid.captures(x).unwrap();

          match cap.get(0).map_or("", |m| m.as_str()) {
            "int" => tokf.push(Token::IntKeyword),
            "char" => tokf.push(Token::CharKeyword),
            "return" => tokf.push(Token::ReturnKeyword),
            _=> println!("id no encontrado"),
          }
      }

    }
    tokf
}
